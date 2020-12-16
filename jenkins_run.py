import os
import shutil
import time

import pytest

currentPath = os.path.dirname(os.path.abspath(__file__))


def run_test(one=True):
    if one:
        date = time.strftime("%Y-%m-%d", time.localtime())
    else:
        date = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())
    report_path = os.path.join(currentPath, 'report', str(date))
    if os.path.exists(report_path):
        shutil.rmtree(report_path)
    test_ed = os.path.join(currentPath, 'TestCase')  # 执行文件夹下面的所有测试用例
    pytest.main([test_ed, '--alluredir=%s' % report_path, '-o log_cli=true -o log_cli_level=INFO'])
    os.system('cp ./report/environment.properties {}/environment.properties'.format(report_path))

    print("**************** done ****************")


if __name__ == '__main__':
    run_test()
