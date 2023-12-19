import fitz  # PyMuPDF
import json

# JSONファイルから設定を読み込む
with open('settings.json', 'r', encoding='utf-8') as file:
    settings = json.load(file)



# Process each page in the document
class FacilityOverview:
    def loadPage(self, page):
        section_list = []
        tables = page.find_tables()
        if tables == None:
            return
        for table_num, table in enumerate(tables):
            section_size_dic = self.getSectionSizeDic(table.extract())
            for row_num, data_row in enumerate(table.extract()):
                section_def = self.getConfigSection(data_row[0])
                if section_def == None:
                    continue
                section_size = section_size_dic[data_row[0]]
                section_info = self.parse_and_set_data(section_def, table.extract()[row_num + 1:row_num + section_size])
                print("section_info = " + str(section_info))
                section_list.append(section_info)
        return section_list

    def getSectionSizeDic(self, data_rows):
        section_size_dic = {}
        i = 0
        pre_title = None
        for row_num, data_row in enumerate(data_rows):
            if None != self.getConfigSection(data_row[0]):
                if pre_title != None:
                    section_size_dic[pre_title] = i
                    i = 0
                pre_title = data_row[0]
            i = i + 1
        section_size_dic[pre_title] = i
        print(section_size_dic)
        return section_size_dic
    def getConfigSection(self,title):
        for section_def in settings["sections"]:
            if title == section_def["title"]:
                return section_def
        return None

    def parse_and_set_data(self, section_def, data_rows):
        title = section_def["title"]
        items = section_def["items"]
        section_info = {}

        for row in data_rows:
            for item in items:
                if item in row:
                    # 項目(item)の次(+1)が項目に対応する値とみなす
                    value = row[row.index(item)+1]
                    section_info[item] = value
        return section_info


class PdfLoader:
    def loadPDF(self, pdf_path):
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)
        # 各セクションの情報を格納する辞書を初期化
        page_list = []
        
        # Process each page in the document
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            #flist = FacilityList()
            columns = page.find_tables()[0].extract()[0]
            if columns[0] == settings["page_title"]:
                print("find 09")
                facility_page = FacilityOverview()
                section_list = facility_page.loadPage(page)
                page_list.append(section_list)
        
        
        # Close the PDF document
        pdf_document.close()
        return page_list
    

# Define the path to the PDF file
pdf_path = './R4hirobaichiran.pdf'
pdf_loader = PdfLoader()
page_list = pdf_loader.loadPDF(pdf_path)

# 抽出されたデータを表示
print("page_list = " + str(page_list))

