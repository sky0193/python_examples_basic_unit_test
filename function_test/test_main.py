import os

import unittest
import HtmlTestRunner

if __name__ == '__main__':
    testsuite = unittest.TestLoader().discover(os.path.dirname(__file__))
    report_path = os.path.join(os.path.dirname(__file__), "unit_test_report")
    h = HtmlTestRunner.HTMLTestRunner(combine_reports=True, output = report_path).run(testsuite)