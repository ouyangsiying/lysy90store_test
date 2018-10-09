import config
import json
from common.NetworkRequest import NetworkRequest
from tool.Tool import Tool
from common.WriteReport import WriteReport
from common.Check import Check


# value_type:1:字符串，2：文件，3：需要token，4:需要加密
class Main:
    def __init__(self):
        self.net = NetworkRequest()
        self.check = Check()
        self.write = WriteReport()
        self.interface = Tool.read_json('interface')
        self.api = Tool.read_json('api')
        self.token = self.net.request_token()

    def run(self):
        for interface in self.interface['interfaces']:
            action_file = Tool.read_json(interface['addr'])
            interface_name = interface['name']

            actions = action_file['actions']  # 获取所有动作
            alldata = action_file['data']  # 获取所有测试数据

            for action in actions:

                interface = action["api"]  # 需要的接口
                dataname = action["data"]  # 需要的数据名字

                url, method, datas = self.get_one_api(self.api, interface)
                check, param, expect = self.get_one_data(dataname, alldata)

                param = self.data_processing(self.token, datas, param)
                self.request_method(url,interface_name, method, check, param, expect)


    # 获取一个接口信息
    def get_one_api(self, interface_list, interface):
        url = interface_list[interface]["url"]
        method = interface_list[interface]["method"]
        datas = interface_list[interface]["data"]
        return url, method, datas

    # 获取一条接口信息
    def get_one_data(self, dataname, datas):
        data = datas[dataname]
        check = datas[dataname]["check"]
        param = datas[dataname]["input"]
        expect = datas[dataname]["output"]
        return check, param, expect

    # 根据参数的类型处理参数
    def data_processing(self, token, types, param):
        for item in types:
            name = item['name']
            type = item['type']
            must = item['must']
            if type == 1:
                pass
            elif type == 2:
                pass
            elif type == 3:
                param[name] = token
            elif type == 4:
                param[name] = Tool.hash_password(param[name], token)
        return param

    def request_method(self, url,interface_name, method, check, param, expect_data):
        result_dict = {}
        if method == "get":
            result = self.net.get(url, param)
            result_dict = json.loads(result.content)
            print("实际结果", result_dict)
        if method == "post":
            result = self.net.post(url, param)
            result_dict = json.loads(result.content)
            print("请求参数",param)
            print("实际结果", result_dict)
        if method == "delete":
            result = self.net.post(url, param)
            result_dict = json.loads(result.content)
            print("实际结果", result_dict)
        if method == "put":
            result = self.net.post(url, param)
            result_dict = json.loads(result.content)
            print("实际结果", result_dict)
        if check == 1:
            flag = self.check.comparison_result_value(expect_data, result_dict)
            self.write.write_report(url, interface_name,param, expect_data, result_dict, flag)
        elif check ==2:
            flag = self.check.comparison_result(expect_data, result_dict)
            self.write.write_report(url, interface_name, param, expect_data, result_dict, flag)
        else:
            pass


if __name__ == '__main__':
    main = Main()
    main.run()
