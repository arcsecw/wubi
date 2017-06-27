#!/usr/bin/env python  
# -*- encoding: utf-8 -*-
'''
__author__ = 'top'
date = '17/6/26'
我爱学习,学习使我快乐
'''
import pickle
import random
data = {}
with open('./wubi.pickle') as f:
    data = pickle.load(f)
print '原始映射表的中文映射五笔字典的总长度为{},五笔映射字典的总长度为{}'.format(len(data['cw']),len(data['wc']))


###########if you want add custom relation please modify this part!

# you just need to add custom relation to data['cw']

add_biaodian = zip(u'，。！？【】（）％＃＠＆１２３４５６７８９０；'\
                                                ,u',.!?[]()%#@&1234567890;')

for k,v in add_biaodian:
    data['cw'][k]=v


########### end ###########################################



cw = data['cw']
wc = {}
for k in cw :
    wubi = cw[k]
    weiba = ''
    while wc.get(wubi+weiba) !=None:
        weiba=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
    wc[wubi+weiba]=k

cw = {wc[k]:k for k in wc}

data['cw']=cw
data['wc']=wc
print '程序执行后映射表的中文映射五笔字典的总长度为{},五笔映射字典的总长度为{}'.format(len(data['cw']),len(data['wc']))

with open('./wubi.pickle','w') as f:
    pickle.dump(data,f)