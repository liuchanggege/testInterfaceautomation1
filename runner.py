# import lib.request
# import lib.connect_mysql
import unittest
from BeautifulReport import BeautifulReport
import os
import time
import logging

BASEPATH = os.path.abspath('./')
CASEPATH = os.path.join(BASEPATH,'case')
REPORTPATH = os.path.join(BASEPATH,'result')
LOGPATH = os.path.join(BASEPATH,'log')
today = time.strftime('%Y-%m-%d%H%M%S')
LOGNAME = '%s-log.txt' % today
print(CASEPATH)
print(REPORTPATH)


if __name__ == '__main__':
    # discover = unittest.defaultTestLoader.discover(CASEPATH, 'test_*.py')
    # logging.basicConfig(filename=os.path.join(LOGPATH, LOGNAME), level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # file_name = '%s-report.html' % today  # 报告文件名
    # fp = open(os.path.join(REPORTPATH,file_name), 'wb')  # wb方式写入
    # runner=HTMLTestRunner(stream=fp, title='测试报告', description='aguest_master项目用例执行情况',verbosity=2)
    # runner.run(discover)
    print(CASEPATH)
    discover = unittest.defaultTestLoader.discover(CASEPATH, 'test_*.py')  # 找运行
    logging.basicConfig(filename=os.path.join(LOGPATH, LOGNAME), level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    runner = BeautifulReport(discover)  # 运行用例
    today = time.strftime('%Y-%m-%d%H%M%S')
    file_name = '%s-report.html' % today  # 报告文件名
    runner.report('测试报告-%s' % today, filename=file_name, log_path=REPORTPATH)  # 产生报告
