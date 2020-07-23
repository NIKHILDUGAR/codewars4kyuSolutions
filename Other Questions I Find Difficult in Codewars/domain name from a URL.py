# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python
def domain_name(url):
    url=url.replace("www.","")
    domain=url.split("//")[-1].split("/")[0]
    domain=domain.split(".")[0]
    return domain
    
#SMALLER SOLUTION (NOT MINE)
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
