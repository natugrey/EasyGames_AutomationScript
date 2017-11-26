# encoding=utf-8
import cv2
import aircv as ac
import ImageGrab
import time
import numpy
from getHandle import *
from mouseCtrl import *
import win32api


def grab_screen():
    pos = get_pos(_title)
    bbox = (pos[0]+8, pos[1], pos[2]-8, pos[3]-8)
    img = ImageGrab.grab(bbox)
    mat = cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)
    return mat


def im_find(_img, confidence, _str):
    _imsrc = grab_screen()
    _matchPos = ac.find_template(_imsrc, _img)
    if _matchPos is None:
        pass
    elif _matchPos['confidence'] < confidence:
        #print _str, 'found but not exact, confidence is: ', _matchPos['confidence']
        pass
    elif _matchPos['confidence'] >= confidence:
        print _str, u'被找到! 准确度为: ', _matchPos['confidence']
        return True
    return False


def im_find_click(_img, confidence, _str):
    _imsrc = grab_screen()
    _matchPos = ac.find_template(_imsrc, _img)
    if _matchPos is None:
        pass
    elif _matchPos['confidence'] < confidence:
        #print _str, 'found but not exact, confidence is: ', _matchPos['confidence']
        pass
    elif _matchPos['confidence'] >= confidence:
        print _str, u'被找到并点击了一次 !  准确度为: ', _matchPos['confidence']
        rawposition = get_mouse_point()
        mouse_left_click(get_pos(_title)[0] + _matchPos['result'][0], get_pos(_title)[1] + _matchPos['result'][1])
        mouse_move(rawposition[0], rawposition[1])


_title = '阴阳师-网易游戏'
set_front(_title)
# _three = [[get_pos(_title)[0] + 130, get_pos(_title)[1] + 200],
#           [get_pos(_title)[0] + 130, get_pos(_title)[1] + 370],
#           [get_pos(_title)[0] + 130, get_pos(_title)[1] + 520]]
im_attack = cv2.imread('attack.png')
im_prepare = cv2.imread('prepare.png')
im_continue = cv2.imread('continue.png')
im_tick = cv2.imread('tick.png')
im_invite = cv2.imread('invite.png')
im_confirm = cv2.imread('confirm.png')
im_begin = cv2.imread('begin.png')
im_default = cv2.imread('default.png')
x = 65535
while(1):
    x += 1
    if x > 25:
        x = 0
        print '\n---------------------- ',\
            time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime(time.time())),\
            ' ----------------------'
    if im_find(im_invite, 0.65, u'“邀请”'):
        time.sleep(1)
        continue
        pass
    im_find_click(im_default, 0.99, u'“默认邀请队友”')
    im_find_click(im_begin, 0.99, u'“开始战斗”')
    im_find_click(im_attack, 0.95, u'“进攻”')
    im_find_click(im_prepare, 0.80, u'“准备”')
    im_find_click(im_continue, 0.60, u'“点击屏幕继续”')
    im_find_click(im_tick, 0.99, u'“钩”')
    im_find_click(im_confirm, 0.99, u'“确定”')
    print u'扫描中...'
    time.sleep(0.5)

# ####### find the match position ############
# pos = ac.find_template(imsrc, im_zeroStar)
##############################################