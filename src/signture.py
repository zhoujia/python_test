'''
Created on 2015-4-6

@author: zhoujia
'''
import hashlib
import urlparse
import urllib

def _verfy_ac(private_key, params):
    items=params.items()

    items.sort()

    params_data = "";
    for key, value in items:
        params_data = params_data + str(key) + str(value)
    params_data = params_data + private_key

    sign = hashlib.sha1()
    sign.update(params_data)
    signature = sign.hexdigest()

    return signature

params = {"Action":"CreateUHostInstance","CPU":1,"ChargeType":"Trial","DiskSpace":50,"ImageId":"uimage-qiut5g","LoginMode":"Password","Memory":2048,"Name":"UCloudExample01","PublicKey":"ucloudliao@tarena.com.cn14280420270002130655531","Password":"123456","Region":"cn-north-03"}
#_verfy_ac('a169cf0457da7acf918a1e423847944ae6b255be',params)
#params = {"Action":"DescribeImage","ImageType":"Base","OsType":"Liunx","PublicKey":"ucloudliao@tarena.com.cn14280420270002130655531","Region":"cn-north-03"}
private_key = 'a169cf0457da7acf918a1e423847944ae6b255be'
print _verfy_ac(private_key,params)



