from time import sleep
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__)) # 예를들어 부모 디렉토리를 만든다면 parent_dir = os.path.join(current_dir, '..') 이렇게도 가능
sys.path.append(current_dir)
from enums import FREQUANCY
import cobot

def disconnectngRB5():
    cobot.MoveITPL_Clear()
    cobot.MotionHalt()
    cobot.DisConnectToCB()

def mainRB5():
    count = 0
    print("[RB5 main...]")
    cobot.ToCB('10.0.2.7')
    cobot.CobotInit()
    cobot.SetProgramMode(cobot.PG_MODE.REAL)
    cobot.MoveL(x=123.76, y=-448.94, z=304.20, rx=-139.6, ry=22.8, rz=67.3, spd=-1, acc=-1)
    sleep(0.5)
    cobot.MoveL(x=123.76, y=-448.94, z=403.26, rx=-139.6, ry=22.8, rz=67.3, spd=-1, acc=-1)
    sleep(0.5)
    cobot.MoveL(x=123.76, y=-448.94, z=304.20, rx=-139.6, ry=22.8, rz=67.3, spd=-1, acc=-1)
    sleep(0.5)
    cobot.MoveL(x=123.76, y=-448.94, z=403.26, rx=-139.6, ry=22.8, rz=67.3, spd=-1, acc=-1)
    sleep(0.5)
    cobot.MoveL(x=123.76, y=-448.94, z=304.20, rx=-139.6, ry=22.8, rz=67.3, spd=-1, acc=-1)
    sleep(2.5)

    disconnectngRB5()


    # while(count <= 5):
    #     count += 1/FREQUANCY
    #     print("RB5...", count)
    #     sleep(1/FREQUANCY)
