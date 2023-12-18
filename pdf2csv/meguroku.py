import fitz  # PyMuPDF
import json

# JSONファイルから設定を読み込む
with open('settings.json', 'r', encoding='utf-8') as file:
    settings = json.load(file)

# Define the path to the PDF file
pdf_path = './R4hirobaichiran.pdf'

# Open the PDF file
pdf_document = fitz.open(pdf_path)

# 各セクションの情報を格納する辞書を初期化
section_list = []

# Process each page in the document
class FacilityOverview:
    def loadPage(self, page):
        section_data = {}
        tables = page.find_tables()
        if tables == None:
            return
        for table_num, table in enumerate(tables):
            for row_num, data_row in enumerate(table.extract()):
                section_def = self.getConfigSection(data_row[0])
                if section_def == None:
                    continue
                section_info = self.parse_and_set_data(section_def, table.extract()[row_num + 1:row_num + 10])
                print("section_info = " + str(section_info))
                section_list.append(section_info)

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
                    value = row[row.index(item)+1]
                    section_info[item] = value

        return section_info
#        if section_info:
#            print("section_info:" + str(section_info))
#            section_data[title] = section_info
#        else:
#            print("section_info:" + str(section_info))

    
class FacilityList:
    def getList(self,page_num,page):
        tables = page.find_tables()
        if tables == None:
            return

        print("page n : " + str(page_num))
        # Process each table found on the page
        for table_num, table in enumerate(tables):
            # Convert the table to a pandas DataFrame
            try:
                columns = table.extract()[0]
                data_rows = table.extract()[1:]
                if len(data_rows) == 0:
                    continue
                columns = [col for col in columns if col]
                if not columns:
                    continue
                # Filter out empty strings from data rows
                data_rows = [[cell for cell in row if cell] for row in data_rows]

                print("columns ->")
                print(columns)
                print("data_rows ->")
                print(data_rows)

                df = pd.DataFrame(data_rows, columns=columns)

                # Remove commas from numeric values
                df = df.applymap(lambda x: x.replace(',', '') if isinstance(x, str) and x.isdigit() else x)

                # Define the path to the output CSV file
                csv_path = f'./table_page{page_num}_table{table_num}.csv'

                # Write the DataFrame to a CSV file
                df.to_csv(csv_path, index=False)
            except:
                print("error at " + str(page_num))
                continue


# Process each page in the document
for page_num in range(pdf_document.page_count):
    page = pdf_document.load_page(page_num)
    #flist = FacilityList()
    columns = page.find_tables()[0].extract()[0]
#    if columns[0] == "09 保育園\n【用途中分類】":
    if columns[0] == settings["page_title"]:
        print("find 09")
        facility_page = FacilityOverview()
        facility_page.loadPage(page)
    #flist.getList(page_num,page)


# Close the PDF document
pdf_document.close()


# 抽出されたデータを表示
print("section_list = " + str(section_list))

