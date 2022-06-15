import requests
import json


nvdpath = "https://services.nvd.nist.gov/rest/json/cve/1.0/"

def getnvd(parm):
    rparm=nvdpath+parm
    print (rparm)
    r = requests.get(rparm)
    return r

reqstr = " "
while reqstr != "" :
    reqstr= input ("CVE parm: ")
    print(reqstr)
    if reqstr !="":
         r = getnvd(reqstr)
    else:
         r = None
         
    if r!=None:
        for i in r.json():
            print (i)
    
