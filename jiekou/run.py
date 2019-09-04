from tools.read_excel import ReadExcel
from tools.requests01 import DoRequest


data = ReadExcel('testcases\\接口测试用例模板.xlsx', 'Sheet1')
testcases = data.read_data()
for testcase in testcases:
    url = testcase[1]
    casename = testcase[3]
    method = testcase[5]
    data = eval(testcase[7])
    http_status_code = testcase[8]
    expect_res = testcase[9]


go = DoRequest(url, data=data)
respone = go.requests_post()
print(respone.status_code)
try:
    assert respone.status_code == http_status_code
    print('通过')
except:
    print('失败')