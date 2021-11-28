# coding=utf-8
from naoqi import ALProxy
# robot_ip="192.168.43.120"    #nao的ip实时地址
# robot_port=9559             #端口号，一般都是9559
import math
import time

robotip = "192.168.43.89"
port = 9559
motionPrx = ALProxy("ALMotion", robotip, port)
postureProxy = ALProxy("ALRobotPosture", robotip, port)
tts = ALProxy("ALTextToSpeech", robotip, port)
config = [
    ["MaxStepX", 0.04],
    ["MaxStepY", 0.02],
    ["StepHeight", 0.02],
    ["MaxStepFrequency", 0.3]
]

motionPrx.wakeUp()  # 让机器人醒来
postureProxy.goToPosture("StandInit", 0.5)
tts.say("go straight")
motionPrx.moveTo(0.5, 0.0, 0.0, config)  # 让机器人行走
time.sleep(1)
motionPrx.moveTo(0.0, 0.0, math.pi / 2, config)  # 让机器人转90度
time.sleep(2)
motionPrx.moveTo(0.2, 0.0, 0.0, config)
time.sleep(1)
motionPrx.moveTo(0.0, 0.0, math.pi / 2, config)
tts.say("go straight")
motionPrx.moveTo(0.5, 0.0, 0.0, config)
motionPrx.rest()  # 让机器人休眠

tts = ALProxy("ALTextToSpeech", robot_ip, robot_port)
# ALTextToSpeech为NAOqi Audio下的一个说话模块
motion = ALProxy("ALMotion", robot_ip, robot_port)
# ALMotion为机器人移动的模块
'''
tts.loadVoicePreference("NaoOfficialVoiceEnglish")#加载声音参数集
tts.setParameter("doubleVoice",1)        #改变基频之间的比例，改变了声音
tts.setVoice("Kenny22Enhanced")          #设置为Kenny的声音，但是设置失败
tts.setParameter("speed",200)            #改变机器人说话速度
tts.resetSpeed ()                        #回到默认速度值
tts.setParameter("doubleVoiceLevel",0.5) #改变第二语音和第一个体积之间的比例
tts.setParameter("doubleVoiceTimeShift",0.1)#第二个声音和第一个之间的时移
tts.setParameter("pitchShift",1.1)       #改变机器人说话音高
'''
tts.setLanguage("Chinese")  # 改变机器人说话的语言为中文
# tts.say("\\vct=150\\Hello my friends")  #改变机器人说话的语调
# tts.say("\\rspd=50\\hello my friends")  #改变机器人说话速度
tts.say("你好，我是nao")  # 机器人具体说话输出语句

motion.moveInit()
# motion.post.moveTO(0.5, 0, 0)      #蹲下一次
# id = motion.post.moveTo(0.5, 0, 0) #向前走
# motion.wait(id, 0)                  #wait方法