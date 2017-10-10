#-*- coding:utf-8 -*-
def save_file(boy, girl, count):

    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'
    boy_file = open(file_name_boy, 'w')
    girl_file = open(file_name_girl, 'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()


def split_file(filename):

    f = open(filename) #打开文件
    boy = []
    girl = []
    count = 1

    for each_line in f:
        if each_line[0:6] != '======':
            (role, line_spoken) = each_line.split('：', 1) #使用split函数，通过中文的“：”进行分割，后面的数字“1”表示分割一次，变成两块
            if role == '小甲鱼':
                boy.append(line_spoken) #将小甲鱼说的话写入到boy这个list里面去
            if role == '小客服':
                girl.append(line_spoken)#将小客服说的话写入到girl这个list里面去
        else:
            save_file(boy, girl ,count) #调用函数
            # 初始化boy和girl列表，并且自增
            boy = []
            girl = []
            count += 1

    save_file(boy, girl, count)

    f.close() #关闭文件

split_file(r'E:\python\-learn-python\小甲鱼python\一个文件任务\record.txt')