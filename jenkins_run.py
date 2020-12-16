import os
import shutil
import time
import sys
import pytest
from util.reportHelp import set_allure_environment, set_allure_report_title, set_allure_logo, set_allure_logo_text

currentPath = os.path.dirname(os.path.abspath(__file__))
print(currentPath)


def run_test():
    date = time.strftime("%Y-%m-%d", time.localtime())
    report_path = os.path.join(currentPath, 'report', str(date))
    if os.path.exists(report_path):
        shutil.rmtree(report_path)
    test_ed = os.path.join(currentPath, 'TestCase')  # 执行文件夹下面的所有测试用例
    pytest.main([test_ed, '--alluredir=%s' % report_path, '-o log_cli=true -o log_cli_level=INFO'])
    print("**************** done ****************")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        report_path = sys.argv[1]
        set_allure_report_title(report_path + "/html", {"reportName": "第一版本"})
        set_allure_environment(report_path + "/html")
        set_allure_logo(report_path + "/html")
        set_allure_logo_text(report_path + "/html", "API")
    else:
        run_test()
