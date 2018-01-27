# coding:utf-8
"""
    author:Lindow
    date:2018/1/27
"""
from numpy import *
# 生成矩阵
def load_data(path):
    f = open(path).readlines()
    data = []
    for i in f:
        data.append([float(j) for j in i.strip().split(' ')])
    return data
# 生成用户间关联度
def create_matrix(dataset):
    data = mat(dataset)
    m,n = shape(data)
    p = zeros([m,m])
    for i in xrange(m):
        for j in xrange(m):
            value1 = 0
            value2 = 0
            value3 = 0
            for k in xrange(n):
                #print data[i][k]
                value1 += (data[i, k] * data[j, k])
                value2 += data[i, k] ** 2
                value3 += data[j, k] ** 2
            p[i, j] = value1 / (sqrt(value2*value3))
    return p

# 获取指定用户被推荐的图书
def high_score_user(dataset, marrix, topnum, user):
    tmp = {}
    for key, value in enumerate(marrix[user-1]):
        if len(tmp) <topnum:
            if value == 1.0:
                continue
            else:
                tmp[key] = value
        else:
            for i in range(topnum):
                tmp1 = sorted(tmp.items(), key=lambda item: item[1])
                if value == 1:
                    break
                elif value > tmp1[i][1]:
                    del tmp[tmp1[i][0]]
                    tmp[key] = value
                    break
    final = []
    for i in range(len(dataset[finaluser-1])):
        if dataset[finaluser-1][i] == 0.0:
            total_a = 0
            total_b = 0
            for j in tmp.keys():
                if dataset[j][i] !=0.0:
                    total_a += tmp[j]*dataset[j][i]
                    total_b += tmp[j]
            if total_b != 0:
                dic = {}
                dic[i] = total_a/total_b
                final.append(dic)
    return final




if __name__ == "__main__":
    # x轴为图书评分，y轴位用户
    dataset = load_data('./data1')
    marrix = create_matrix(dataset)
    # 被推荐图书的用户
    finaluser = 2
    # 推荐图书的前几位
    topuser = 3
    user = high_score_user(dataset, marrix, topuser, finaluser)
    print user