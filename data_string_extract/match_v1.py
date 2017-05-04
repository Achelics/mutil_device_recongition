# -*- coding: utf-8 -*-

import re
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



#读取样本数据：
def read_sample_data(sample_data_path):
    sample_data_list = []   #定义保存样本数据的List
    with open(sample_data_path, 'r') as f:  #按行读取样本数据
        for line in f:
            # raw_data = json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            # new_line = eval(json.loads(raw_data))
            # print new_line
            brand = line.strip("\n")
            # model = new_line["Model"]

            brand1 = re.sub(r'\W', '', brand)  #将brand提取只含有字母和数字
            brand2 = brand1.replace('_', '')
            # model1 = re.sub(r'\W', '', model)  #将model提取只含有字母和数字
            # model2 = model1.replace('_', '')

            sample_data_list.append({'brand': brand2})  #都添加到List里面去，返回List
    f.close()
    return sample_data_list



#对需要进行匹配的数据进行读取以及拆分：
def split_data(line):
    #将样本中常见的但是对匹配无效的字段进行整理，便于接下来筛选
    invalid_word = ['camera', 'network', 'wireless', '720p','dome', 'bullet', 'box', 'pan', 'cam',
                    'box', '3mp', 'ptz', '1080p', 'vga', 'svga', 'ip', 'default', 'videl', 'fixed',
                    'pan', 'tilt', 'megapixel', 'cube', 'poe', 'outdoor' , 'indoor','server', 'ir', 'can', 'see',
                    'internet', '2mp', 'mini', 'password', 'name', 'admin', '.', 'video', 'wired',
                    'day', 'night', 'home', 'router']

    line1 = line.strip('\n').split('=')[-1]  #将数据的末尾换行去掉，然后取得“=”右边的数据
    line2 = line1.replace('"',' ').replace('_',' ').replace('/',' ').replace('\\',' ').replace(':',' ').replace('!',' ').replace('.',' ')  #将特殊符号替换成空格
    line3 = line2.lower().split(' ')  #按空格将数据拆分成一个一个需要匹配的Word

    word_list=[]  #对Word进行遍历，只要不在invalid_word里面的都将作为匹配的数据添加到List里面去，返回List
    for word in line3:
        if word and word not in invalid_word:
            word_list.append(word)
    return word_list



#进行word的匹配：
def mach_word(word, mylist):
    mach_word_list = []
    if (word and len(word) >= 3):  #word不为空并且长度大于3
        if not word.isdigit():  #word不可以全为数字
            for value in mylist:
                if value['brand'].lower() == (word.lower()):  #将word在brand里面匹配，只要满足一个就跳出来
                    result = {'brand': value['brand']} # 想当然的错误，只匹配品牌，型号根本不对
                    mach_word_list.append(result)
                    break
                # elif value['model'].lower().startswith(word.lower()):  #将word在model里面匹配，输出所有满足的
                #     result = {'brand': value['brand'], 'model': value['model']}# 想当然的错误，只匹配型号，品牌根本不对
                #     mach_word_list.append(result)
                else:
                    pass
    return mach_word_list

#对没有匹配到的word进行再次匹配
def second_mach_word(word,mylist):
    second_mach_word_list = []
    if '-' in word:  #判断是否含有“-”
        result_1 = mach_word(word.replace('-', ''),mylist)  #现删掉“-”,整体匹配，得到结果就输出，例如“tp-link，d-link”
        second_mach_word_list.extend(result_1)
        if result_1 == []:  #如果没有结果，就拆分成多个word进行匹配
            for new_word in word.split('-'):
                result_2 = mach_word(new_word,mylist)
                second_mach_word_list.extend(result_2)
                if result_2 == []:  #如果还是没有结果，就在判断它是否由字母和数字组成
                    if new_word.isalpha():
                        pass
                    else:
                        y = re.sub(r'\d', "", new_word)  #将由字母和数字组成的word中的数字删去，进行匹配
                        result_3 = mach_word(y,mylist)
                        second_mach_word_list.extend(result_3)
    else:
        if word.isalpha():
            pass
        else:
            y = re.sub(r'\d', "", word)  #word不含有“-”，将由字母和数字组成的word中的数字删去，进行匹配
            result_4 = mach_word(y,mylist)
            second_mach_word_list.extend(result_4)

    return second_mach_word_list



#对最后返回的list进行处理，注意*传入的List的元素必须是Dict
def output(output_list):
    output_result_list = []
    if output_list == []:  #list为空
        pass
        # print "Not Find"
    else:
        print "Find This"
        brand_list = []
        for value in output_list:  #将list元素中brand提取出来去重，输出
            brand_list.append(value['brand'])
        a = set(brand_list)
        for value1 in list(a):
            if value1 in brand_list:
                output_result_list.append(output_list[brand_list.index(value1)])
    return output_result_list




if __name__ == '__main__':
    my_list = read_sample_data(r'F:\mutil_result\brand_file\brand_list.json') #将样本数据保存到list里面
    with open(r'F:\mutil_result\401_brand_analysis\match_401.json', 'a+') as fw:  #打开match。json文件，便于写入数据
        with open(r'F:\mutil_result\401_brand_analysis\80-http-banner-zgrab-results-401_0_string.json', 'r') as f:  #打开需要匹配的数据
            for line in f.readlines():
                word_list = split_data(line)
                result_list = []
                for word in word_list:
                    first_result = mach_word(word,my_list)
                    result_list.extend(first_result)
                    if first_result == []:
                        second_result = second_mach_word(word,my_list)
                        result_list.extend(second_result)
                write_line = {'Input':line, 'Output': output(result_list)}
                fw.write(('%s\n') % write_line)