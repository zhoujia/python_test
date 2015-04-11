'''
Created on 2015-4-7

@author: zhoujia
'''
import base64
def paramURL(url):
    str = url.split("&")
    str.sort();
    print str
    d={}
    for par in str:
        key = par.split("=")[0]
        value = par.split("=")[1]
        
        d[key] = value
    return d
        
    

print base64.b64encode('123456')
#paramURL('''OsType=Liunx&Action=DescribeImage&ImageType=Base&PublicKey=ucloudliao@tarena.com.cn14280420270002130655531&Region=cn-north-03&Signature=af3d05137f71b290adce2ee374ac25cf8679ea82''')