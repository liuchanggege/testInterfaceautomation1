import requests

class Test_myRequest(object):

    def __init__(self,url,method,params=None,json=None,data=None,headers=None,files=None):
        self.url=url
        self.method=method
        self.json=json
        self.data=data
        self.headers=headers
        self.params=params
        self.files=files
        if method=='POST':
            self.post()
        else:
            self.get()
    def post(self):
        res=requests.post(url=self.url,json=self.json,data=self.data,headers=self.headers,files=self.files)
        self.res=res


    def get(self):
        res=requests.get(url=self.url,params=self.params,headers=self.data)
        self.res=res

        return self.res

if __name__ == '__main__':
    a = Test_myRequest('http://127.0.0.1:8000/api/user/login', 'POST',
                               data={'username': 'liuchang', 'passwd': 'Lc123456'})
    print(a.res.json())


