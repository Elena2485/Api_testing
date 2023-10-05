from api.client import Client

class HttpBinApi(Client):
    HTML = "/html"
    BASE_URL = 'https://httpbin.org'
    ROBOTS = '/robots.txt'

    def list_html(self):
        """
        :method:    get
        :routs:     /html
        :status:    200
        """
        url = self.BASE_URL + self.HTML
        return self.get(url)

    def robots_txt(self):

        """
        :method:    get
        :routs:     /html
        :status:    200
        """
        url = self.BASE_URL + self.ROBOTS
        return self.get(url)

    def get_ip(self):
        url = self.BASE_URL + '/ip'
        return self.get(url)



http_bin_api = HttpBinApi()