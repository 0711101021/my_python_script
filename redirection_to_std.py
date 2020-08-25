import sys
import pdb

'''
重定向所有的输入和输出到标准输入和输出
'''
class Redirection:
    def __init__(self,in_obj,out_obj):
        self.input=in_obj
        self.output=out_obj

    def read_line(self):
        res = self.input.read_line()
        self.output.write(res)
        return res

if __name__ == "__main__":
    # pdb.set_trace()
    # 如果不是以终端的方式运行脚本，则自动重定向输入和输出
    if not sys.stdin.isatty():
        sys.stdin = Redirection(in_obj=sys.stdin,out_obj=sys.stdout)
    a = input("Enter a string: ")
    b = input("Enter another string: ")
    print('Entered strings are:',repr(a),'and',repr(b))
