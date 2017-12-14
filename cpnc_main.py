#! python 3

import os
#Area Code Match the procvince
from L86AreaCode import _86ac
# cellphone number match area code
from CM20NumLogic import _20nl

def getResult():
    currentFolder = os.getcwd()
    targetFile = currentFolder + "/test.txt"
    if(os.path.isfile(targetFile)):
        with open(targetFile,'r+') as fh:        
            for l in fh.readlines():
                l = l.replace('\n','')
                _num = l.rstrip()[0:7]
                _acname = ACNameByNum(_num)
                l = l + _acname
                fh.write(l)
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
    getResult()
    return True

main()
