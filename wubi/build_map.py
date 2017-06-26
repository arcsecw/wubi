#!/usr/bin/env python  
# -*- encoding: utf-8 -*-
'''
__author__ = 'top'
date = '17/6/26'
我爱学习,学习使我快乐
'''
import cPickle
import random
data = {}
with open('./wubi.cPickle') as f:
    data = cPickle.load(f)

print '原始映射表的中文映射五笔字典的总长度为{},五笔映射字典的总长度为{}'.format(len(data['cw']),len(data['wc']))
#添加一些自定义的中文到英文的映射关系
add_biaodian = zip(u'，。！？【】（）％＃＠＆１２３４５６７８９０；'\
                                                ,u',.!?[]()%#@&1234567890;')

for k,v in add_biaodian:
    data['cw'][k]=v

#重建反向映射表
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

with open('./wubi.cPickle','w') as f:
    cPickle.dump(data,f)