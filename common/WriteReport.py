import json
import xlwt
from xlutils.copy import copy
from tool.Tool import Tool


class WriteReport:
    def __init__(self):
        pass

    def write_report(self,url, interface_name,params, expect, actual, flag):
        open_file = Tool.read_excel("report")
        table = open_file.sheets()[0]
        n = table.nrows
        wb = copy(open_file)
        write_sheet = wb.get_sheet(0)

        params = json.dumps(params, ensure_ascii=False)  # 默认不将中文编码
        expect = json.dumps(expect, ensure_ascii=False)
        expect = Tool.json_converted_str(expect)
        actual = json.dumps(actual, ensure_ascii=False)
        actual = Tool.json_converted_str(actual)

        style = xlwt.easyxf('align: wrap on')  # 数据写入excel自动换行
        write_sheet.col(2).width = (30 * 367)
        write_sheet.col(3).width = (30 * 367)

        write_sheet.write(n, 0, url)
        write_sheet.write(n, 1, interface_name)
        write_sheet.write(n, 2, params)
        write_sheet.write(n, 3, expect, style)
        write_sheet.write(n, 4, actual, style)

        if flag == 1:
            write_sheet.write(n, 5, u"测试通过")
            Tool.log("测试通过",'test')
            print("测试通过")
        else:
            write_sheet.write(n, 5, u"测试失败")
            Tool.log("测试失败", 'test')
            print("测试失败")
        wb.save(r"../test_report/report.xls")
        # print("报告书写完成")
