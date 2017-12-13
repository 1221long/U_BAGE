#! python 3
# encoding=utf8
'''
import sys
from imp import reload
reload(sys)
print(sys.getdefaultencoding)
'''

import os
#Area Code Match the procvince
from L86AreaCode import _86ac
# cellphone number match area code
from CM20NumLogic import _20nl

import linecache

def getResult_w1():
    currentFolder = os.getcwd()
    sourceFile = currentFolder + "/test.txt"
    targetFile = currentFolder + "/target.txt"
    if(os.path.exists(targetFile)): 
        os.remove(targetFile)

    tf = open(targetFile, 'w',encoding='utf8')
        
    with open(sourceFile,'r+') as fh:        
        for l in fh.readlines():
            l = l.replace('\n','')
            _num = l.rstrip()[0:7]
            _acname = ACNameByNum(_num)
            l = l + _acname
            tf.write(l)
            tf.write('\n')
    
    tf.flush()
    tf.close()
    print('w1_over')
    return True

def getResult_w2():
    currentFolder = os.getcwd()
    sourceFile = currentFolder + "/test.txt"
    targetFile = currentFolder + "/target.txt"

    if(os.path.exists(targetFile)):
        os.remove(targetFile)

    tf = open(targetFile, 'w',encoding='utf8')

    if(os.path.isfile(sourceFile)):
        slc = 0
        for l in enumerate(open(sourceFile, 'r+')):
            slc += 1
    
    tlc = 1
    while tlc <= (slc+1):
        l = linecache.getline(sourceFile, tlc)
        l = l.replace('\n','')
        _num = l.rstrip()[0:7]
        _acname = ACNameByNum(_num)
        l = l + _acname
        tf.write(l)
        tf.write('\n')        
        linecache.clearcache()
        tlc += 1
    
    tf.flush()
    tf.close()
    print('w2_over')
    return True


def ACNameByNum(num):
    if(int(num) in _20nl):
        _ac = _20nl[int(num)]
        if(_ac in _86ac):
            _name = _86ac[int(_ac)]
        else:
            return '    unknown'
    else:
        return '    unknown'
    return '    '+ _name

def main():
    getResult_w1()
    print('main_over')
    return True

main()
