#!/usr/bin/env python3
import requests
from os import mkdir, path
from time import time
import json


def check_url(url):
    try:
        requests.get(url)
        return True
    except Exception:
        return False


def get_headers():
    headers = {}
    header = input("\n> Headers (ex: accept:text/html): ")
    while header:
        if ':' in header:
            key, val = header.split(':')
            headers[key] = val
        header = input()
    return headers


def get_params():
    params = []
    param = input("\n> Parameters (ex: 's=mark', ...): ")
    while param:
        params.append(param)
        param = input()
    return '?' + '&'.join(params)


def check_body(body):
    if not body:
        return True
    try:
        json.loads(body)
        return True
    except Exception:
        return False


def get_response(method, url, headers, body):
    if method == 'get':
        response = requests.get(url, json=body, headers=headers)
    elif method == 'post':
        response = requests.post(url, json=body, headers=headers)
    elif method == 'put':
        response = requests.put(url, json=body, headers=headers)
    elif method == 'delete':
        response = requests.delete(url, json=body, headers=headers)
    elif method == 'patch':
        response = requests.patch(url, json=body, headers=headers)
    elif method == 'head':
        response = requests.head(url, json=body, headers=headers)
    else:
        response = requests.options(url, json=body, headers=headers)
    return response


def check_response(response):
    scode = response.status_code
    if scode in range(400, 500):
        status = 'client_error'
    elif scode in range(500, 600):
        status = 'server_error'
    else:
        status = 'data'
    file_type = response.headers['Content-Type'].split('/')[-1].split(';')[0]
    content = response.text
    return status, file_type, content


def main():
    # get urls:
    url = input("\n> Your API's url (Enter to take default: 'http://www.omdbapi.com/'): ")
    if url:
        url = url.strip('/')
        while not check_url(url):
            url = input("\n> Wrong url, try again: ").strip('/')
    else:
        url = "http://www.omdbapi.com/"

    # get method:
    method = input("\n> Method: ")
    while method not in ('get', 'post', 'put', 'delete', 'patch', 'head', 'options'):
        method = input("\n> Method should be in ['get', 'post', 'put', 'delete', 'patch', 'head', 'options'] > ")

    # get params
    params = get_params()
    if params:
        url = url + params

    # get headers
    user_headers = get_headers()

    # get body
    body = input('\n> Body (in json type): ')
    while not check_body(body):
        body = input('\n> Wrong data, please input the right json type: ')

    print("\n> Requested url: %s" % url)

    # store response data and error log
    response = get_response(method, url, user_headers, body)
    status, file_type, content = check_response(response)
    request_time = str(time())
    if status == 'data':
        if not path.exists('response_data'):
            mkdir('response_data')
        file_name = 'response_data/' + request_time + '_' + method + '.' + file_type
        print('<%s> Saved in %s' % (response.status_code, file_name))
    else:
        if not path.exists('error_log'):
            mkdir('error_log')
        file_name = 'error_log/' + request_time + '_' + status + '.' + file_type
        print('<%s> Saved in %s' % (response.status_code, file_name))
    with open(file_name, 'w') as f:
        f.write(content)


if __name__ == '__main__':
    flag = input("> Hi there, start app?[OK] ")
    while flag == "OK":
        main()
        flag = input("\n> Add another API?[OK] ")
    print('\n Have a nice day :)\n')

