import datetime

curr_time = datetime.datetime.now()
curr_time = curr_time.strftime("[%Y-%m-%d %H:%M:%S] ")

open_text = open('log.log',mode='a+')
open_text.write(curr_time)
open_text.write('hello\n')
open_text.close()