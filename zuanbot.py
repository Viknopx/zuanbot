import random
import keyboard
from threading import Thread
import pyperclip as pclip
from os import system as system
import PySimpleGUI as sg


def str_open(filepath):
    str_list = []
    for i in open(filepath, 'r', encoding='UTF-8-sig'):
        str_list.append(i.strip())
    return str_list


def str_hlqk():
    rdm_num = random.randint(0, len(list_hlqk) - 1)
    copytext(list_hlqk[rdm_num])
    # return list_hlqk[rdm_num]


def str_ktff():
    rdm_num = random.randint(0, len(list_ktff) - 1)
    copytext(list_ktff[rdm_num])

    # return list_hlqk[rdm_num]


def key_hot():
    # 右键触发hello函数
    keyboard.add_hotkey('page_down', str_hlqk)
    keyboard.add_hotkey('page_up', str_ktff)
    # 阻塞，直至等待到ctrl+c信号
    keyboard.wait('ctrl + page_down + page_up')


def copytext(str):
    pclip.copy(str)


if __name__ == '__main__':
    try:
        list_hlqk = str_open('data/骂人宝典-火力全开.txt')
        list_ktff = str_open('data/骂人宝典-口吐芬芳.txt')
    except FileNotFoundError:
        print("FileNotFoundError:缺少数据文件，请将此文件放置data文件夹同级！")
        system('pause')
        exit(0)
    thread_hot = Thread(target=key_hot)
    thread_hot.start()
    print("运行成功：\n\n  PageUp阴阳怪气！\n  PageDown火力全开！\n  ctrl+page_down+page_up同时按下或叉掉对话框关闭程序！")

