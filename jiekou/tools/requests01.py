import requests


class DoRequest:

    def __init__(self, url, data):
        self.url = url
        self.data = data
        

    def requests_post(self):
        res = requests.post(self.url, self.data)
        return res

    def requests_get(self):
        res1 = requests.get(self.url)
        return res1
