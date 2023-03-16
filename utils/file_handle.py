# -*- coding: utf-8 -*- 
"""
Project: ComparePlayList
Author: guokaikuo
Create time: 2023-03-15 15:11
IDE: PyCharm
"""
import xml.etree.ElementTree as ET
import os

channels = {
    "CH01": "陕西卫视",
    "CH02": "陕西一套",
    "CH03": "陕西二套",
}


def xml_parser(file_path: str):
    # 判断xml文件格式
    f = os.path.basename(file_path)

    pl = f.split('.')
    file_name = ''.join(pl[:-1])
    file_format = pl[-1]
    if file_format != 'lis':
        return

    tree = ET.parse(file_path)
    root = tree.getroot()
    root_info = root.attrib
    # 获取文件头中的节目单类型，频道名称等
    playlist_type = root_info.get("strPSName", "None")
    playlist_chid = root_info.get("strCHID", None)
    playlist_channel = channels.get(playlist_chid, "None")

    print(playlist_type, playlist_channel, file_name)
    for child in root:
        print(child.tag, child.attrib)


if __name__ == '__main__':
    xml_parser('../2023-03-14pm.lis')
