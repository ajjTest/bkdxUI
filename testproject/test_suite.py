import unittest
import time
import sys
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('casetests', pattern='aaa.py')
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='测试deafult报告', report_dir='E:\workplace/bkdxweb/baokaodaxue/testproject/reports', theme='theme_default')




    # fp.close()












