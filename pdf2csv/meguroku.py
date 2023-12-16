import fitz  # PyMuPDF
import pandas as pd

# Define the path to the PDF file
pdf_path = './R4hirobaichiran.pdf'

# Open the PDF file
pdf_document = fitz.open(pdf_path)


class FacilityOverview:
    def __init__(self):
        self.location = None
        self.floor = None
        self.responsible_department = None
        self.year_of_establishment = None
        self.purpose_area = None
        self.management_type = None
        self.management_period = None
        self.opening_hours = None
        self.closing_days = None
        self.facility_structure = None
        self.establishment_ordinance = None
        self.remarks = None

    def parse_and_set_data(self, data_rows):
        for row in data_rows:
            if '所在地' in row:
                self.location = row[row.index('所在地')+1]
                print("location : " + self.location)
            if '階' in row:
                self.floor = row[row.index('階')+1]
                print("floor : " + self.floor)
            if '担当所管' in row:
                self.responsible_department = row[row.index('担当所管')+1]
            if '開設年度' in row:
                self.year_of_establishment = row[row.index('開設年度')+1]
            if '用途別面積' in row:
                self.purpose_area = row[row.index('用途別面積')+1]
            if '運営形態（直営・委託・指定管理）' in row:
                self.management_type = row[row.index('運営形態（直営・委託・指定管理）')+1]
    def loadPage(self, page):
        tables = page.find_tables()
        if tables == None:
            return
        for table_num, table in enumerate(tables):
            for row_num, data_row in enumerate(table.extract()):
                if data_row[0] == "１\u3000施設の概要":
                    summary_line = row_num
                    self.parse_and_set_data(table.extract()[row_num:row_num + 9])
                    break



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
    flist = FacilityList()
    columns = page.find_tables()[0].extract()[0]
    if columns[0] == "09 保育園\n【用途中分類】":
        print("find 09")
        facility_page = FacilityOverview()
        facility_page.loadPage(page)
    #flist.getList(page_num,page)
    

# Close the PDF document
pdf_document.close()

