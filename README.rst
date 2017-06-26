wubi
======

You do not need to modify your model when applied it to Chinese,you can translate chinese chars to wubi ,then you can process chinese chars like english

For example if you want to use character-level neural network model in chinese chars, you will find it is beteer to translate them from chinese to wubi at first.

当你处理汉语时,你不必修改你原来的模型。你可以将汉语翻译成五笔字型码。你就可以像处理英文一样的处理汉语了

比如说,如果你想使用一个字符级神经网络模型处理中文,你会发现最好先将这些汉语翻译成五笔字符。


重要提示
------

喜欢就star一下

if you like it , please star

Install
-------

.. code:: bash

    $ pip install wubi


Short introduce
-----

.. code:: python

    >>> import wubi
    >>> print wubi.get('WenChaoWang爱自由','cw')
    WenChaoWang ep thd mh

    >>> print wubi.get('WenChaoWang ep thd mh','wc')
    WenChaoWang爱自由

.. notice
    when your chinese text within english the ' ' will be drop
    //TODO

Long introduce
------

input:

当前自然语言处理模型中单词级模型效果很好，但是由于英文单词天然由空格隔开，中文只有连续的字与标点，为了将各种单词级语言模型应用于中文，中文分词成了中文自然语言处理领域一个基础性研究。近来研究表明，在很多神经网络模型中，字符级语言模型效果也很好，而且从长远来看，由于字符级语言模型比单词级语言模型保留了更多的原始信息，随着神经网络模型的发展以及计算能力的提高，字符级语言模型的效果应该会更好。将每一个中文汉字当做一个字符输入字符级语言模型会导致很多问题，实验效果相对英文语料来说并不理想，经实，验先将中文汉字转化为五笔字型码，输入模型计算后再将五笔字型码转换回汉字直观效果与英文语料相近。本着分享的精神将这一想法供广大的中文自然语言处理的童鞋一起分享，同时将我自己写的小工具开源出来。

output:

iv ue thd qd ygk yyy th gj saj gajf k ujfj yngk xe saj gajf uqt js tve vb , wjg j mh gf amd yygy ujfj yngk gd qd mh pw st bgk ga , k yygy kw e lpk xfn r pb gn sfi hko , o b uqf tk tkh ujfj yngk xe ygk yyy saj gajf yid et gf k yygy , k yygy wv yngk dn b k yygy thd qd ygk yyy th gj wycm fakgk g wh ad dbm ntg dga pwv . rp go dga pwv ge je , d tve qq pyj x mqq xtk saj gajf k , pb twf xe ygk yyy saj gajf uqt js bn tve vb , dmjr eg ww ta fqp go rhf , mh gf pb twf xe ygk yyy saj gajf xx ujfj yngk xe ygk yyy saj gajf wk qyvl b gjq qq r dr vck wy thn , bde udh pyj x mqq xtk saj gajf r v nae c ey yf tha ce lt r rj ym , pb twf xe ygk yyy saj gajf r uqt js yid yynwr wf gjq vb . uqf txg g wh k yygy ic pb iv wdt g wh pb twf lwg ty pb twf xe ygk yyy saj gajf wf nf gcftm tve qq ukd jghmt , pu cwg uqt js sh cf amd yygy ygk ou go yu ua i gj shn , x pu , cwg tfq uqf k yygy ic pb lfn wx o gg tt pb gajf dcg , lwg ty saj gajf yf tha rg gmf uqf gg tt pb gajf dcg lfn rq lkd ic pb fh cm uqt js gn amd yygy ygk ou sh rp . sg udh wv ybf r oge pyj uqf p g shn if waw yygt dd r k yygy thd qd ygk yyy th gj r ujff afffi g fhn wv ybf , m jf uqf q thd nng pgn r ih a hw ga idr bm go .

License
-------

`wubi` is free software, under an MIT-style license. See LICENSE for details.

