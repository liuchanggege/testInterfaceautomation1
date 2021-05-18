
from __future__ import unicode_literals
from lib import request
import  json
import random
import string
#登录获取token
# a = request.Test_myRequest('http://api.longpean.com/login/login', 'POST',
#                            data={'mobile': '15214382625', 'password': 'lc123456'})
#
# print(a.res.headers.get('Authorization'))
#
# result = a.res.json()
# print(result)
# headers={'Authorization':a.res.headers.get('Authorization')}
#
#
# # 列表查询，没用
# # data ={"linkUrl":"","simpleTitle":"","productLevel":"","developType":"","audiStatus":"","allSee":"","checkStatus":1,"status":"","currentPage":1,"pageSize":50,"createdBy":"141","permisson":1}
# # a=request.Test_myRequest('https://papi.longpean.com/tProductNew/queryProductNewList', 'POST',
# #                            json=data,headers=headers)
# # print(a.res.json())
#
#
# # 获取返回token
# data2 = {"bucket":"test","envir":"test_tk"}
# a=request.Test_myRequest('http://picture.longpean.com//picture/token', 'POST',
#                            data=data2)
# l=str(random.randrange(1,1000000))
#
# #上传图片到文件服务器
# m="18172_161951963194912"+l+".jpeg"
# data1 = {"token":json.loads(a.res.json().get('data')).get('token'),"key":m}
# file= {"file": open("/Users/liuchang/Downloads/A6B5A_803.jpg", "rb")}
# a=request.Test_myRequest('https://up.qiniup.com/', 'POST',
#                            data=data1,files=file)
# print(a.res.json())
#
# # 保存新品
# s=''.join(random.sample(string.ascii_lowercase,5))
# itemurl="http://www.ebay.com.qqq1"+s
#
# simpleTitle="测试商品"+l
# print(simpleTitle)
#
#
# data={"imageUrl": "http://tk.longpean.com/"+m,"linkUrl":itemurl,"developType":0,"note": "","simpleTitle": simpleTitle,"productNature":0,"station":"", "detargetId":"","goodStore": 1,"dulizhanStore": 0,"amazonStore": 0}
#
# a=request.Test_myRequest('http://api.longpean.com/tProductNew/saveOrUpdateProductNew', 'POST',
#                            data=data,headers=headers)
#
# print(a.res.json().get("data").get('id'))
# id=a.res.json().get("data").get('id')
#
#
# #审核通过
# data3= {"ids":id,"checkStatus":2}
#
# a=request.Test_myRequest('http://api.longpean.com/tProductNew/updateProductNewAuditBatch', 'POST',
#                            data=data3,headers=headers)
#
# print(a.res.json())
# #
# #获取父sku
#
# a=request.Test_myRequest('http://api.longpean.com/skuRules/getFatherSku', 'GET',
#                            headers=headers)
#
# print(a.res.json().get("data"))
# FatherSKu=a.res.json().get("data")
# #获取子sku
# data4= {"parentSku":FatherSKu,"sku":"","num":1}
#
# a=request.Test_myRequest('http://api.longpean.com/skuRules/getSku', 'POST',
#                            json=data4,headers=headers)
#
# print(a.res.json().get('data')[0])
#
# sku =a.res.json().get('data')[0]
#
# #
# #
# #
# #
# #
# #
# #
# # 获取返回token
# data5 = {"bucket":"test","envir":"test_tk"}
# a=request.Test_myRequest('http://picture.longpean.com//picture/token', 'POST',
#                            data=data5)
# l1=str(random.randrange(1,1000000))
#
# #上传图片到文件服务器
# m="161951963194912"+l1+"/A6B5A_803.jpeg"
# data6 = {"token":json.loads(a.res.json().get('data')).get('token'),"key":m}
# file= {"file": open("/Users/liuchang/Downloads/A6B5A_803.jpg", "rb")}
# a=request.Test_myRequest('https://up.qiniup.com/', 'POST',
#                            data=data6,files=file)
# print(a.res.json())
# key = a.res.json().get("key")
# url= "http://tk.longpean.com/"+key
#
#
#
# #添加sku和链接关系
#
# data7= [{"hasDefault":1,"sku":sku,"links":"https://detail.1688.com/offer/582177627118.html?spm=a26352.b28411319.offerlist.1.5d871e62VBZakz","supplierName":"永康市一心硅胶制品厂","url_supplierName":"永康市一心硅胶制品厂","supplierId":17729}]
#
# a=request.Test_myRequest('http://api.longpean.com/owp/inventoryWarning/addListLinks', 'POST',
#                            json=data7,headers=headers)
#
# print(a.res.json())
#
# subSku= {"subSku":[{"subId":"","sku":sku,"colour":"","weight":2,"size":"","cost":2,"startNum":1,"inWide":"2","inHigh":"2","inLong":"2","outWide":"2","outHigh":"2","outLong":"2","inNetweight":2,"subUrl":[]}]}
#
# url = {"file":[{"url":url,"fileType":0,"main":1,"sourceType":3}]}
# json3 ={'productSellingPoint':'', 'subSku':json.dumps(subSku), 'specialCount1':'', 'parentSku':FatherSKu, 'specialCount3':'', 'itemUrl':'http://www.ebay.com.qqq1rkvic','productLevel':'','tagName':'','salerName':'新品','status':-3,'fixedDescription':'','suitTarget3':'','category_ids':'208,508','radomDescription':'111111','purchaser':'向梦洁','productCertificate':'','sourceType':2, 'url': json.dumps(url),'specialCount2':'','queryKey':'','znProductName':simpleTitle,'cateIds':'208,508','radomDescriptionCn':'1111111','enProductTitle':'a b c d e f g h i j k','productNewId':id,'suitTarget2':'','keyword': 'a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk', 'aliasCnName':'111','suitTarget1':'','productFullCate':'汽车、摩托车(Automobiles & Motorcycles)>>力帆汽车销售(Auto Sale)'}
#
# json4={'params2':[{'inLong':'2','outLong':'2','inHigh':'2','style':'','outWide':'2','inWide':'2','specs':'','sku':FatherSKu,'inNetweight':2,'CostPrice':2,'bmpFile':'No Image','goodsName':simpleTitle,'supportName':'永康市一心硅胶制品厂','linkUrl':'https://detail.1688.com/offer/582177627118.html?spm=a26352.b28411319.offerlist.1.5d871e62VBZakz','weight': 2,'outHigh':'2'}],'sonData1':{'goodsCategoryId':'508','unit':'','sampleCount':0,'aliasCnName':'111','specs':'','cateIds':'208,508','PackingRatio': 0,'purchaser':'向梦洁','GoodsCount':0,'originCountry':'China','selfMake':0,'brand':'','USEDueDate':'2069-05-31 11:21:46','MinNum':1,'productCertificate':'','hscode':'1111','StoreID':17,'MaxNum':1,'notes':'','StockDays':3,'sourceType':2,'SellDays':2,'itemUrl':'http://www.ebay.com.qqq1rkvic','CategoryCode':'208,508','category_ids':'208,508','SalerName':'新品','declaredValue':1,'SalerName2':'刘畅','material':'','packageCount':0,'goodAttrs':'7','AliasEnName':'111','packName':'','packFee':0}}
#
# data8={"id":id,"json":json.dumps(json4,ensure_ascii=False).replace("\'", '\"'),"json1":json.dumps(json3,ensure_ascii=False).replace("\'", '\"')}
# print("data8: %s" %data8)
# data9=json.dumps(data8,ensure_ascii=False)
# print("data9: %s" %data9)
#
# data10={"id":4808,"json1":"{\"status\":-3,\"url\":\"{\\\"file\\\":[{\\\"url\\\":\\\"http://tk.longpean.com/1619593400746/辅图33.jpg\\\",\\\"fileType\\\":0,\\\"main\\\":1,\\\"sourceType\\\":3}]}\",\"productFullCate\":\"汽车、摩托车(Automobiles & Motorcycles)>>力帆汽车销售(Auto Sale)\",\"cateIds\":\"208,508\",\"fixedDescription\":\"\",\"category_ids\":\"208,508\",\"parentSku\":\"A6B9G\",\"salerName\":\"新品\",\"purchaser\":\"向梦洁\",\"enProductTitle\":\"a b c d e f g h i j k l m n\",\"queryKey\":\"\",\"radomDescriptionCn\":\"111111111\",\"radomDescription\":\"111111111\",\"specialCount1\":\"\",\"specialCount2\":\"\",\"specialCount3\":\"\",\"suitTarget1\":\"\",\"suitTarget2\":\"\",\"suitTarget3\":\"\",\"aliasCnName\":\"1111\",\"znProductName\":\"测试商品376771\",\"productCertificate\":\"\",\"subSku\":\"{\\\"subSku\\\":[{\\\"subId\\\":\\\"\\\",\\\"sku\\\":\\\"A6B9G\\\",\\\"colour\\\":\\\"\\\",\\\"weight\\\":2,\\\"size\\\":\\\"\\\",\\\"cost\\\":2,\\\"startNum\\\":1,\\\"inWide\\\":\\\"2\\\",\\\"inHigh\\\":\\\"2\\\",\\\"inLong\\\":\\\"2\\\",\\\"outWide\\\":\\\"2\\\",\\\"outHigh\\\":\\\"2\\\",\\\"outLong\\\":\\\"2\\\",\\\"inNetweight\\\":2,\\\"subUrl\\\":[]}]}\",\"sourceType\":2,\"productNewId\":4808,\"itemUrl\":\"http://www.ebay.com.qqq1ovphk\",\"tagName\":\"\",\"keyword\":\"a\\nb\\nc\\nd\\ne\\nf\\ng\\nh\\ni\\nj\\nk\\nl\\nm\\nn\",\"productLevel\":\"\",\"productSellingPoint\":\"\"}","json":"{\"sonData1\":{\"goodsCategoryId\":\"508\",\"cateIds\":\"208,508\",\"specs\":\"\",\"CategoryCode\":\"208,508\",\"category_ids\":\"208,508\",\"itemUrl\":\"http://www.ebay.com.qqq1ovphk\",\"SalerName\":\"新品\",\"purchaser\":\"向梦洁\",\"StockDays\":3,\"brand\":\"\",\"unit\":\"\",\"USEDueDate\":\"2069-05-31 11:21:46\",\"goodAttrs\":\"7\",\"SalerName2\":\"刘畅\",\"packFee\":0,\"material\":\"\",\"packName\":\"\",\"MaxNum\":1,\"MinNum\":1,\"SellDays\":2,\"GoodsCount\":0,\"StoreID\":17,\"packageCount\":0,\"sampleCount\":0,\"PackingRatio\":0,\"productCertificate\":\"\",\"selfMake\":0,\"hscode\":\"11111\",\"AliasEnName\":\"1111\",\"declaredValue\":1,\"originCountry\":\"China\",\"notes\":\"\",\"sourceType\":2,\"aliasCnName\":\"1111\"},\"params2\":[{\"bmpFile\":\"No Image\",\"sku\":\"A6B9G\",\"goodsName\":\"测试商品376771\",\"weight\":2,\"CostPrice\":2,\"style\":\"\",\"inWide\":\"2\",\"inHigh\":\"2\",\"inLong\":\"2\",\"outWide\":\"2\",\"outHigh\":\"2\",\"outLong\":\"2\",\"specs\":\"\",\"inNetweight\":2,\"linkUrl\":\"https://detail.1688.com/offer/582177627118.html?spm=a26352.b28411319.offerlist.1.5d871e62VBZakz\",\"supportName\":\"永康市一心硅胶制品厂\"}]}"}
# print("data10: %s" %data10)
# print(type(data8),type(data9),type(data10))
# a=request.Test_myRequest('http://api.longpean.com/tProductNew/saveProduct', 'POST',
#                            json=data8,headers=headers)
#
#
# print(a.res.json())
# parentSkuId=a.res.json().get('data')
#
#
# #添加ProductFileAz
#
# data11={"url":[],"parentSku":FatherSKu,"parentSkuId":parentSkuId,"list":[{"subId":"","sku":sku,"colour":"","storeName":"上海仓","size":"","competingGoodsPrice":"","inWide":2,"inLong":2,"inHigh":2,"outLong":2,"outWide":2,"outHigh":2,"airTransFee":"","seaTransFee":"","finalFreight":"","inNetweight":2,"style":"","url":[]}]}
#
# a=request.Test_myRequest('http://api.longpean.com/productParentSkuInfo/addProductFileAz', 'POST',
#                            json=data11,headers=headers)
#
# print(a.res.json())
#
#
# #
# #添加ParentSku
#
# subsku1={"subSku":[{"subId":"","sku":sku,"colour":"","storeName":"上海仓","weight":2,"size":"","cost":2,"startNum":1,"used":"0","subUrl":"","competingGoodsPrice":"","inWide":2,"inLong":2,"inHigh":2,"outLong":2,"outWide":2,"outHigh":2,"airTransFee":"","seaTransFee":"","finalFreight":"","inNetweight":2,"style":""}]}
# data12={"developType":0,"status":0,"url":json.dumps(url),"id":parentSkuId,"productFullCate":"汽车、摩托车(Automobiles & Motorcycles)>>力帆汽车销售(Auto Sale)","cateIds":"208,508","parentSku":FatherSKu,"salerName":"刘畅","responserName":"刘畅","enProductTitle":"a b c d e f g h i j k","queryKey":"a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk","productCertificate":"","radomDescriptionCn":"1111111","radomDescription":"111111","fixedDescription":"","znProductName":simpleTitle,"isphoto":"","competingGoodsMonthSales":"","estimatedMonthSale":"","productLevel":"","productSellingPoint":"","suitTarget1":"","suitTarget2":"","suitTarget3":"","specialCount1":"","specialCount2":"","specialCount3":"","subSku":json.dumps(subsku1),"tagName":"","keyword":"a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk"}
#
# print(data12)
#
# a=request.Test_myRequest('http://api.longpean.com/productParentSkuInfo/addParentSku', 'POST',
#                            json=data12,headers=headers)
#
# print(a.res.json())
#
# #普货二审通过
# data13= {"spuId":parentSkuId,"goodAttrs":7,"storeId":17}
#
# print(data13)
# a=request.Test_myRequest('http://api.longpean.com/productParentSkuInfo/modifyGoodAttrs', 'POST',
#                            data=data13,headers=headers)
#
# print(a.res.json())
#
# #添加检查
#
# data14= {"checkStatus":1,"notes":"审核通过","parentSkuId":parentSkuId,"recommendFlag":0}
#
# print(data14)
# a=request.Test_myRequest('http://api.longpean.com/productParentSkuInfo/addCheckInfo', 'POST',
#                            data=data14,headers=headers)
#
# print(a.res.json())


if __name__ == '__main__':
    a={"id":54254,"json1":"{\"status\":-3,\"url\":\"{\\\"file\\\":[{\\\"url\\\":\\\"http://pspk.longpean.com/1620719114028/辅图11.jpg\\\",\\\"fileType\\\":0,\\\"main\\\":1,\\\"sourceType\\\":1},{\\\"url\\\":\\\"http://pspk.longpean.com/1620719170267/辅图11.jpg\\\",\\\"fileType\\\":0,\\\"main\\\":0,\\\"sourceType\\\":1}]}\",\"productFullCate\":\"汽车、摩托车(Automobiles & Motorcycles)>>力帆汽车销售(Auto Sale)\",\"category_ids\":\"208,508\",\"parentSku\":\"A2S8U\",\"salerName\":\"新品\",\"purchaser\":\"胡云昆\",\"queryKey\":\"\",\"aliasCnName\":\"111\",\"znProductName\":\"测试商品图片11\",\"productCertificate\":\"\",\"subSku\":\"{\\\"subSku\\\":[{\\\"subId\\\":\\\"\\\",\\\"sku\\\":\\\"A2S8U\\\",\\\"colour\\\":\\\"\\\",\\\"weight\\\":2,\\\"size\\\":\\\"\\\",\\\"cost\\\":2,\\\"startNum\\\":1,\\\"inWide\\\":\\\"2\\\",\\\"inHigh\\\":\\\"2\\\",\\\"inLong\\\":\\\"2\\\",\\\"outWide\\\":\\\"2\\\",\\\"outHigh\\\":\\\"2\\\",\\\"outLong\\\":\\\"2\\\",\\\"inNetweight\\\":2,\\\"subUrl\\\":[]}]}\",\"sourceType\":2,\"productNewId\":54254,\"itemUrl\":\"http://www.ebay.com.dsds1\",\"tagName\":\"\",\"keyword\":\"a\\nb\\nc\\nd\\ne\\nf\\ng\\nh\\ni\\njk\",\"cateIds\":\"208,508\",\"fixedDescription\":\"\",\"enProductTitle\":\"a b c d e f g h i jk\",\"radomDescriptionCn\":\"1111111\",\"radomDescription\":\"1111111\",\"specialCount1\":\"\",\"specialCount2\":\"\",\"specialCount3\":\"\",\"suitTarget1\":\"\",\"suitTarget2\":\"\",\"suitTarget3\":\"\",\"productLevel\":\"\",\"productSellingPoint\":\"\"}","json":"{\"sonData1\":{\"cateIds\":\"208,508\",\"specs\":\"\",\"brand\":\"\",\"unit\":\"\",\"SalerName2\":\"刘畅\",\"StoreID\":17,\"goodsCategoryId\":\"508\",\"CategoryCode\":\"208,508\",\"category_ids\":\"208,508\",\"itemUrl\":\"http://www.ebay.com.dsds1\",\"SalerName\":\"新品\",\"purchaser\":\"胡云昆\",\"StockDays\":3,\"USEDueDate\":\"2069-05-31 11:21:46\",\"goodAttrs\":\"7\",\"packFee\":0,\"material\":\"\",\"packName\":\"\",\"MaxNum\":1,\"MinNum\":1,\"SellDays\":2,\"GoodsCount\":0,\"packageCount\":0,\"sampleCount\":0,\"PackingRatio\":0,\"productCertificate\":\"\",\"selfMake\":0,\"hscode\":\"1111\",\"AliasEnName\":\"11111\",\"declaredValue\":1,\"originCountry\":\"China\",\"notes\":\"\",\"sourceType\":2,\"aliasCnName\":\"111\"},\"params2\":[{\"bmpFile\":\"No Image\",\"CostPrice\":2,\"specs\":\"\",\"sku\":\"A2S8U\",\"goodsName\":\"测试商品图片11\",\"weight\":2,\"style\":\"\",\"supplierId\":17729,\"inWide\":\"2\",\"inHigh\":\"2\",\"inLong\":\"2\",\"outWide\":\"2\",\"outHigh\":\"2\",\"outLong\":\"2\",\"inNetweight\":2,\"linkUrl\":\"https://detail.1688.com/offer/582177627118.html?spm=a26352.b28411319.offerlist.1.5d871e62VBZakz\",\"supportName\":\"永康市一心硅胶制品厂\"}]}"}

    b =json.dumps(a)
    c={'json': '{"sonData1":{"cateIds":"208,508","specs":"","brand":"","unit":"","SalerName2":"刘畅","StoreID":17,"goodsCategoryId":"508","CategoryCode":"208,508","category_ids":"208,508","itemUrl":"http://www.ebay.com.dsds1","SalerName":"新品","purchaser":"胡云昆","StockDays":3,"USEDueDate":"2069-05-31 11:21:46","goodAttrs":"7","packFee":0,"material":"","packName":"","MaxNum":1,"MinNum":1,"SellDays":2,"GoodsCount":0,"packageCount":0,"sampleCount":0,"PackingRatio":0,"productCertificate":"","selfMake":0,"hscode":"1111","AliasEnName":"11111","declaredValue":1,"originCountry":"China","notes":"","sourceType":2,"aliasCnName":"111"},"params2":[{"bmpFile":"No Image","CostPrice":2,"specs":"","sku":"A2S8U","goodsName":"测试商品图片11","weight":2,"style":"","supplierId":17729,"inWide":"2","inHigh":"2","inLong":"2","outWide":"2","outHigh":"2","outLong":"2","inNetweight":2,"linkUrl":"https://detail.1688.com/offer/582177627118.html?spm=a26352.b28411319.offerlist.1.5d871e62VBZakz","supportName":"永康市一心硅胶制品厂"}]}', 'id': 54254, 'json1': '{"status":-3,"url":"{\\"file\\":[{\\"url\\":\\"http://pspk.longpean.com/1620719114028/辅图11.jpg\\",\\"fileType\\":0,\\"main\\":1,\\"sourceType\\":1},{\\"url\\":\\"http://pspk.longpean.com/1620719170267/辅图11.jpg\\",\\"fileType\\":0,\\"main\\":0,\\"sourceType\\":1}]}","productFullCate":"汽车、摩托车(Automobiles & Motorcycles)>>力帆汽车销售(Auto Sale)","category_ids":"208,508","parentSku":"A2S8U","salerName":"新品","purchaser":"胡云昆","queryKey":"","aliasCnName":"111","znProductName":"测试商品图片11","productCertificate":"","subSku":"{\\"subSku\\":[{\\"subId\\":\\"\\",\\"sku\\":\\"A2S8U\\",\\"colour\\":\\"\\",\\"weight\\":2,\\"size\\":\\"\\",\\"cost\\":2,\\"startNum\\":1,\\"inWide\\":\\"2\\",\\"inHigh\\":\\"2\\",\\"inLong\\":\\"2\\",\\"outWide\\":\\"2\\",\\"outHigh\\":\\"2\\",\\"outLong\\":\\"2\\",\\"inNetweight\\":2,\\"subUrl\\":[]}]}","sourceType":2,"productNewId":54254,"itemUrl":"http://www.ebay.com.dsds1","tagName":"","keyword":"a\\nb\\nc\\nd\\ne\\nf\\ng\\nh\\ni\\njk","cateIds":"208,508","fixedDescription":"","enProductTitle":"a b c d e f g h i jk","radomDescriptionCn":"1111111","radomDescription":"1111111","specialCount1":"","specialCount2":"","specialCount3":"","suitTarget1":"","suitTarget2":"","suitTarget3":"","productLevel":"","productSellingPoint":""}'}
    print(a)
    subsku='"{\\"subSku\\":[{\\"subId\\":\\"\\",\\"sku\\":\\"A2S8U\\",\\"colour\\":\\"\\",\\"weight\\":2,\\"size\\":\\"\\",\\"cost\\":2,\\"startNum\\":1,\\"inWide\\":\\"2\\",\\"inHigh\\":\\"2\\",\\"inLong\\":\\"2\\",\\"outWide\\":\\"2\\",\\"outHigh\\":\\"2\\",\\"outLong\\":\\"2\\",\\"inNetweight\\":2,\\"subUrl\\":[]}]}"'
    c=json.loads(subsku)
    print(c)
    print(b)