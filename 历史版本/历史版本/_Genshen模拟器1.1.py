from easygui import *
ff = open(r'C:\the number.txt','a')
ff.close
ff = open(r'C:\the number.txt')
wenzi = ff.read()
ff.close()
ff = open(r'C:\the number.txt','w')
if wenzi == '':
    ff.write('1')
    wenzi = 0
else:
    ff.write(str(int(wenzi)+1))
wenzi = int(wenzi) + 1
ff.close()
if wenzi == 1:
    msgbox('七国·尘世·众生,向着星辰与深渊,开启你的冒险吧。首次开启加载较慢,请耐心等待',image='ban.jpg')
else:
    msgbox('这是你第{}次打开此程序,向着星辰与深渊,开启你的冒险吧'.format(wenzi),image = 'ban.jpg')
import threading
import numpy
import ctypes
import zipping
import random
import sys
import pygame
import time
from moviepy.editor import VideoFileClip

musicing1 = pygame.image.load("musicplayer.png")
musicing2 = pygame.image.load("musicplayer2.png")
musiclist = []
musiclist.append(r'镇守之森.mp3')
musiclist.append(r'何妄何执.mp3')
musiclist.append(r'甘雨.mp3')
musiclist.append(r'liyue.mp3')
musiclist.append(r'liyue2.mp3')
musiclist.append(r'温迪.mp3')
musiclist.append(r'test.mp3')
musiclist.append(r'test2.mp3')
yinyueshuliang = 7
dinggui = 0
dingguiobject = 'wuqi'
a = 0  # 总抽数
c = 0  # 五星保底
d = 0  # 五星总抽中数
sixingfangwai = 0
musicplayer = 0
musicloud = 0.5
b1 = 0  # 五星抽中数（歪）
b2 = 0
b3 = 0
b4 = 0
b5 = 0
b6 = 0
p = 0  # 五星歪数
oo = 0  # 五星防第二次歪
c1 = 0  # 四星
c2 = 0
c3 = 0
c4 = 0
c5 = 0
u = 0  # 四星保底
po = 0  # 四星总抽中数
ff = 0  # 四星保底数
d1 = 0  # 三星
d2 = 0
d3 = 0
d4 = 0
d5 = 0
d6 = 0
d7 = 0
d8 = 0
d9 = 0
d10 = 0
m0 = 0
m1 = 0
m2 = 0
m3 = 0
m4 = 0
m5 = 0
m6 = 0
m7 = 0
m8 = 0
m9 = 0
m10 = 0
m11 = 0
m12 = 0
m13 = 0
m14 = 0
m15 = 0
m16 = 0
m17 = 0
m18 = 0
m19 = 0
m20 = 0
m21 = 0
m22 = 0
m23 = 0
m24 = 0
m25 = 0
m26 = 0
m27 = 0
m28 = 0
m29 = 0
m30 = 0
m31 = 0
m32 = 0
m33 = 0
m34 = 0
m35 = 0
m36 = 0
m37 = 0
m38 = 0
m39 = 0
kq1 = 0
kq2 = 0
chouzhongprize1 = 0
chouzhongprize2 = 0
wushichou = 0
liushichou = 0
qishichou = 0
bashichou = 0
wuxingbaodi = 0
xingchen = 0
xinghui = 0
linshixingchen = 0
linshixinghui = 0
aa = True
cc = True
hhhhh = False
fff = False
gg = False
oiu = False
firsting = True
wuqi1 = True            #这个变量用于判断是否抽武器池，True为不是武器池，False为是武器池
green = (0, 255, 0)     #颜色设置
prize_list = ['甘雨', '温迪', '钟离', '武器池', '牛逼']            #这个是奖池的选项------------------------------------
listing = []                                                       #创建一个空列表，以便在抽奖过程中使用append向里面存储
file=r'test.mp3'
musicplay = True
prize = choicebox(msg='请选择祈愿奖池', title='原神', choices=prize_list)
if prize == None:                                                  #处理用户关闭choicebox--------------------------------
    print('程序退出成功')
    sys.exit(0)
elif prize == '温迪':
    prize1 = '温迪'
    prize2 = '温迪'#下面这一块用于导入需要用到的图片视频数据
    tupian = pygame.image.load("venty.jpg")
    tupian2 = pygame.image.load("venty2.jpg")
    tupian3 = pygame.image.load("venty3.jpg")
    tupian4 = pygame.image.load("venty4.jpg")
    video1 = VideoFileClip(r"温迪1.mp4")
    listw = ['芭芭拉', '菲谢尔', '香菱', '芭芭拉', '菲谢尔']
elif prize == '甘雨':
    prize1 = '甘雨'
    prize2 = '甘雨'
    tupian = pygame.image.load("ganyu.jpg")
    tupian2 = pygame.image.load("ganyu2.jpg")
    tupian3 = pygame.image.load("ganyu3.jpg")
    tupian4 = pygame.image.load("ganyu4.jpg")
    video1 = VideoFileClip(r"甘雨1.mp4")
    listw = ['多莉', '砂糖', '行秋', '多莉', '砂糖']
elif prize == '牛逼':
    prize1 = '刻晴，歪了，但没完全歪！'
    prize2 = '刻晴，歪了，但没完全歪！'
    tupian = pygame.image.load("nb.jpg")
    tupian2 = pygame.image.load("nb2.jpg")
    tupian3 = pygame.image.load("nb3.jpg")
    tupian4 = pygame.image.load("nb4.jpg")
    video1 = VideoFileClip(r"nb.mp4")
    listw = ['芭芭拉', '凝光', '班尼特', '芭芭拉', '凝光']
elif prize == '钟离':
    prize1 = '钟离'
    prize2 = '钟离'
    tupian = pygame.image.load("zhongli.jpg")
    tupian2 = pygame.image.load("zhongli2.jpg")
    tupian3 = pygame.image.load("zhongli3.jpg")
    tupian4 = pygame.image.load("zhongli4.jpg")
    video1 = VideoFileClip(r"钟离1.mp4")
    listw = ['柯莱', '迪奥娜', '菲谢尔', '柯莱', '迪奥娜']
elif prize == '武器池':
    prize1 = '苍古自由之誓'
    prize2 = '四风原典'
    tupian = pygame.image.load("gui.jpg")
    tupian2 = pygame.image.load("gui0.jpg")
    tupian3 = pygame.image.load("gui1.jpg")
    tupian4 = pygame.image.load("gui2.jpg")
    video1 = VideoFileClip(r"nb.mp4")
    listw = ['暗巷闪光', '幽夜华尔兹', '雨裁', '西风长枪', '流浪乐章']
    wuqi1 = False
else:
    sys.exit()
    tupian = pygame.image.load("1.jpg")
    tupian2 = pygame.image.load("2.jpg")
    tupian3 = pygame.image.load("3.jpg")
    tupian4 = pygame.image.load("4.jpg")
    video1 = VideoFileClip(r".mp4")
    listw = ['', '', '']
tupian = pygame.transform.scale(tupian, (1200, 600))                #更改图片大小以适应屏幕
tupian2 = pygame.transform.scale(tupian2, (1200, 600))
tupian3 = pygame.transform.scale(tupian3, (1200, 600))
tupian4 = pygame.transform.scale(tupian4, (1200, 600))
err = pygame.image.load("error.jpg")                                #处理错误用的图片
err = pygame.transform.scale(err, (1200, 600))
pr1 = listw[0]                                                      #取出当前用户选择奖池概率up的四星，角色池pr4和pr5为空
pr2 = listw[1]
pr3 = listw[2]
pr4 = listw[3]
pr5 = listw[4]
msgbox('在程序运行前，请检查涉及到的模块和字体你是否已悉数安装', title='警告', ok_button='我已知晓', image='cao.jpg')   #一个温馨提示
size = weight, height = 1200, 600    #创建pygame窗口----------------------------------------
screen = pygame.display.set_mode(size)    
pygame.mixer.quit()
pygame.init()
bg = (0, 0, 0)
screen.fill(bg)
pygame.display.set_caption(prize, '祈愿模拟器')


def aff(event):             #这是一个引入yp.py的函数，用于视频处理----------------------------------------------------------------------------------
    if event.type == pygame.MOUSEBUTTONDOWN:
        zipping.breakplay()
        logoimage = screen.blit(tupian, (0, 0))
        pygame.display.flip()

pygame.mixer.music.load(musiclist[musicplayer])
pygame.mixer.music.play()
musicplay = False
try:            #用于处理错误----------------------------------------
    if wuqi1:       #判断是否为武器池，如果是就跳过其中的内容
        for i in range(25):        #加载三张图片----------------------------------------
            screen.fill(bg)
            tupian2.set_alpha(20 * i)
            logoimage = screen.blit(tupian2, (0, 0))
            pygame.display.flip()
        while aa:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    screen.fill(bg)
                    logoimage = screen.blit(err, (0, 0))
                    pygame.display.flip()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    aa = False
        for i in range(25):
            screen.fill(bg)
            tupian2.set_alpha(500 - 20 * i)
            logoimage = screen.blit(tupian2, (0, 0))
            pygame.display.flip()
        aa = True
        for i in range(25):
            screen.fill(bg)
            tupian3.set_alpha(20 * i)
            logoimage = screen.blit(tupian3, (0, 0))
            pygame.display.flip()
        while aa:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    screen.fill(bg)
                    logoimage = screen.blit(err, (0, 0))
                    pygame.display.flip()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    aa = False
        for i in range(25):
            screen.fill(bg)
            tupian3.set_alpha(500 - 20 * i)
            logoimage = screen.blit(tupian3, (0, 0))
            pygame.display.flip()
        aa = True
        for i in range(25):
            screen.fill(bg)
            tupian4.set_alpha(20 * i)
            logoimage = screen.blit(tupian4, (0, 0))
            pygame.display.flip()
        while aa:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    screen.fill(bg)
                    logoimage = screen.blit(err, (0, 0))
                    pygame.display.flip()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    aa = False
        for i in range(25):
            screen.fill(bg)
            tupian4.set_alpha(500 - 20 * i)
            logoimage = screen.blit(tupian4, (0, 0))
            pygame.display.flip()
        aa = True
    for i in range(25):         #这是奖池的主页面图片
        screen.fill(bg)
        tupian.set_alpha(20 * i)
        logoimage = screen.blit(tupian, (0, 0))
        pygame.display.flip()
    logoimage = screen.blit(musicing1, (1140,60))
    pygame.display.flip()
    msgbox('按键盘‘H’键查看帮助', title='动身吧，旅行者，异世的诗篇还在等着我们呢', ok_button='好的',image = 'ooops8.jpg')
    while True:    #卡池部分循环
        size = weight, height = 1200, 600   #这两句用于重新加载窗口大小，用于处理视频播放后窗口大小的更改
        screen = pygame.display.set_mode(size)
        if musicplay:
            logoimage = screen.blit(tupian, (0, 0))
            logoimage = screen.blit(musicing2, (1140,60))
            pygame.display.flip()
        else:
            logoimage = screen.blit(tupian, (0, 0))
            logoimage = screen.blit(musicing1, (1140,60))
            pygame.display.flip()
        while aa:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    size = weight, height = 1200, 600
                    screen = pygame.display.set_mode(size)
                    screen.fill(bg)
                    logoimage = screen.blit(err, (0, 0))
                    pygame.display.flip()
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if (mouse_x > 905) and (mouse_x < 1200) and (mouse_y > 525) and (mouse_y < 600):#十连--------------------------------------------------------------------------------
                        t4 = 10
                        aa = False
                        hhhhh = True
                        fff = True
                    elif (mouse_x > 633) and (mouse_x < 905) and (mouse_y > 525) and (mouse_y < 600):#单发---------------------------------------------------------------------
                        t4 = 1
                        aa = False
                        hhhhh = True
                        gg = True
                    elif (mouse_x > 1125) and (mouse_x < 1200) and (mouse_y > 53) and (mouse_y < 100):#背景音乐---------------------------------------------------------------------
                        if musicplay:
                            pygame.mixer.music.load(musiclist[musicplayer])
                            pygame.mixer.music.play()
                            musicplay = False
                            logoimage = screen.blit(tupian, (0, 0))
                            logoimage = screen.blit(musicing1, (1140,60))
                            pygame.display.flip()
                        else:
                            pygame.mixer.music.stop()
                            musicplay = True
                            logoimage = screen.blit(tupian, (0, 0))
                            logoimage = screen.blit(musicing2, (1140,60))
                            pygame.display.flip()
                    elif (mouse_x > 390) and (mouse_x < 633) and (mouse_y > 525) and (mouse_y < 600):#自定义抽奖次数-----------------------------------------------------------------
                        bb = True
                        while bb:
                            t4 = enterbox('请输入一个小于等于2000的正整数',image = 'ooops6.jpg')
                            try:
                                if t4.isdecimal():#后面这段是为了处理用户输入的奇怪东西，当然可以用easygui中的integerbox，但用户体验会降低
                                    t4 = int(t4)
                                    if t4 <= 2000 and t4 > 0:
                                        bb = False
                                        aa = False
                                        hhhhh = False
                                        oiu = True
                                    else:
                                        msgbox('请输入一个在0-2000范围内的数字', ok_button='明白了',image = 'ooops4.jpg')
                                        bb = False
                                else:
                                    msgbox('请输入一个正整数', ok_button='明白了',image = 'ooops4.jpg')
                                    bb = False
                            except AttributeError:#这句话用于处理‘用户关闭窗口’的事件------------------------------
                                  bb = False
                    elif (mouse_x > 1072) and (mouse_x < 1104) and (mouse_y > 0) and (mouse_y < 53):#玩家点击原石按钮-----------------------------------------------------------------
                        msgbox('你想得美', title='原石用完了！',image = 'ooops7.jpg')
                    elif (mouse_x > 183) and (mouse_x < 330) and (mouse_y > 553) and (mouse_y < 600):#角色演示播放------------------------------------------------------------------
                        awqa = True
                        while firsting:
                            msgbox('来自派蒙的“温馨”提示：双击任意区域返回到主页面', ok_button='哦',image = 'ooops2.jpg')
                            firsting = False
                        pygame.mixer.quit()
                        pygame.init()
                        zipping.preview(video1, eventa=aff)
                        while awqa:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    awqa = False
                                    size = weight, height = 1200, 600
                                    screen = pygame.display.set_mode(size)
                                    pygame.init()
                                    screen.fill(bg)
                                    tupian =pygame.transform.scale(tupian, (1200, 600))
                                    musicplay = True
                                    logoimage = screen.blit(tupian, (0, 0))
                                    logoimage = screen.blit(musicing2, (1140,60))
                                    pygame.display.flip()
                    elif (mouse_x > 0) and (mouse_x < 150) and (mouse_y > 425) and (mouse_y < 550):
                        if not wuqi1:
                            if dingguiobject == 'wuqi':
                                dingguiyong = choicebox('请选择定轨武器',choices = ['苍古自由之誓','四风原典'])
                                if dingguiyong == '苍古自由之誓':
                                    dingguiobject = 'canggu'
                                elif dingguiyong == '四风原典':
                                    dingguiobject = 'sifeng'
                                elif dingguiyong == None:
                                    pass
                                dinggui = 0
                            else:
                                msgbox('定轨{}/2发'.format(dinggui))
                        else:
                            pass
                    elif (mouse_x > 0) and (mouse_x < 90) and (mouse_y > 0) and (mouse_y < 200):#切换祈愿池--------------------------------------------------------------------------------
                        prize = choicebox(msg='请选择祈愿奖池', title='原神', choices=prize_list)
                        oh = True
                        if prize == None:
                            oh = False
                        elif prize == '温迪':
                            prize1 = '温迪'
                            prize2 = '温迪'
                            tupian = pygame.image.load("venty.jpg")
                            video1 = VideoFileClip(r"温迪1.mp4")
                            listw = ['芭芭拉', '菲谢尔', '香菱','芭芭拉','菲谢尔']
                            wuqi1 = True
                        elif prize == '甘雨':
                            prize1 = '甘雨'
                            prize2 = '甘雨'
                            tupian = pygame.image.load("ganyu.jpg")
                            video1 = VideoFileClip(r"甘雨1.mp4")
                            listw = ['多莉', '砂糖', '行秋','多莉','砂糖']
                            wuqi1 = True
                        elif prize == '钟离':
                            prize1 = '钟离'
                            prize2 = '钟离'
                            tupian = pygame.image.load("zhongli.jpg")
                            video1 = VideoFileClip(r"钟离1.mp4")
                            listw = ['柯莱', '迪奥娜', '菲谢尔']
                            listw = ['柯莱', '迪奥娜', '菲谢尔', '柯莱', '迪奥娜']
                            wuqi1 = True
                        elif prize == '武器池':
                            prize1 = '苍古自由之誓'
                            prize2 = '四风原典'
                            tupian = pygame.image.load("gui.jpg")
                            tupian2 = pygame.image.load("gui0.jpg")
                            tupian3 = pygame.image.load("gui1.jpg")
                            tupian4 = pygame.image.load("gui2.jpg")
                            listw = ['暗巷闪光', '幽夜华尔兹', '雨裁', '西风长枪', '流浪乐章']
                            wuqi1 = False
                        else:
                            prize1 = '刻晴，歪了，但没完全歪！'
                            prize2 = '刻晴，歪了，但没完全歪！'
                            tupian = pygame.image.load("nb.jpg")
                            video1 = VideoFileClip(r"nb.mp4")
                            listw = ['芭芭拉', '凝光', '班尼特','芭芭拉','凝光']
                            wuqi1 = True
                        if oh:
                            dingguiobject = 'wuqi'
                            dinggui = 0
                            a = 0
                            c = 0
                            d = 0
                            sixingfangwai = 0
                            b1 = 0
                            b2 = 0
                            b3 = 0
                            b4 = 0
                            b5 = 0
                            b6 = 0
                            p = 0
                            oo = 0
                            c1 = 0
                            c2 = 0
                            c3 = 0
                            u = 0
                            po = 0
                            ff = 0
                            d1 = 0
                            d2 = 0
                            d3 = 0
                            d4 = 0
                            d5 = 0
                            d6 = 0
                            d7 = 0
                            d8 = 0
                            d9 = 0
                            d10 = 0
                            m0 = 0
                            m1 = 0
                            m2 = 0
                            m3 = 0
                            m4 = 0
                            m5 = 0
                            m6 = 0
                            m7 = 0
                            m8 = 0
                            m9 = 0
                            m10 = 0
                            m11 = 0
                            m12 = 0
                            m13 = 0
                            m14 = 0
                            m15 = 0
                            m16 = 0
                            m17 = 0
                            m18 = 0
                            m19 = 0
                            m20 = 0
                            m21 = 0
                            m22 = 0
                            m23 = 0
                            m24 = 0
                            m25 = 0
                            m26 = 0
                            m27 = 0
                            m28 = 0
                            m29 = 0
                            m30 = 0
                            m31 = 0
                            m32 = 0
                            m33 = 0
                            m34 = 0
                            m35 = 0
                            m36 = 0
                            m37 = 0
                            m38 = 0
                            m39 = 0
                            wushichou = 0
                            liushichou = 0
                            qishichou = 0
                            bashichou = 0
                            wuxingbaodi = 0
                            chouzhongprize1 = 0
                            chouzhongprize2 = 0
                            linshixingchen = 0
                            linshixinghui = 0
                            xingchen = 0
                            xinghui = 0
                            pr1 = listw[0]
                            pr2 = listw[1]
                            pr3 = listw[2]
                            pr4 = listw[3]
                            pr5 = listw[4]
                            size = weight, height = 1200, 600
                            screen = pygame.display.set_mode(size)
                            pygame.init()
                            screen.fill(bg)
                            tupian =pygame.transform.scale(tupian, (1200, 600))
                            if musicplay:
                                logoimage = screen.blit(tupian, (0, 0))
                                logoimage = screen.blit(musicing2, (1140,60))
                                pygame.display.flip()
                            else:
                                logoimage = screen.blit(tupian, (0, 0))
                                logoimage = screen.blit(musicing1, (1140,60))
                                pygame.display.flip()
                            pygame.display.flip()
                            msgbox('刷新成功（抽奖数据已被重置）',image = 'ooops1.jpg')
                    elif (mouse_x > 40) and (mouse_x < 185) and (mouse_y > 550) and (mouse_y < 600):#历史记录查看---------------------------------------------------------------------
                        size = weight, height = 1200, 600
                        screen = pygame.display.set_mode(size)
                        screen.fill((0, 0, 0))
                        msgboxx1 = ('累计共抽{}发，抽中五星{}发,获得无主的星尘x{},无主的星辉x{}'.format(a, d,xingchen,xinghui))
                        if not wuqi1:
                            msgboxx1535 = ('在五十抽以下出金{}发,50-59出金{}发,60-69出金{}发,70-79出金{}发,保底{}发'.format(d - bashichou - liushichou - qishichou - wuxingbaodi,liushichou,qishichou,bashichou, wuxingbaodi))
                            msgboxx2 = ('歪了{}发，其中天空之刃{}发，天空之琴{}发，天空之傲{}发，天空之卷{}发，天空之脊{}发。'.format(p, b1+b5, b2,b3, b4,b6))
                            msgboxx3 = ('累计共抽中{}{}发,{}{}发,没歪{}发。累计共抽中四星{}发,保底{}发。'.format(prize1, chouzhongprize1, prize2, chouzhongprize2,d-p,po, ff))
                            msgboxx4 = ('其中{}{}发,{}{}发,{}{}发,{}{}发,{}{}发，祭礼剑{}发'.format(pr1, c1,pr2, c2,pr3, c3,pr4, c4,pr5, c5,m1))
                        else:
                            msgboxx1535 = ('在六十抽以下出金{}发,60-69出金{}发,70-79出金{}发,80-89出金{}发,保底{}发'.format(d - liushichou - qishichou - bashichou - wuxingbaodi,liushichou,qishichou, bashichou, wuxingbaodi))
                            msgboxx2 = ('歪了{}发，其中迪卢克{}发，刻晴{}发，七七{}发，莫娜{}发，提纳里{}发，琴{}发。'.format(p, b1, b2,b3, b4, b5,b6))
                            msgboxx3 = ('累计共抽中{}{}发。累计共抽中四星{}发，保底{}发。'.format(prize1, d - p, po, ff))
                            msgboxx4 = ('其中{}{}发,{}{}发,{}{}发,祭礼剑{}发'.format(pr1, c1 +c4,pr2, c2 + c5 ,pr3, c3,m1))
                        msgboxx5 = ('祭礼残章{}发,祭礼弓{}发,祭礼大剑{}发,西风剑{},发西风秘典{}发,西风猎弓{}发'.format(m2,m3, m4,m5, m6,m7))
                        msgboxx6 = ('西风大剑{}发,西风长枪{}发,暗巷闪光{}发,暗巷猎手{}发,暗巷的酒与诗{}发,笛剑{}发'.format(m8,m9,m10,m11,m12,m13))
                        msgboxx7 = ('辰纱之纺锤{},发匣里龙吟{}发,匣里灭辰{}发,绝弦,{}发，弓藏{}发,恶王丸{}发'.format(m14,m15,m16,m17, m18, m19,))
                        msgboxx8 = ('幽夜华尔兹{}发,雨裁{}发,千岩古剑{}发,千岩长枪{}发,昭心{}发,流浪乐章{}发'.format(m20, m21, m22, m23,m24, m25))
                        msgboxx9 = ('芭芭拉{}发,行秋{}发,菲谢尔{}发,云堇{}发,凝光{}发,罗莎莉亚{}发,雷泽{}发'.format(m26, m27, m28, m29, m30, m31,m32))
                        msgboxx10 = ('重云{}发,早柚{},砂糖{}发,班尼特{}发,烟绯{}发,香菱{}发,托马{}发'.format(m33, m34,m35, m36, m37,m38,m39))
                        msgboxx11 = ('累计共抽中三星{}发，其中飞天御剑{}发，飞天大御剑{}发'.format(a - d - po, d1, d2))
                        msgboxx1147 = ('神射手之誓{}发，黑缨枪{}发,以理服人{}发,冷刃{}发'.format(d3, d4,d5, d6))
                        msgboxx1148 = ('黎明神剑{}发，讨龙英杰谭{}发，魔导绪论{}发，沐浴龙血的剑{}发。'.format(d7, d8, d9, d10))
                        backing = ('返回')
                        fonting = pygame.font.Font('hk4e_zh-cn.ttf', 26)
                        font1 = fonting.render(msgboxx1, True, (255,255,0))
                        font1535 = fonting.render(msgboxx1535,True,(255,255,0))
                        font2 = fonting.render(msgboxx2, True, (255,255,0))
                        font3 = fonting.render(msgboxx3, True, (255,255,0))
                        font4 = fonting.render(msgboxx4, True, green)
                        font5 = fonting.render(msgboxx5, True, green)
                        font6 = fonting.render(msgboxx6, True, green)
                        font7 = fonting.render(msgboxx7, True, green)
                        font8 = fonting.render(msgboxx8, True, green)
                        font9 = fonting.render(msgboxx9, True, green)
                        font10 = fonting.render(msgboxx10, True, green)
                        font11 = fonting.render(msgboxx11, True, green)
                        font12 = fonting.render(backing, True, (255, 0, 0))
                        font13 = fonting.render(msgboxx1147, True, green)
                        font14 = fonting.render(msgboxx1148, True, green)
                        screen.blit(font1, (30, 30))
                        screen.blit(font1535, (30, 70))
                        screen.blit(font2, (30, 110))
                        screen.blit(font3, (30, 150))
                        screen.blit(font4, (30, 190))
                        screen.blit(font5, (30, 230))
                        screen.blit(font6, (30, 270))
                        screen.blit(font7, (30, 310))
                        screen.blit(font8, (30, 350))
                        screen.blit(font9, (30, 390))
                        screen.blit(font10, (30, 430))
                        screen.blit(font11, (30, 470))
                        screen.blit(font12, (1130, 30))
                        screen.blit(font13, (30, 510))
                        screen.blit(font14, (30, 550))
                        pygame.display.flip()
                        fhgs = True
                        while fhgs:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    size = weight, height = 1200, 600
                                    screen = pygame.display.set_mode(size)
                                    screen.fill(bg)
                                    logoimage = screen.blit(err, (0, 0))
                                    pygame.display.flip()
                                    sys.exit(0)
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse_x, mouse_y = pygame.mouse.get_pos()
                                    if (mouse_x > 1090) and (mouse_x < 1200) and (mouse_y > 0) and (mouse_y < 100):#退出历史记录查看----------------------------------------
                                        fhgs = False
                                        screen.fill((0, 0, 0))
                                        if musicplay:
                                            logoimage = screen.blit(tupian, (0, 0))
                                            logoimage = screen.blit(musicing2, (1140,60))
                                            pygame.display.flip()
                                        else:
                                            logoimage = screen.blit(tupian, (0, 0))
                                            logoimage = screen.blit(musicing1, (1140,60))
                                            pygame.display.flip()
                    elif (mouse_x > 1126) and (mouse_x < 1200) and (mouse_y > 0) and (mouse_y < 53):#重置-------------------------------------------------------------------------
                        dingguiobject = 'wuqi'
                        dinggui = 0
                        a = 0
                        c = 0
                        d = 0
                        sixingfangwai = 0
                        b1 = 0
                        b2 = 0
                        b3 = 0
                        b4 = 0
                        b5 = 0
                        b6 = 0
                        p = 0
                        oo = 0
                        c1 = 0
                        c2 = 0
                        c3 = 0
                        u = 0
                        po = 0
                        ff = 0
                        d1 = 0
                        d2 = 0
                        d3 = 0
                        d4 = 0
                        d5 = 0
                        d6 = 0
                        d7 = 0
                        d8 = 0
                        d9 = 0
                        d10 = 0
                        m0 = 0
                        m1 = 0
                        m2 = 0
                        m3 = 0
                        m4 = 0
                        m5 = 0
                        m6 = 0
                        m7 = 0
                        m8 = 0
                        m9 = 0
                        m10 = 0
                        m11 = 0
                        m12 = 0
                        m13 = 0
                        m14 = 0
                        m15 = 0
                        m16 = 0
                        m17 = 0
                        m18 = 0
                        m19 = 0
                        m20 = 0
                        m21 = 0
                        m22 = 0
                        m23 = 0
                        m24 = 0
                        m25 = 0
                        m26 = 0
                        m27 = 0
                        m28 = 0
                        m29 = 0
                        m30 = 0
                        m31 = 0
                        m32 = 0
                        m33 = 0
                        m34 = 0
                        m35 = 0
                        m36 = 0
                        m37 = 0
                        m38 = 0
                        m39 = 0
                        pr1 = listw[0]
                        pr2 = listw[1]
                        pr3 = listw[2]
                        pr4 = listw[3]
                        pr5 = listw[4]
                        wushichou = 0
                        liushichou = 0
                        qishichou = 0
                        bashichou = 0
                        wuxingbaodi = 0
                        chouzhongprize1 = 0
                        chouzhongprize2 = 0
                        xingchen = 0
                        xinghui = 0
                        linshixinghui = 0
                        linshixingchen = 0
                        msgbox('重置成功', ok_button='好的',image = 'guobaxiao.gif')
                elif event.type == pygame.KEYDOWN:
                    try:
                        if chr(event.key) == 'h':
                            size = weight, height = 1200, 600
                            screen = pygame.display.set_mode(size)
                            screen.fill((0, 0, 0))
                            msgboxx1 = ('what is new in Genshen 1.1')
                            msgboxx2 = ('初步增加简单的定轨功能')
                            msgboxx3 = ('帮助:')
                            msgboxx4 = ('按左上角可以切换祈愿池，按右上角可以重置祈愿，按左下角对应按键可以观看角色演示和历史记录。')
                            msgboxx5 = ('注：自定义抽奖次数的抽奖结果需要去shell界面查看。点击祈愿后，会有1-2秒延迟，属正常现象')
                            msgboxx6 = ('可使用「神铸定轨」对本期五星UP武器「单手剑·苍古自由之誓」或「法器·四风原典」进行定轨')
                            msgboxx7 = ('一般情况下所有角色或武器均适用基础概率，如触发概率UP，保底等以具体规则为准')
                            msgboxx8 = ('退出此页面后按‘F’键或点击右上角暂停图标播放/暂停音乐,按‘E’键强制刷新当前页面')
                            msgboxx9 = ('退出此页面后按‘R’键播放下一首,按‘T’键播放上一首,按‘O’键调高音量,按‘P’键调低音量')
                            #msgboxxc = ('关于背景音乐详细信息请退出此页面后按‘L’键查询')
                            msgboxxc = ('定轨功能之后会进一步更新')
                            msgboxxa = ('关于祈愿物品公示请退出此页面后按‘M’键查询')
                            msgboxxb = ('关于祈愿内置详细信息请退出此页面后按‘N’键查询')
                            backing = ('返回')
                            fonting = pygame.font.Font('hk4e_zh-cn.ttf', 26)
                            font1 = fonting.render(msgboxx1, True, (255,0,0))
                            font2 = fonting.render(msgboxx2, True, green)
                            font3 = fonting.render(msgboxx3, True, (255,0,0))
                            font4 = fonting.render(msgboxx4, True, green)
                            font5 = fonting.render(msgboxx5, True, green)
                            font6 = fonting.render(msgboxx6, True, green)
                            font7 = fonting.render(msgboxx7, True, green)
                            font8 = fonting.render(msgboxx8, True, green)
                            font9 = fonting.render(msgboxx9, True, green)
                            fontc = fonting.render(msgboxxc, True, (255,0,255))
                            fonta = fonting.render(msgboxxa, True, (255,0,255))
                            fontb = fonting.render(msgboxxb, True, (255,0,255))
                            fontba = fonting.render(backing, True, (255,0,0))
                            screen.blit(font1, (30, 30))
                            screen.blit(font2, (30, 70))
                            screen.blit(font3, (30, 110))
                            screen.blit(font4, (30, 150))
                            screen.blit(font5, (30, 190))
                            screen.blit(font6, (30, 230))
                            screen.blit(font7, (30, 270))
                            screen.blit(font8, (30, 310))
                            screen.blit(font9, (30, 350))
                            screen.blit(fontc, (30, 470))
                            screen.blit(fonta, (30, 510))
                            screen.blit(fontb, (30, 550))
                            screen.blit(fontba, (1130, 30))
                            pygame.display.flip()
                            fhgs = True
                            while fhgs:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        size = weight, height = 1200, 600
                                        screen = pygame.display.set_mode(size)
                                        screen.fill(bg)
                                        logoimage = screen.blit(err, (0, 0))
                                        pygame.display.flip()
                                        sys.exit(0)
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        mouse_x, mouse_y = pygame.mouse.get_pos()
                                        if (mouse_x > 1090) and (mouse_x < 1200) and (mouse_y > 0) and (mouse_y < 100):#退出历史记录查看----------------------------------------
                                            fhgs = False
                                            screen.fill((0, 0, 0))
                                            if musicplay:
                                                logoimage = screen.blit(tupian, (0, 0))
                                                logoimage = screen.blit(musicing2, (1140,60))
                                                pygame.display.flip()
                                            else:
                                                logoimage = screen.blit(tupian, (0, 0))
                                                logoimage = screen.blit(musicing1, (1140,60))
                                                pygame.display.flip()
                        elif chr(event.key) == 'f':
                            if musicplay:
                                pygame.mixer.music.load(musiclist[musicplayer])
                                pygame.mixer.music.play()
                                musicplay = False
                                logoimage = screen.blit(tupian, (0, 0))
                                logoimage = screen.blit(musicing1, (1140,60))
                                pygame.display.flip()
                            else:
                                pygame.mixer.music.stop()
                                musicplay = True
                                logoimage = screen.blit(tupian, (0, 0))
                                logoimage = screen.blit(musicing2, (1140,60))
                                pygame.display.flip()
                        elif chr(event.key) == 'r':
                            if musicplayer == yinyueshuliang:
                                musicplayer = 0
                            else:
                                musicplayer += 1
                            pygame.mixer.music.load(musiclist[musicplayer])
                            pygame.mixer.music.play()
                        elif chr(event.key) == 't':
                            if musicplayer == 0:
                                musicplayer = yinyueshuliang
                            else:
                                musicplayer -= 1
                            pygame.mixer.music.load(musiclist[musicplayer])
                            pygame.mixer.music.play()
                        elif chr(event.key) == 'o':
                            if musicloud >= 1:
                                musicloud = 1
                                msgbox('音量已是最大')
                            else:
                                musicloud +=0.2
                            pygame.mixer.music.set_volume(musicloud)
                        elif chr(event.key) == 'p':
                            if musicloud <= 0:
                                musicloud = 0
                                msgbox('音量已是最小')
                            else:
                                musicloud -= 0.2
                            pygame.mixer.music.set_volume(musicloud)
                        elif chr(event.key) == 'e':
                            if musicplay:
                                logoimage = screen.blit(tupian, (0, 0))
                                logoimage = screen.blit(musicing2, (1140,60))
                                pygame.display.flip()
                            else:
                                logoimage = screen.blit(tupian, (0, 0))
                                logoimage = screen.blit(musicing1, (1140,60))
                                pygame.display.flip()
                        elif chr(event.key) == 'l':
                            size = weight, height = 1200, 600
                            screen = pygame.display.set_mode(size)
                            screen.fill((0, 0, 0))
                            msgboxx1 = ('歌曲列表')
                            msgboxx2 = ('1.镇守之森(Her Legacy·Hanachirusato·Time to say Farewell)')
                            msgboxx4 = ('2.何妄何执(雷电将军)')
                            msgboxx5 = ('3.甘雨(角色演示)')
                            msgboxx6 = ('4.璃月港-昼')
                            msgboxx7 = ('5.飞彩镌流年·海灯节2022')
                            msgboxx8 = ('6.温迪(角色演示)')
                            msgboxx10 = ('7.徐浚皓1')
                            msgboxx11 = ('8.徐浚皓2')
                            backing = ('返回')
                            fonting = pygame.font.Font('hk4e_zh-cn.ttf', 26)
                            font1 = fonting.render(msgboxx1, True, (255,0,255))
                            font2 = fonting.render(msgboxx2, True, green)
                            font4 = fonting.render(msgboxx4, True, green)
                            font5 = fonting.render(msgboxx5, True, green)
                            font6 = fonting.render(msgboxx6, True, green)
                            font7 = fonting.render(msgboxx7, True, green)
                            font8 = fonting.render(msgboxx8, True, green)
                            font9 = fonting.render(msgboxx9, True, green)
                            font10 = fonting.render(msgboxx10, True, green)
                            font11 = fonting.render(msgboxx11, True, green)
                            font12 = fonting.render(backing, True, (255, 0, 0))
                            screen.blit(font1, (30, 30))
                            screen.blit(font2, (30, 70))
                            screen.blit(font4, (30, 110))
                            screen.blit(font5, (30, 150))
                            screen.blit(font6, (30, 190))
                            screen.blit(font7, (30, 230))
                            screen.blit(font8, (30, 270))
                            screen.blit(font9, (30, 310))
                            screen.blit(font10, (30, 350))
                            screen.blit(font11, (30, 390))
                            screen.blit(font12, (1130, 30))
                            pygame.display.flip()
                            fhgs = True
                            while fhgs:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        size = weight, height = 1200, 600
                                        screen = pygame.display.set_mode(size)
                                        screen.fill(bg)
                                        logoimage = screen.blit(err, (0, 0))
                                        pygame.display.flip()
                                        sys.exit(0)
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        mouse_x, mouse_y = pygame.mouse.get_pos()
                                        if (mouse_x > 1090) and (mouse_x < 1200) and (mouse_y > 0) and (mouse_y < 100):
                                            fhgs = False
                                            screen.fill((0, 0, 0))
                                            if musicplay:
                                                logoimage = screen.blit(tupian, (0, 0))
                                                logoimage = screen.blit(musicing2, (1140,60))
                                                pygame.display.flip()
                                            else:
                                                logoimage = screen.blit(tupian, (0, 0))
                                                logoimage = screen.blit(musicing1, (1140,60))
                                                pygame.display.flip()
                        elif chr(event.key) == 'm':
                            size = weight, height = 1200, 600
                            screen = pygame.display.set_mode(size)
                            screen.fill((0, 0, 0))
                            msgboxx1 = ('Available five-star characters(不包括UP的角色)')
                            msgboxx2 = ('迪卢克、刻晴、七七、莫娜、提纳里、琴')
                            msgboxx3 = ('Available five-star weapons(不包括UP的武器)')
                            msgboxx4 = ('天空之刃、天空之琴、天空之傲、天空之卷、天空之脊')
                            msgboxx5 = ('Available four-star objects(不包括UP的角色或武器)')
                            msgboxx6 = ('祭礼剑、祭礼残章、祭礼弓、祭礼大剑、西风剑、西风秘典、西风猎弓、西风大剑、西风长枪、暗巷闪光')
                            msgboxx7 = ('暗巷猎手、暗巷的酒与诗、笛剑、辰纱之纺锤、匣里龙吟、匣里灭辰、绝弦、弓藏、恶王丸、幽夜华尔兹')
                            msgboxx8 = ('雨裁、千岩古剑、千岩长枪、昭心、流浪乐章、芭芭拉、行秋、菲谢尔、云堇、凝光、罗莎莉亚、雷泽')
                            msgboxx9 = ('重云、早柚、砂糖、班尼特、烟绯、香菱。')
                            msgboxx10 = ('Available three-star weapons')
                            msgboxx11 = ('飞天御剑、飞天大御剑、神射手之誓、黑缨枪、以理服人、冷刃、黎明神剑、讨龙英杰谭、魔导绪论、沐')
                            msgboxx12 = ('浴龙血的剑')
                            backing = ('返回')
                            fonting = pygame.font.Font('hk4e_zh-cn.ttf', 26)
                            font1 = fonting.render(msgboxx1, True, (255,0,0))
                            font2 = fonting.render(msgboxx2, True, green)
                            font3 = fonting.render(msgboxx3, True, (255,0,0))
                            font4 = fonting.render(msgboxx4, True, green)
                            font5 = fonting.render(msgboxx5, True, (255,0,0))
                            font6 = fonting.render(msgboxx6, True, green)
                            font7 = fonting.render(msgboxx7, True, green)
                            font8 = fonting.render(msgboxx8, True, green)
                            font9 = fonting.render(msgboxx9, True, green)
                            font10 = fonting.render(msgboxx10, True, (255,0,0))
                            font11 = fonting.render(msgboxx11, True, green)
                            font12 = fonting.render(backing, True, (255, 0, 0))
                            font13 = fonting.render(msgboxx12, True, green)
                            screen.blit(font1, (30, 30))
                            screen.blit(font2, (30, 70))
                            screen.blit(font3, (30, 110))
                            screen.blit(font4, (30, 150))
                            screen.blit(font5, (30, 190))
                            screen.blit(font6, (30, 230))
                            screen.blit(font7, (30, 270))
                            screen.blit(font8, (30, 310))
                            screen.blit(font9, (30, 350))
                            screen.blit(font10, (30, 390))
                            screen.blit(font11, (30, 430))
                            screen.blit(font12, (1130, 30))
                            screen.blit(font13, (30, 470))
                            pygame.display.flip()
                            fhgs = True
                            while fhgs:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        size = weight, height = 1200, 600
                                        screen = pygame.display.set_mode(size)
                                        screen.fill(bg)
                                        logoimage = screen.blit(err, (0, 0))
                                        pygame.display.flip()
                                        sys.exit(0)
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        mouse_x, mouse_y = pygame.mouse.get_pos()
                                        if (mouse_x > 1090) and (mouse_x < 1200) and (mouse_y > 0) and (mouse_y < 100):#退出历史记录查看----------------------------------------
                                            fhgs = False
                                            screen.fill((0, 0, 0))
                                            if musicplay:
                                                logoimage = screen.blit(tupian, (0, 0))
                                                logoimage = screen.blit(musicing2, (1140,60))
                                                pygame.display.flip()
                                            else:
                                                logoimage = screen.blit(tupian, (0, 0))
                                                logoimage = screen.blit(musicing1, (1140,60))
                                                pygame.display.flip()
                        elif chr(event.key) == 'n':
                            size = weight, height = 1200, 600
                            screen = pygame.display.set_mode(size)
                            screen.fill((0, 0, 0))
                            msgbox1 = ('官方公布的祈愿机制')
                            msgboxx1 = ('在活动祈愿中,五星角色祈愿的基础概率为0.6%,综合概率(含保底)为1.6%,五星武器祈愿的基')
                            msgboxx2 = ('础概率为0.7%,综合概率(含保底)为1.85%,最多90次祈愿内必定能通过保底获取5星物品。当祈')
                            msgboxx3 = ('愿获取到五星角色或武器时,有50%的概率为本期UP角色或武器。如果本次祈愿获取的五星角色')
                            msgbox3 = ('或武器非本期UP角色或武器,下次祈愿获取的五星角色必定为本期UP的五星角色或武器。')
                            msgboxx4 = ('在活动祈愿中，四星物品祈愿的基础概率为5.1%(角色武器各占一半)，综合概率(含保底)为13%')
                            msgboxx5 = ('，最多10次祈愿内必定能通过保底获取4星或以上物品，通过保底获取四星物品的概率为99.4%,')
                            msgboxx6 = ('获取五星角色的概率为0.6%。当祈愿获取到四星角色或武器时，有50%的概率为本期UP角色或')
                            msgboxx7 = ('武器。如果本次祈愿获取的四星角色或武器非本期UP角色或武器，下次祈愿获取的四星角色必定')
                            msgboxx8 = ('为本期UP的四星角色或武器。')  #https://www.bilibili.com/video/BV1mb4y1S7Td/?spm_id_from=trigger_reload
                            msgboxx9 = ('获得四星武器时，会同时获得两个无主的星辉作为副产物，获得三星武器时，会同时获得十五个')
                            msgboxx10 = ('无主的星尘作为副产物。第2-7次获得相同的角色时，五星会转化为10个无主的星辉和一个对应')
                            msgboxx11 = ('角色的命星，四星会转化为2个无主的星辉和一个对应角色的命星。第八次及以上获得重复角色')
                            backing = ('返回')
                            backing2 = ('下一页')
                            fonting = pygame.font.Font('hk4e_zh-cn.ttf', 26)
                            font1113 = fonting.render(msgbox1, True, (255,0,0))
                            font1 = fonting.render(msgboxx1, True, green)
                            font2 = fonting.render(msgboxx2, True, green)
                            font3 = fonting.render(msgboxx3, True, green)
                            font31 = fonting.render(msgbox3, True, green)
                            font4 = fonting.render(msgboxx4, True, green)
                            font5 = fonting.render(msgboxx5, True, green)
                            font6 = fonting.render(msgboxx6, True, green)
                            font7 = fonting.render(msgboxx7, True, green)
                            font8 = fonting.render(msgboxx8, True, green)
                            font9 = fonting.render(msgboxx9, True, green)
                            font10 = fonting.render(msgboxx10, True, green)
                            font11 = fonting.render(msgboxx11, True, green)
                            font12 = fonting.render(backing, True, (255, 0, 0))
                            font0 = fonting.render(backing2, True, (255, 0, 0))
                            screen.blit(font1113, (30, 30))
                            screen.blit(font1, (30, 70))
                            screen.blit(font2, (30, 110))
                            screen.blit(font3, (30, 150))
                            screen.blit(font31, (30,190 ))
                            screen.blit(font4, (30,230))
                            screen.blit(font5, (30,270 ))
                            screen.blit(font6, (30,310 ))
                            screen.blit(font7, (30,350 ))
                            screen.blit(font8, (30,390 ))
                            screen.blit(font9, (30, 430))
                            screen.blit(font10, (30, 470))
                            screen.blit(font11, (30, 510))
                            screen.blit(font12, (1130, 30))
                            screen.blit(font0, (1100, 560))
                            pygame.display.flip()
                            linshipanding2 = True
                            while linshipanding2:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        size = weight, height = 1200, 600
                                        screen = pygame.display.set_mode(size)
                                        screen.fill(bg)
                                        logoimage = screen.blit(err, (0, 0))
                                        pygame.display.flip()
                                        sys.exit(0)
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        mouse_x, mouse_y = pygame.mouse.get_pos()
                                        if (mouse_x > 1090) and (mouse_x < 1200) and (mouse_y > 0) and (mouse_y < 100):#退出历史记录查看----------------------------------------
                                            linshipanding2 = False
                                            screen.fill((0, 0, 0))
                                            if musicplay:
                                                logoimage = screen.blit(tupian, (0, 0))
                                                logoimage = screen.blit(musicing2, (1140,60))
                                                pygame.display.flip()
                                            else:
                                                logoimage = screen.blit(tupian, (0, 0))
                                                logoimage = screen.blit(musicing1, (1140,60))
                                                pygame.display.flip()
                                        elif (mouse_x > 1070) and (mouse_x < 1200) and (mouse_y > 500) and (mouse_y < 600):#退出历史记录查看----------------------------------------
                                            linshipanding2 = False
                                            screen.fill((0, 0, 0))
                                            msgboxx12 = ('时，五星将转化为25个无主的星辉，四星会转化为5个无主的星辉')
                                            msgboxx1 = ('官方实质的祈愿机制')
                                            msgboxx2 = ('在角色活动祈愿中,五星0-73发基础概率为0.6%,74-89发基础概率为0.6%+(n-73)*6%,综合')
                                            msgboxx3 = ('概率(含保底)为1.605%,在武器活动祈愿中,五星祈愿1-62的基础概率为0.7%,63-73的基础概率')
                                            msgboxx4 = ('为0.7%+(n-62)*7%,74-79发的基础概率为77.7%+(n-73)*3.5%,综合概率(含保底)为1.878%')
                                            msgboxx5 = ('在角色活动祈愿中四星1-8发基础概率为5.1%,第九发基础概率为56.1%,综合概率(含保底)为')
                                            msgboxx6 = ('13.057%。在武器活动祈愿中,四星1-7发的基础概率为6%,第八发的基础概率为66%,第九发的')
                                            msgboxx7 = ('基础概率为96%,综合概率(含保底)为14.841%。')
                                            backing = ('返回')
                                            pygame.display.flip()
                                            font111 = fonting.render(msgboxx12, True, green)
                                            font1 = fonting.render(msgboxx1, True, (255,0,0))
                                            font2 = fonting.render(msgboxx2, True, green)
                                            font3 = fonting.render(msgboxx3, True, green)
                                            font4 = fonting.render(msgboxx4, True, green)
                                            font5 = fonting.render(msgboxx5, True, green)
                                            font6 = fonting.render(msgboxx6, True, green)
                                            font7 = fonting.render(msgboxx7, True, green)
                                            font12 = fonting.render(backing, True, (255, 0, 0))
                                            screen.blit(font111, (30,30))
                                            screen.blit(font1, (30,70))
                                            screen.blit(font2, (30,110))
                                            screen.blit(font3, (30,150))
                                            screen.blit(font4, (30,190))
                                            screen.blit(font5, (30,230))
                                            screen.blit(font6, (30,270))
                                            screen.blit(font7, (30,310))
                                            screen.blit(font12, (1130, 30))
                                            pygame.display.flip()
                                            linshipanding = True
                                            while linshipanding:
                                                for event in pygame.event.get():
                                                    if event.type == pygame.QUIT:
                                                        size = weight, height = 1200, 600
                                                        screen = pygame.display.set_mode(size)
                                                        screen.fill(bg)
                                                        logoimage = screen.blit(err, (0, 0))
                                                        pygame.display.flip()
                                                        sys.exit(0)
                                                    elif event.type == pygame.MOUSEBUTTONDOWN:
                                                        mouse_x, mouse_y = pygame.mouse.get_pos()
                                                        if (mouse_x > 1090) and (mouse_x < 1200) and (mouse_y > 0) and (mouse_y < 100):
                                                            linshipanding = False
                                                            screen.fill((0, 0, 0))
                                                            if musicplay:
                                                                logoimage = screen.blit(tupian, (0, 0))
                                                                logoimage = screen.blit(musicing2, (1140,60))
                                                                pygame.display.flip()
                                                            else:
                                                                logoimage = screen.blit(tupian, (0, 0))
                                                                logoimage = screen.blit(musicing1, (1140,60))
                                                                pygame.display.flip()
                    except Exception:
                        if musicplay:
                            logoimage = screen.blit(tupian, (0, 0))
                            logoimage = screen.blit(musicing2, (1140,60))
                            pygame.display.flip()
                        else:
                            logoimage = screen.blit(tupian, (0, 0))
                            logoimage = screen.blit(musicing1, (1140,60))
                            pygame.display.flip()
        screen.fill((0, 0, 0))
        if True:
            for itt in range(t4):
                screen.fill((0, 0, 0))
                a += 1
                aa = True
                bb = True
                if wuqi1:
                    if c <= 60:
                        b = 3
                    elif c <= 73:
                        b = 10
                    elif c <= 88:
                        b = 30*(c - 73)
                    else:
                        b = 500
                else:
                    if c <= 50:
                        b = 3
                    elif c <= 63:
                        b = 10
                    elif c <= 73:
                        b = 35*(c - 62)
                    elif c < 79:
                        b = 388 + 17.5 * (c - 73)
                    else:
                        b = 500
                e = random.randint(1, 500)
                if e <= b:
                    xinghui += 10
                    linshixinghui += 10
                    if wuqi1:
                        julibaodi = 89 - c
                    else:
                        julibaodi = 79 - c
                    if julibaodi <= 30 and julibaodi > 20:
                        liushichou += 1
                    elif julibaodi <= 20 and julibaodi > 10:
                        qishichou += 1
                    elif julibaodi <= 10 and julibaodi > 0:
                        bashichou += 1
                    elif julibaodi <=0:
                        wuxingbaodi+=1
                    kq1 = 1
                    d += 1
                    if not wuqi1:
                        if dingguiobject != 'wuqi':
                            if dinggui >= 2:
                                if dingguiobject == 'canggu':
                                    listing.append('{}，距离保底{}发---------------'.format(prize1, julibaodi))
                                    dinggui = 0
                                    dingguiobject = 'wuqi'
                                elif dingguiobject == 'sifeng':
                                    listing.append('{}，距离保底{}发---------------'.format(prize2, julibaodi))
                                    dinggui = 0
                                    dingguiobject = 'wuqi'
                                continue
                    if oo >= 1:
                        wuxingpanding = random.randint(1,2)
                        if wuxingpanding == 1:
                            listing.append('{}，距离保底{}发---------------'.format(prize1, julibaodi))
                            chouzhongprize1 += 1
                            if not wuqi1:
                                if dingguiobject == 'canggu':
                                    dinggui = 0
                                    dingguiobject = 'wuqi'
                                else:
                                    dinggui += 1
                        else:
                            listing.append('{}，距离保底{}发---------------'.format(prize2, julibaodi))
                            chouzhongprize2 += 1
                            if not wuqi1:
                                if dingguiobject == 'sifeng':
                                    dinggui = 0
                                    dingguiobject = 'wuqi'
                                else:
                                    dinggui += 1
                        oo = 0
                    else:
                        if wuqi1:
                            g = random.randint(2, 3)
                        else:
                            g = random.randint(0, 3)
                        if g <= 2:
                            oo += 1
                            if not wuqi1:
                                dinggui += 1
                            f = random.randint(0, 30)
                            p += 1
                            if 89 - c == 0:
                                ee += 1
                            if f <= 4:
                                if wuqi1:
                                    listing.append('迪卢克，距离保底{}发---------------'.format(julibaodi))
                                else:
                                    listing.append('天空之刃，距离保底{}发---------------'.format(julibaodi))
                                b1 += 1
                            elif f <= 9:
                                if wuqi1:
                                    listing.append('刻晴，距离保底{}发---------------'.format(julibaodi))
                                else:
                                    listing.append('天空之琴，距离保底{}发---------------'.format(julibaodi))
                                b2 += 1
                            elif f <= 15:
                                if wuqi1:
                                    listing.append('七七，距离保底{}发---------------'.format(julibaodi))
                                else:
                                    listing.append('天空之傲，距离保底{}发---------------'.format(julibaodi))
                                b3 += 1
                            elif f <= 21:
                                if wuqi1:
                                    listing.append('莫娜，距离保底{}发---------------'.format(julibaodi))
                                else:
                                    listing.append('天空之卷，距离保底{}发---------------'.format(julibaodi))
                                b4 += 1
                            elif f <= 24:
                                if wuqi1:
                                    listing.append('提纳里，距离保底{}发---------------'.format(julibaodi))
                                else:
                                    listing.append('天空之刃，距离保底{}发---------------'.format(julibaodi))
                                b5 += 1
                            else:
                                if wuqi1:
                                    listing.append('琴，距离保底{}发---------------'.format(julibaodi))
                                else:
                                    listing.append('天空之脊，距离保底{}发---------------'.format(julibaodi))
                                b6 += 1
                        else:
                            wuxingpanding = random.randint(1,2)
                            if wuxingpanding == 1:
                                listing.append('{}，距离保底{}发---------------'.format(prize1,julibaodi))
                                chouzhongprize1 += 1
                                if not wuqi1:
                                    if dingguiobject == 'canggu':
                                        dinggui = 0
                                        dingguiobject = 'wuqi'
                                    else:
                                        dinggui += 1
                            else:
                                listing.append('{}，距离保底{}发---------------'.format(prize2,julibaodi))
                                chouzhongprize2 += 1
                                if not wuqi1:
                                    if dingguiobject == 'sifeng':
                                        dinggui = 0
                                        dingguiobject = 'wuqi'
                                    else:
                                        dinggui += 1
                            oo = 0
                    c = 0
                else:
                    c += 1
                    if u < 7:
                        sixing = 17
                    elif u == 7:
                        sixing = 8
                    elif u == 8:
                        sixing = 4
                    elif u == 9:
                        sixing = 1
                        ff += 1
                    v = random.randint(1, sixing)
                    if v == 1:
                        xinghui += 2
                        linshixinghui += 2
                        kq2 = 1
                        po += 1
                        if sixingfangwai >= 1:
                            sixingfangwai = 0
                            k = random.randint(0, 48)
                            if k <= 9:
                                listing.append('{}，距离保底{}发'.format(pr1, 9 - u))
                                c1 += 1
                            elif k <= 18:
                                listing.append('{}，距离保底{}发'.format(pr2, 9 - u))
                                c2 += 1
                            elif k <= 30:
                                listing.append('{}，距离保底{}发'.format(pr3, 9 - u))
                                c3 += 1
                            elif k <= 39:
                                listing.append('{}，距离保底{}发'.format(pr4, 9 - u))
                                c4 += 1
                            else:
                                listing.append('{}，距离保底{}发'.format(pr5, 9 - u))
                                c5 += 1
                        else:
                            kk = random.randint(1, 2)
                            if kk <= 1:
                                sixingfangwai = 0
                                k = random.randint(0, 48)
                                if k <= 9:
                                    listing.append('{}，距离保底{}发'.format(pr1, 9 - u))
                                    c1 += 1
                                elif k <= 18:
                                    listing.append('{}，距离保底{}发'.format(pr2, 9 - u))
                                    c2 += 1
                                elif k <= 30:
                                    listing.append('{}，距离保底{}发'.format(pr3, 9 - u))
                                    c3 += 1
                                elif k <= 39:
                                    listing.append('{}，距离保底{}发'.format(pr4, 9 - u))
                                    c4 += 1
                                else:
                                    listing.append('{}，距离保底{}发'.format(pr5, 9 - u))
                                    c5 += 1
                            else:
                                sixingfangwai += 1
                                mm = random.randint(0, 13)
                                if mm <= 6:
                                    m = random.randint(1,9)
                                    if m == 1:
                                        listing.append('祭礼剑，距离保底{}发'.format(9 - u))
                                        m1 += 1
                                    elif m == 2:
                                        listing.append('祭礼残章，距离保底{}发'.format(9 - u))
                                        m2 += 1
                                    elif m == 3:
                                        listing.append('祭礼弓，距离保底{}发'.format(9 - u))
                                        m3 += 1
                                    elif m == 4:
                                        listing.append('祭礼大剑，距离保底{}发'.format(9 - u))
                                        m4 += 1
                                    elif m == 5:
                                        listing.append('西风剑，距离保底{}发'.format(9 - u))
                                        m5 += 1
                                    elif m == 6:
                                        listing.append('西风秘典，距离保底{}发'.format(9 - u))
                                        m6 += 1
                                    elif m ==7:
                                        listing.append('西风猎弓，距离保底{}发'.format(9 - u))
                                        m7 += 1
                                    elif m == 8:
                                        listing.append('西风大剑，距离保底{}发'.format(9 - u))
                                        m8 += 1
                                    else:
                                        listing.append('西风长枪，距离保底{}发'.format(9 - u))
                                        m9 += 1
                                elif mm <= 10:
                                    m = random.randint(0, 72)
                                    if m <= 5:
                                        listing.append('暗巷闪光，距离保底{}发'.format(9 - u))
                                        m10 += 1
                                    elif m <= 10:
                                        listing.append('暗巷猎手，距离保底{}发'.format(9 - u))
                                        m11 += 1
                                    elif m <= 15:
                                        listing.append('暗巷的酒与诗，距离保底{}发'.format(9 - u))
                                        m12 += 1
                                    elif m <= 20:
                                        listing.append('笛剑，距离保底{}发'.format(9 - u))
                                        m13 += 1
                                    elif m <= 23:
                                        listing.append('辰砂之纺锤，距离保底{}发'.format(9 - u))
                                        m14 += 1
                                    elif m <= 28:
                                        listing.append('匣里龙吟，距离保底{}发'.format(9 - u))
                                        m15 += 1
                                    elif m <= 33:
                                        listing.append('匣里灭辰，距离保底{}发'.format(9 - u))
                                        m16 += 1
                                    elif m <= 38:
                                        listing.append('绝弦，距离保底{}发'.format(9 - u))
                                        m17 += 1
                                    elif m <= 43:
                                        listing.append('弓藏，距离保底{}发'.format(9 - u))
                                        m18 += 1
                                    elif m <= 46:
                                        listing.append('恶王丸，距离保底{}发'.format(9 - u))
                                        m19 += 1
                                    elif m <= 49:
                                        listing.append('幽夜华尔兹，距离保底{}发'.format(9 - u))
                                        m20 += 1
                                    elif m <= 54:
                                        listing.append('雨裁，距离保底{}发'.format(9 - u))
                                        m21 += 1
                                    elif m <= 58:
                                        listing.append('千岩古剑，距离保底{}发'.format(9 - u))
                                        m22 += 1
                                    elif m <= 62:
                                        listing.append('千岩长枪，距离保底{}发'.format(9 - u))
                                        m23 += 1
                                    elif m <= 66:
                                        listing.append('昭心，距离保底{}发'.format(9 - u))
                                        m24 += 1
                                    elif m <= 72:
                                        listing.append('流浪乐章，距离保底{}发'.format(9 - u))
                                        m25 += 1
                                else:
                                    m = random.randint(0, 66)
                                    if m <= 5:
                                        listing.append('芭芭拉，距离保底{}发'.format(9 - u))
                                        m26 += 1
                                    elif m <= 10:
                                        listing.append('行秋，距离保底{}发'.format(9 - u))
                                        m27 += 1
                                    elif m <= 15:
                                        listing.append('菲谢尔，距离保底{}发'.format(9 - u))
                                        m28 += 1
                                    elif m <= 19:
                                        listing.append('云堇，距离保底{}发'.format(9 - u))
                                        m29 += 1
                                    elif m <= 24:
                                        listing.append('凝光，距离保底{}发'.format(9 - u))
                                        m30 += 1
                                    elif m <= 28:
                                        listing.append('罗莎莉亚，距离保底{}发'.format(9 - u))
                                        m31 += 1
                                    elif m <= 33:
                                        listing.append('雷泽，距离保底{}发'.format(9 - u))
                                        m32 += 1
                                    elif m <= 38:
                                        listing.append('重云，距离保底{}发'.format(9 - u))
                                        m33 += 1
                                    elif m <= 42:
                                        listing.append('早柚，距离保底{}发'.format(9 - u))
                                        m34 += 1
                                    elif m <= 46:
                                        listing.append('砂糖，距离保底{}发'.format(9 - u))
                                        m35 += 1
                                    elif m <= 51:
                                        listing.append('班尼特，距离保底{}发'.format(9 - u))
                                        m36 += 1
                                    elif m <= 56:
                                        listing.append('烟绯，距离保底{}发'.format(9 - u))
                                        m37 += 1
                                    elif m <= 61:
                                        listing.append('香菱，距离保底{}发'.format(9 - u))
                                        m38 += 1
                                    else:
                                        listing.append('托马，距离保底{}发'.format(9 - u))
                                        m39 += 1
                        u = 0
                    else:
                        xingchen += 15
                        linshixingchen += 15
                        u += 1
                        hh = random.randint(1, 10)
                        if hh == 1:
                            listing.append('飞天御剑')
                            d1 += 1
                        elif hh == 2:
                            listing.append('飞天大御剑')
                            d2 += 1
                        elif hh == 3:
                            listing.append('神射手之誓')
                            d3 += 1
                        elif hh == 4:
                            listing.append('黑缨枪')
                            d4 += 1
                        elif hh == 5:
                            listing.append('以理服人')
                            d5 += 1
                        elif hh == 6:
                            listing.append('冷刃')
                            d6 += 1
                        elif hh == 7:
                            listing.append('黎明神剑')
                            d7 += 1
                        elif hh == 8:
                            listing.append('讨龙英杰谭')
                            d8 += 1
                        elif hh == 9:
                            listing.append('魔导绪论')
                            d9 += 1
                        else:
                            listing.append('沐浴龙血的剑')
                            d10 += 1
        iyu = False
        if hhhhh == True:
            hh = False
            if kq1 != 0:
                if fff:
                    fff = False
                    clip = VideoFileClip(r'10j.mp4')
                    zipping.preview(clip, eventa=aff)
                if gg:
                    gg = False
                    iyu = True
                    clip = VideoFileClip(r'1j.mp4')
                    zipping.preview(clip, eventa=aff)
            else:
                if kq2 != 0:
                    if fff:
                        clip = VideoFileClip(r'10z.mp4')
                        zipping.preview(clip, eventa=aff)
                    if gg:
                        clip = VideoFileClip(r'1z.mp4')
                        zipping.preview(clip, eventa=aff)
                else:
                    clip = VideoFileClip(r'1l.mp4')
                    zipping.preview(clip, eventa=aff)
        number = 0
        qwerttt = True
        screen.fill((0, 0, 0))
        if gg:
            gg = False
            for i in listing:
                fonting = pygame.font.Font('hk4e_zh-cn.ttf', 100)
                fonting2 = pygame.font.Font('hk4e_zh-cn.ttf', 50)
                lkjd = str(i)
                msgboxx13 =('获得无主的星尘x{},无主的星辉x{}'.format(linshixingchen,linshixinghui))
                font1 = fonting.render(lkjd, True, green)
                font13 = fonting2.render(msgboxx13, True, (255,255,0))
                screen.blit(font1, (30, 30))
                screen.blit(font13, (300, 550))
                pygame.display.flip()
        if oiu:
            screen.fill((0, 0, 0))
            fonting = pygame.font.Font('hk4e_zh-cn.ttf', 100)
            font1 = fonting.render('Loading...', True, (255, 0, 0))
            screen.blit(font1, (350, 250))
            pygame.display.flip()
        if fff:
            number = 0
            fff = False
            for i in listing:
                fonting = pygame.font.Font('hk4e_zh-cn.ttf', 50)
                lkjd = str(i)
                msgboxx13 =('获得无主的星尘x{},无主的星辉x{}'.format(linshixingchen,linshixinghui))
                font1 = fonting.render(lkjd, True, green)
                font13 = fonting.render(msgboxx13, True, (255,255,0))
                screen.blit(font1, (20, 20 + 50 * number))
                screen.blit(font13, (300, 550))
                pygame.display.flip()
                number += 1
        if not oiu:
            while qwerttt:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        qwerttt = False
        for i in listing:  #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
            print(i)
        if kq1 != 0 and not oiu:
            qwerttt = True
            if iyu:
                for i in listing:
                    fonting = pygame.font.Font('hk4e_zh-cn.ttf', 100)
                    fonting2 = pygame.font.Font('hk4e_zh-cn.ttf', 50)
                    lkjd = str(i)
                    msgboxx13 =('获得无主的星尘x{},无主的星辉x{}'.format(linshixingchen,linshixinghui))
                    font1 = fonting.render(lkjd, True, green)
                    font13 = fonting2.render(msgboxx13, True, (255,255,0))
                    screen.blit(font1, (30, 30))
                    screen.blit(font13, (300, 550))
                    pygame.display.flip()
            else:
                number = 0
                for i in listing:
                    fonting = pygame.font.Font('hk4e_zh-cn.ttf', 50)
                    lkjd = str(i)
                    msgboxx13 =('获得无主的星尘x{},无主的星辉x{}'.format(linshixingchen,linshixinghui))
                    font1 = fonting.render(lkjd, True, green)
                    font13 = fonting.render(msgboxx13, True, (255,255,0))
                    screen.blit(font1, (20,20 + 50*number))
                    screen.blit(font13, (300, 550))
                    pygame.display.flip()
                    number += 1
            while qwerttt:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        qwerttt = False
        iyu = False
        listing = []
        kq1 = 0
        kq2 = 0
        linshixingchen = 0
        linshixinghui = 0
        logoimage = screen.blit(tupian, (0, 0))
        if not oiu:
            logoimage = screen.blit(musicing2 , (1140,60))
            musicplay = True
        pygame.display.flip()
        number = 0
        if oiu:
            oiu = False
            while cc:
                msgbox('提示：请前往shell界面查看抽奖结果', ok_button='哦' ,image = 'ooops3.jpg')
                msgbox('提示：点击“历史记录”查看更多结果', ok_button='哦',image = 'ooops5.jpg')
                cc = False
        print('\n' * 2)
#except AttributeError as reason:
except Exception as reason:
    print(reason)
    screen.fill(bg)
    logoimage = screen.blit(err, (0, 0))
    pygame.display.flip()
