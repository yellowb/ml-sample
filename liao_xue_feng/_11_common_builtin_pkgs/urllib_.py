from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as url:
    data = url.read()
    print('Status: ', url.status, url.reason)
    print('Headers:')
    for k, v in url.getheaders():
        print(k, ' : ', v)

    print('Data:')
    print(data.decode('UTF-8'))
