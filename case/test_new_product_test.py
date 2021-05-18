from __future__ import unicode_literals

'this is a case about create product'
_author_ = 'liuchang'

import unittest
import logging
from lib import request
import os
import random
import string
import json
from lib.config import URL,MOBILE,PASSWORD,PICTURE_URL



class Test_new_product(unittest.TestCase):

    sku=''
    l=''
    m=''
    headers=''
    FatherSKu=''
    simpleTitle=''
    parentSkuId=''
    id=''
    imgurl=''
    url=''



    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # 登录
    def test_10(self):
        '''登录'''

        a = request.Test_myRequest(os.path.join(URL,'login/login'), 'POST',
                                   data={'mobile': MOBILE, 'password': PASSWORD})

        print(a.res.headers.get('Authorization'))
        result = a.res.json()
        headers = {'Authorization': a.res.headers.get('Authorization')}
        Test_new_product.headers=headers
        print(headers)
        self.assertEqual("200", result['errorCode'])
        logging.info('返回结果是：%s,header 是 %s' % (result, headers))

    # 上传新品图片
    def test_11(self):
        '''上传新品图片'''

        # 获取返回token
        data2 = {"bucket": "test", "envir": "test_tk"}
        a = request.Test_myRequest(PICTURE_URL, 'POST',
                                   data=data2)
        l = str(random.randrange(1, 1000000))
        Test_new_product.l = l

        # 上传图片到文件服务器
        m = "18172_161951963194912" + Test_new_product.l + ".jpeg"
        Test_new_product.m=m
        data1 = {"token": json.loads(a.res.json().get('data')).get('token'), "key": Test_new_product.m}
        file = {"file": open("/Users/liuchang/Downloads/A6B5A_803.jpg", "rb")}
        a = request.Test_myRequest('https://up.qiniup.com/', 'POST',
                                   data=data1, files=file)
        result = a.res.json()

        logging.info('返回结果是：%s' % result)

    # 保存新品
    def test_12(self):
        '''保存新品接口并返回新品id'''

        s = ''.join(random.sample(string.ascii_lowercase, 5))
        itemurl = "http://www.ebay.com.qqq1" + s

        simpleTitle = "测试商品" + Test_new_product.l
        Test_new_product.simpleTitle = simpleTitle

        data = {"imageUrl": "http://tk.longpean.com/" + Test_new_product.m, "linkUrl": itemurl, "developType": 0, "note": "",
                "simpleTitle": simpleTitle, "productNature": 0, "station": "us", "detargetId": "", "goodStore": 1,
                "dulizhanStore": 0, "amazonStore": 0}


        a = request.Test_myRequest(os.path.join(URL,'tProductNew/saveOrUpdateProductNew'), 'POST',
                                   data=data, headers=Test_new_product.headers)
        result = a.res.json()

        id = result.get("data").get('id')
        print(id)
        #拿到商品的id
        Test_new_product.id=id
        self.assertEqual("200", result['errorCode'])
    # 获取父sku
    def test_13(self):
        '''获取父sku接口'''
        a = request.Test_myRequest(os.path.join(URL,'skuRules/getFatherSku'), 'GET',
                                   headers=Test_new_product.headers)

        result = a.res.json()
        FatherSKu = result.get("data")
        Test_new_product.FatherSKu = FatherSKu
        self.assertEqual("200", result['errorCode'])

    # 获取子sku
    def test_14(self):
        '''获取子sku接口'''
        data4 = {"parentSku": Test_new_product.FatherSKu, "sku": "", "num": 1}

        a = request.Test_myRequest(os.path.join(URL,'skuRules/getSku'), 'POST',
                                   json=data4, headers=Test_new_product.headers)
        result = a.res.json()
        print(result.get('data')[0])

        sku = result.get('data')[0]
        Test_new_product.sku = sku
        self.assertEqual("200", result['errorCode'])

    # 主图上传
    def test_15(self):
        '''上传一个主图'''
        # 获取返回token
        data5 = {"bucket": "test", "envir": "test_tk"}
        a = request.Test_myRequest(PICTURE_URL, 'POST',
                                   data=data5)
        l1 = str(random.randrange(1, 1000000))

        # 上传图片到文件服务器
        m = "161951963194912" + l1 + "/A6B5A_803.jpeg"
        data6 = {"token": json.loads(a.res.json().get('data')).get('token'), "key": m}
        file = {"file": open("/Users/liuchang/Downloads/A6B5A_803.jpg", "rb")}
        a = request.Test_myRequest('https://up.qiniup.com/', 'POST',
                                   data=data6, files=file)
        print(a.res.json())
        key = a.res.json().get("key")
        imgurl = "http://tk.longpean.com/" + key
        Test_new_product.imgurl = imgurl

    # 添加sku和链接关系
    def test_16(self):
        '''保存供应商链接'''
        data7 = [{"hasDefault": 1, "sku": Test_new_product.sku,
                  "links": "https://detail.1688.com/offer/582177627118.html?spm=a26352.b28411319.offerlist.1.5d871e62VBZakz",
                  "supplierName": "永康市一心硅胶制品厂", "url_supplierName": "永康市一心硅胶制品厂", "supplierId": 17729}]

        a = request.Test_myRequest(os.path.join(URL,"owp/inventoryWarning/addListLinks"), 'POST',
                                   json=data7, headers=Test_new_product.headers)
    # 创建商品
    def test_17(self):
        '''创建商品接口'''
        subSku = {"subSku": [
            {"subId": "", "sku": Test_new_product.sku, "colour": "", "weight": 2, "size": "", "cost": 2, "startNum": 1, "inWide": "2",
             "inHigh": "2", "inLong": "2", "outWide": "2", "outHigh": "2", "outLong": "2", "inNetweight": 2, "subUrl": []}]}

        url = {"file": [{"url": Test_new_product.imgurl, "fileType": 0, "main": 1, "sourceType": 3}]}
        Test_new_product.url = url
        json3 = {'productSellingPoint': '', 'subSku': json.dumps(subSku), 'specialCount1': '', 'parentSku': Test_new_product.FatherSKu,
                 'specialCount3': '', 'itemUrl': 'http://www.ebay.com.qqq1rkvic', 'productLevel': '', 'tagName': '',
                 'salerName': '新品', 'status': -3, 'fixedDescription': '', 'suitTarget3': '', 'category_ids': '208,508',
                 'radomDescription': '111111', 'purchaser': '向梦洁', 'productCertificate': '', 'sourceType': 2,
                 'url': json.dumps(url), 'specialCount2': '', 'queryKey': '', 'znProductName': Test_new_product.simpleTitle,
                 'cateIds': '208,508', 'radomDescriptionCn': '1111111', 'enProductTitle': 'a b c d e f g h i j k',
                 'productNewId': Test_new_product.id, 'suitTarget2': '', 'keyword': 'a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk', 'aliasCnName': '111',
                 'suitTarget1': '', 'productFullCate': '汽车、摩托车(Automobiles & Motorcycles)>>力帆汽车销售(Auto Sale)'}

        json4 = {'params2': [
            {'inLong': '2', 'outLong': '2', 'inHigh': '2', 'style': '', 'outWide': '2', 'inWide': '2', 'specs': '',
             'sku': Test_new_product.FatherSKu, 'inNetweight': 2, 'CostPrice': 2, 'bmpFile': 'No Image', 'goodsName': Test_new_product.simpleTitle,
             'supportName': '永康市一心硅胶制品厂',
             'linkUrl': 'https://detail.1688.com/offer/582177627118.html?spm=a26352.b28411319.offerlist.1.5d871e62VBZakz',
             'weight': 2, 'outHigh': '2'}],
            'sonData1': {'goodsCategoryId': '508', 'unit': '', 'sampleCount': 0, 'aliasCnName': '111', 'specs': '',
                         'cateIds': '208,508', 'PackingRatio': 0, 'purchaser': '向梦洁', 'GoodsCount': 0,
                         'originCountry': 'China', 'selfMake': 0, 'brand': '', 'USEDueDate': '2069-05-31 11:21:46',
                         'MinNum': 1, 'productCertificate': '', 'hscode': '1111', 'StoreID': 17, 'MaxNum': 1,
                         'notes': '', 'StockDays': 3, 'sourceType': 2, 'SellDays': 2,
                         'itemUrl': 'http://www.ebay.com.qqq1rkvic', 'CategoryCode': '208,508',
                         'category_ids': '208,508', 'SalerName': '新品', 'declaredValue': 1, 'SalerName2': '刘畅',
                         'material': '', 'packageCount': 0, 'goodAttrs': '7', 'AliasEnName': '111', 'packName': '',
                         'packFee': 0}}

        data8 = {"id": Test_new_product.id, "json": json.dumps(json4, ensure_ascii=False),
                 "json1": json.dumps(json3, ensure_ascii=False)}
        print("data8: %s" % data8)

        a = request.Test_myRequest(os.path.join(URL,"tProductNew/saveProduct"), 'POST',
                                   json=data8, headers=Test_new_product.headers)
        result = a.res.json()
        parentSkuId = result.get('data')
        Test_new_product.parentSkuId=parentSkuId
        self.assertEqual("200", result['errorCode'])

    # 添加ProductFileAz
    def test_18(self):
        '''保存文件'''
        data11 = {"url": [], "parentSku": Test_new_product.FatherSKu, "parentSkuId": Test_new_product.parentSkuId, "list": [
            {"subId": "", "sku": Test_new_product.sku, "colour": "", "storeName": "上海仓", "size": "", "competingGoodsPrice": "",
             "inWide": 2, "inLong": 2, "inHigh": 2, "outLong": 2, "outWide": 2, "outHigh": 2, "airTransFee": "",
             "seaTransFee": "", "finalFreight": "", "inNetweight": 2, "style": "", "url": []}]}

        a = request.Test_myRequest(os.path.join(URL,"productParentSkuInfo/addProductFileAz"), 'POST',
                                   json=data11, headers=Test_new_product.headers)
        result=a.res.json()
        self.assertEqual("200", result['errorCode'])

        #
    # 添加ParentSku
    def test_19(self):
        '''保存商品'''
        subsku1 = {"subSku": [
            {"subId": "", "sku": Test_new_product.sku, "colour": "", "storeName": "上海仓", "weight": 2, "size": "", "cost": 2,
             "startNum": 1, "used": "0", "subUrl": "", "competingGoodsPrice": "", "inWide": 2, "inLong": 2, "inHigh": 2,
             "outLong": 2, "outWide": 2, "outHigh": 2, "airTransFee": "", "seaTransFee": "", "finalFreight": "",
             "inNetweight": 2, "style": ""}]}
        data12 = {"developType": 0, "status": 0, "url": json.dumps(Test_new_product.url), "id": Test_new_product.parentSkuId,
                  "productFullCate": "汽车、摩托车(Automobiles & Motorcycles)>>力帆汽车销售(Auto Sale)", "cateIds": "208,508",
                  "parentSku": Test_new_product.FatherSKu, "salerName": "刘畅", "responserName": "刘畅",
                  "enProductTitle": "a b c d e f g h i j k", "queryKey": "a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk",
                  "productCertificate": "", "radomDescriptionCn": "1111111", "radomDescription": "111111",
                  "fixedDescription": "", "znProductName": Test_new_product.simpleTitle, "isphoto": "", "competingGoodsMonthSales": "",
                  "estimatedMonthSale": "", "productLevel": "", "productSellingPoint": "", "suitTarget1": "",
                  "suitTarget2": "", "suitTarget3": "", "specialCount1": "", "specialCount2": "", "specialCount3": "",
                  "subSku": json.dumps(subsku1), "tagName": "", "keyword": "a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk"}



        a = request.Test_myRequest(os.path.join(URL,"productParentSkuInfo/addParentSku"), 'POST',
                                   json=data12, headers=Test_new_product.headers)

        result=a.res.json()
        print(result)
        self.assertEqual("200", result['errorCode'])

    # 普货二审通过
    def test_20(self):
        '''二审通过'''
        data13 = {"spuId": Test_new_product.parentSkuId, "goodAttrs": 7, "storeId": 17}

        a = request.Test_myRequest(os.path.join(URL,"productParentSkuInfo/modifyGoodAttrs"), 'POST',
                                   data=data13, headers=Test_new_product.headers)

        result=a.res.json()
        print(result)
        self.assertEqual("200", result['errorCode'])

    # 添加检查
    def test_21(self):
        '''添加检查'''
        data14 = {"checkStatus": 1, "notes": "审核通过", "parentSkuId": Test_new_product.parentSkuId, "recommendFlag": 0}

        a = request.Test_myRequest(os.path.join(URL,"productParentSkuInfo/addCheckInfo"), 'POST',
                                   data=data14, headers=Test_new_product.headers)

        result=a.res.json()
        print(result)
        self.assertEqual("200", result['errorCode'])


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(Test_new_product('test_1'))
    # suite.addTest(Test_login('test_2'))
    test_dir = './'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    runner = unittest.TextTestRunner()
    runner.run(discover)
