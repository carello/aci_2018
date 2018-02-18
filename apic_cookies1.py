import requests
import json
from pprint import pprint

ctrl = 'some ip'
user = 'some user'
pw = 'some password'


def get_cookies(a_apic):
    username = user
    password = pw
    url = a_apic + '/api/aaaLogin.json'
    auth = dict(aaaUser=dict(attributes=dict(name=username, pwd=password)))
    authenticate = requests.post(url, data=json.dumps(auth), verify=False)
    return authenticate.cookies


def get_subnets(a_apic, cookies):
    uri = '/api/class/fvSubnet.json'
    url = a_apic + uri
    req = requests.get(url, cookies=cookies, verify=False)
    response = req.text
    return response


def get_aep(a_apic, cookies):
    uri = '/api/node/mo/uni/tn-ABBOTT.json?query-target=subtree&target-subtree-class=fvAEPg'
    url = a_apic + uri
    req = requests.get(url, cookies=cookies, verify=False)
    response = req.text
    return response


def get_stuff(a_apic, cookies):
    uri = '/api/node/mo/uni/tn-ABBOTT.json?query-target=subtree&target-subtree-class=fvTenant,fvAp,fvAEPg,fvRsBd,fvCtx,fvRtCtx'
    url = a_apic + uri
    req = requests.get(url, cookies=cookies, verify=False)
    response = req.text
    return response


if __name__ == "__main__":
    protocol = 'http'
    host = ctrl
    apic = '{0}://{1}'.format(protocol, host)
    cookies = get_cookies(apic)

    rsp = get_subnets(apic, cookies)
    rsp_dict = json.loads(rsp)
    subnets = rsp_dict['imdata']

    r_aep = get_aep(apic, cookies)
    r_aep_dict = json.loads(r_aep)
    aeps = r_aep_dict['imdata']

    r_stuff = get_stuff(apic, cookies)
    r_stuff_dict = json.loads(r_stuff)
    stuff = r_stuff_dict['imdata']

    print('\n--- SUBNETS --')
    for subs in subnets:
        print(subs['fvSubnet']['attributes']['ip'])
    print('\n--- AEPS ---')
    pprint(aeps)
    print('\n--- STUFF ---')
    pprint(stuff)
