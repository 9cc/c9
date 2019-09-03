from tools.read_excel import ReadExcel


data = ReadExcel('F:\\Work\\jiekou\\testcases\\接口测试用例模板.xlsx', 'Sheet1')
testcases = data.read_data()
for testcase in testcases:
    print(testcase)