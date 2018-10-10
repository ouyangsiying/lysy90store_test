import json
import config
import xlrd
import hashlib
import datetime


class Tool:
    # 读json文件
    @staticmethod
    def read_json(filename):
        try:
            with open(config.rootPath+"/resource/" + filename + ".json", 'r', encoding='utf-8') as load_file:
                load_json_dict = json.load(load_file)
                return load_json_dict
        except Exception as e:
            print("读文件异常",e)
            Tool.log(e,'debug.log')
            exit()

    # 读excel
    @staticmethod
    def read_excel(filename):
        try:
            excel_file = xlrd.open_workbook(config.rootPath+"/test_report/" + filename + ".xls", formatting_info=True)
            return excel_file
        except Exception as e:
            print("读文件异常", e)
            Tool.log(e, 'debug.log')
            exit()

    # 将json字符串格式化
    @staticmethod
    def json_converted_str(str1):
        str2 = str(str1)
        str2 = str2.replace("{", "{\n")
        str2 = str2.replace(",", ",\n")
        str2 = str2.replace("}", "}\n")
        return str2

    # 加密密码
    @staticmethod
    def hash_password(password, token):
        hash_password1 = hashlib.sha1((password).encode('utf_8')).hexdigest()
        hash_password = hashlib.sha1((hash_password1+token).encode('utf_8')).hexdigest()
        return hash_password

    # 写日志
    @staticmethod
    def log(msg,filename = 'log'):
        curr_time = datetime.datetime.now()
        curr_time = curr_time.strftime("[%Y-%m-%d %H:%M:%S] ")
        open_text = open(config.rootPath+'/log/'+filename+'.log', mode='a+',encoding='utf8')
        open_text.write(curr_time)
        open_text.write(msg)
        open_text.write('\n')
        open_text.close()