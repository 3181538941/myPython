#!/usr/bin/env python
# -*- coding: utf-8 -*-
from naoqi import ALProxy
tts=ALProxy("ALTextToSpeech","192.168.43.120",9559)

'''
tts.setLanguage("English")
tts.say("hello")
'''

tts.setLanguage("Chinese")


'''
tts.say("打南边来了一个嘛,手里提着五斤鳎蚂,打北边来了一个哑巴,腰里别着一个喇叭")
tts.say("提搂鳎蚂的喇嘛要拿鳎蚂去换别着喇叭的哑巴的喇叭,别着喇叭的哑巴不愿意拿喇叭去换提搂鳎蚂的喇嘛的鳎蚂")
tts.say("粉红墙上画凤凰，凤凰画在粉红墙。")
tts.say(" 红凤凰、粉凤凰，红粉凤凰、花凤凰。")
tts.say("红凤凰,黄凤凰,红粉凤凰,粉红凤凰,花粉花凤凰。")
'''