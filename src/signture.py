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
    print items

    params_data = "";
    for key, value in items:
        params_data = params_data + str(key) + str(value)
    params_data = params_data + private_key
    print params_data
    sign = hashlib.sha1()
    sign.update(params_data)
    signature = sign.hexdigest()

    return signature

params = {"Action":"CreateUHostInstance","CPU":1,"ChargeType":"Trial","DiskSpace":50,"LoginMode":"Password","Memory":512,"Name":"UCloudExample01","PublicKey":"ucloudliao%40tarena.com.cn14280420270002130655531","Password":"123456","Region":"cn-north-03"}
#_verfy_ac('a169cf0457da7acf918a1e423847944ae6b255be',params)
private_key = 'a169cf0457da7acf918a1e423847944ae6b255be'
print _verfy_ac(private_key,params)



