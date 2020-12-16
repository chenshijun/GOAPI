import os
import json
import base64
import re


def get_json_data(json_path, value):
    with open(json_path, 'rb') as f:
        json_data = json.load(f)
        json_data = dict(json_data, **value)
    f.close()
    return json_data


def set_allure_report_title(report_path, value):
    path = report_path + "/widgets/summary.json"
    if os.path.exists(path):
        data = get_json_data(path, value)
        with open(path, 'w') as r:
            json.dump(data, r)
        r.close()
    else:
        set_allure_report_title()


def set_allure_environment(report_path):
    path = report_path + "/widgets/environment.json"
    if os.path.exists(path):
        with open(path, 'w') as r:
            data = [{
                "values": ["GOAPI"],
                "name": "项目名称"
            }, {
                "values": ["uat"],
                "name": "运行环境"
            }, {
                "values": ["阿bei"],
                "name": "作者"
            }, {
                "values": ["2.13.0"],
                "name": "allure版本"
            }, {
                "values": ["3.7.5"],
                "name": "python版本"
            }]
            json.dump(data, r)
        r.close()
    else:
        set_allure_environment()


def img2base64(image_bytes):
    with open(image_bytes, "rb") as fb:
        img = fb.read()
        base64_bytes = base64.b64encode(img)
        base64_str = base64_bytes.decode("utf-8")
    return base64_str


def set_allure_logo(path):
    image = "data:image/jpg;base64," + img2base64("./report/logo.png")
    file = path + "/styles.css"
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if "[dir=ltr] .side-nav__brand{background:url(" in line:
                bs64_str = \
                    re.findall("\[dir=ltr\] \.side-nav__brand{background:url\((.*?)\) no-repeat 0}.language-select",
                               line,
                               re.S)[0]
                line = line.replace(bs64_str + ") no-repeat 0",
                                    image + ") no-repeat 0; background-size: 45px 50px !important;")
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)


def set_allure_logo_text(path, text):
    file = path + "/app.js"
    file_data = ""
    logo_text = """<span class="'+l(__default(n(6)).call(s,"side-nav","brand-text",{name:"b",hash:{},data:a}))+'">Allure</span>"""
    new_test = """<span class="'+l(__default(n(6)).call(s,"side-nav","brand-text",{name:"b",hash:{},data:a}))+'">""" + text + "</span>"
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if logo_text in line:
                print(111)
                line = line.replace(logo_text, new_test)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)
