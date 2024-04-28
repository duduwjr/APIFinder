import re
import requests
import argparse
import pandas as pd

def banner():
    print('''
  ___  ______ ___________ _           _           
 / _ \ | ___ \_   _|  ___(_)         | |          
/ /_\ \| |_/ / | | | |_   _ _ __   __| | ___ _ __ 
|  _  ||  __/  | | |  _| | | '_ \ / _` |/ _ \ '__|
| | | || |    _| |_| |   | | | | | (_| |  __/ |   
\_| |_/\_|    \___/\_|   |_|_| |_|\__,_|\___|_|   

V-1.2.0                                    by Garry
    ''')
# 匹配 文件中的中的 API 路径
def API_extract_file(f, url2):
    with open(f, 'r', encoding='utf-8') as file1:
        content = file1.read()
    fileurl = 'url.txt'
    list = ["(/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+)+",
            "(/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+)+",
            "(/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+)+",
            "(/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+)+",
            "(/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+)+"]
    with open(fileurl, 'w') as file:
        file.write('')
    for api in list:
        pattern = re.findall(api, content)
        print(pattern)
        with open(fileurl, 'a') as file:
            # 遍历列表中的每个元素
            for item in pattern:
                # 将当前元素转换成字符串后添加到文件中，并自动换行
                file.write(str(item) + '\n')
    file.close()

    with open(fileurl, 'r') as file:
        content = file.readlines()

    # 在每行文本的前面都拼接上一个 URL 地址
    new_content = [f'{url2}{line.strip()}'
                   for line in content]

    # 将拼接后的结果保存到原文件中
    with open(fileurl, 'w') as file:
        file.write('\n'.join(new_content))

    print("URL 地址已成功添加到result.txt文件中。")

# 匹配 HTTPS 网页中的 JavaScript 中的 API 路径
def API_extract(url1, url2):
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url1, verify=False)
    fileurl = 'url.txt'
    list = ["(/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+)+",
            "(/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+)+",
            "(/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+)+",
            "(/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+)+",
            "(/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+/[a-zA-Z0-9][a-zA-Z0-9-#_\.]+)+"]
    with open(fileurl, 'w') as file:
        file.write('')
    for api in list:
        pattern = re.findall(api, response.text)
        print(pattern)
        with open(fileurl, 'a') as file:
            # 遍历列表中的每个元素
            for item in pattern:
                # 将当前元素转换成字符串后添加到文件中，并自动换行
                file.write(str(item) + '\n')
    file.close()

    with open(fileurl, 'r') as file:
        content = file.readlines()

    # 在每行文本的前面都拼接上一个 URL 地址
    new_content = [f'{url2}{line.strip()}'
                   for line in content]

    # 将拼接后的结果保存到原文件中
    with open(fileurl, 'w') as file:
        file.write('\n'.join(new_content))

    print("URL 地址已成功添加到result.txt文件中。")

# 去重
def remove_duplicate_lines(input_fp, output_fp):
    # 用于保存已经出现过的行
    lines_seen = set()
    with open(input_fp, 'r') as infile, open(output_fp, 'w') as outfile:
        for line in infile:
            if line not in lines_seen:
                outfile.write(line)
                lines_seen.add(line)

# 获取对应链接的响应码和长度
def traverse_urls(urls_txt,res_code):
    print(30*'*')
    with open(urls_txt, 'r') as f:
        for line in f.readlines():
            url = line.strip()
            response = requests.get(url, verify=False)
            length = len(response.text)
            res = response.status_code
            if res == res_code:
                print(f'URL: {url};响应码: {res};长度: {length}')
            else:
                continue
# 输出所有url响应信息
def all_info(urls_txt):
    print("正在输出所有url的响应信息，请等待...")
    data = []
    with open(urls_txt, 'r') as f:
        for line in f.readlines():
            url = line.strip()
            requests.packages.urllib3.disable_warnings()
            response = requests.get(url, verify=False)
            length = len(response.text)
            res = response.status_code
            data.append([url, res, length])

    df = pd.DataFrame(data, columns=['URL', 'Response Code', 'Length'])
    df.to_excel('result.xlsx', index=False)
    print("已将url响应信息输出到result.xlsx中")

# 用户传参
def user():
    parse = argparse.ArgumentParser(prog='APIFinder')  # 创建一个解析器对象

    parse.add_argument('-u', dest='url1', type=str, help='目标url(例如:http://xxx.com/x.js)')  # 添加可选参数
    parse.add_argument('-f', dest='file', type=str, help='目标文件(由于一些js需要下载才能查看，或者要扫一些代码文件中的地址，用此参数即可)')  # 添加可选参数
    parse.add_argument('-U', dest='url2', type=str, help='需要拼接的url(例如:http://xxx.com/xx)')  # 添加可选参数
    parse.add_argument('-i', dest='res', type=int, help='输出对应响应码的url及长度(例如:200)', nargs='+')  # 添加可选参数

    result = parse.parse_args()  # 开始解析参数
    return result

if __name__ == "__main__":
    banner()
    # txt 文件路径
    input_fp = "url.txt"
    # 去重后的文件路径
    output_fp = "result.txt"
    result = user()
    url2 = result.url2
    print(url2)
    if url2.endswith('/'):
        url2 = url2.rstrip('/')
    if result.url1:
        API_extract(result.url1, url2)
    if result.file:
        API_extract_file(result.file, url2)
    remove_duplicate_lines(input_fp, output_fp)
    all_info(output_fp)
    if result.res:
        traverse_urls(output_fp, result.res)