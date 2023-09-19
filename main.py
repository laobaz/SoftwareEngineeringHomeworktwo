from simhash import Simhash
import re
import jieba

import sys
# 清除html和符号和空格
def remove(file):
    result = re.compile(r'<[^>]+>', re.S).sub('', file).strip()
    punc = '~`!#$%^&*()_+-=|\';"＂:/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》{《}】【\n\]\[ '
    new_result = re.sub(r"[%s]+" % punc, "", result)

    return new_result


# 读取文件
def readfile(file):
    with open(file, 'r', encoding='UTF-8') as work:
        return remove(work.read())

def cutfile(file):
    file_list= jieba.cut(file,cut_all=True)
    return file_list




# 相似度比较
#使用simhash算法实现
def analyse(one, two):
    one_simhash = Simhash(one)
    two_simhash = Simhash(two)
    max_hashbit = max(len(bin(one_simhash.value)), len(bin(two_simhash.value)))
    #求汉明距离
    distince = one_simhash.distance(two_simhash)  # 汉明距离
    result = 1 - distince / max_hashbit
    return result



if __name__ == '__main__':

    if len(sys.argv) != 4:
        print('传入参数个数错误！')
        exit()

    one_file = sys.argv[1]
    two_file = sys.argv[2]
    ans_file = sys.argv[3]


    one_list = cutfile(readfile(one_file))
    two_list = cutfile(readfile(two_file))


    analyse_result= analyse(one_list,two_list)


    f = open(ans_file, 'w', encoding="utf-8")
    f.write("文章相似度： %.2f" % analyse_result)
    f.close()

    print("文章相似度：%.2f" % analyse_result)
