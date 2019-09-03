import xlrd


class ReadExcel:

    def __init__(self,filename, sheet_names):
        self.filename = filename
        self.sheet_names = sheet_names

    def read_data(self):
        res =[]
        data = xlrd.open_workbook(self.filename)
        table = data.sheet_by_name(self.sheet_names)

        for row in range(1, table.nrows):
            res.append(table.row_values(row))

        return res

    def write_data(self):
        pass

if __name__ == "__main__":
    data = ReadExcel('F:\\Work\\jiekou\\testcases\\接口测试用例模板.xlsx', 'Sheet1')
    print(data.read_data())
