import qrcode
import os, sys
from os import remove
import time
from picamera import PiCamera
import cv2
from PIL import Image, ImageDraw, ImageEnhance
import datetime
from io import StringIO

def return_print(*message):
        io = StringIO()
        print(*message, file=io, end="")
        return io.getvalue()

for i in range (2) :
        for i in range(1, 7):
                #src = cv2.imread(f'/home/pi/robo/countdown2/{i}.jpg', cv2.IMREAD_COLOR)
        
                #dst = cv2.resize(src, dsize=(720,432), interpolation=cv2.INTER_AREA)

                cv2.namedWindow("Window_name", cv2. WINDOW_NORMAL)
                cv2.setWindowProperty("Window_name", cv2. WND_PROP_FULLSCREEN, cv2. WINDOW_FULLSCREEN)
                cv2.moveWindow("Window_name", x=0, y=0)
                img = cv2.imread(f'/home/pi/robo/countdown2/{i}.jpg', cv2.IMREAD_COLOR)
                #dst = cv2.resize(src, dsize=(720, 432), interpolation=cv2.INTER_AREA)
                cv2.imshow("Window_name", img)
                #cv2.imshow("dst", dst)
                cv2.waitKey(1000)
                time.sleep(0.5)
                cv2.destroyAllWindows()

        os.system("./camera.sh")

path = os.path.normpath("/home/pi/camera")
file_list = os.listdir(path) # path 하위의 모든 파일 및 디렉토리를 리스트로 가져옴
file_list.sort(reverse=True)
size = len(file_list) # 해당 디렉토리의 바로 아래에 있는 파일/디렉토리 개수만 계산

global first, second
new = Image.new("RGBA", (800, 400))

cnt = 0
for filename in file_list:
        img = return_print("/home/pi/camera/"+f"{os.path.splitext(filename)[0]}")
        cnt += 1

        if cnt == 1:
                second = Image.open(f"{img}.jpg")
                new.paste(second, (400,0))
                remove(f"{img}.jpg")
                print("cnt = 1 success!")
        if cnt == 2:
                first = Image.open(f"{img}.jpg")
                new.paste(first, (0,0))
                remove(f"{img}.jpg")
                print("cnt = 2 success!")
        if cnt == 3:
                print("cnt = 3, break!")
                break;
                
now = datetime.datetime.now()
nowDateTime = now.strftime('%Y-%m-%d_%H%M%S')
name = return_print(sys.argv[1])
new.save("/home/pi/cameraHistory/"+f"{name}.png")
new.show()

#qrimg = qrcode.make("
#img = qrcode.make("/home/pi/camera/2023-02-28_162425.png")
#img.save("/home/pi/cameraHistory")
