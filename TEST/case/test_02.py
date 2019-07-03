import requests
import unittest


class gongdan(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.h = {
        "Content-Type":"application/json; charset=utf-8",
        "authorization":"Digest_username='hoa', realm='HOA', nonce='7a5f3fc58ba8ae92caa8c7ba9ff9c550', uri='/', qop=auth, response='47e33fe29200e23c146d8fd50ee70ba', nc=00000001, cnonce='46b115b6484247249457daa9108ae1cd'",
        "Connection":"close",
        "node":"open",
        "accept":"application/json; charset=utf-8",
        "referer":"http://172.19.1.208:8190",
        "host":"172.19.1.208:8190"
    }
        self.url= "http://172.19.1.208:8190"
    def tearDown(self):
        pass

    def creat_wand(self):
        body={
             "CmdType": "NEW_INSTALLATION",
            "Parameter": {
                "NewInstallationArray" : [
                    {
                        "OrderNo": "201940101",
                        "PppoeAccount": "SMY4",
                        "ServiceCode": "wband",
                        "LOID": "201940102",
                        "AreaCode": "2301",
                        "PppoePassword": "1234",
                        "BANDWIDTH": "102400",
                        "Address": "光电园麒麟座B",
                        "Phone": "20"
                    }
                                        ]
                        }
            }
        r = requests.post()
        print(r.status_code)
        print(r.content.decode("utf_8"))


