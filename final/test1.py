import os, sys
import time
from picamera import PiCamera
import cv2
from PIL import Image, ImageEnhance
from datetime import datetime, timezone

for i in range (2) :
        for i in range(5, 0, -1):
                src = cv2.imread(f'/home/pi/robo/icon/{i}.jpg', cv2.IMREAD_COLOR)
        
                dst = cv2.resize(src, dsize=(720,432), interpolation=cv2.INTER_AREA)

                i = "test"
                cv2.moveWindow(i,-100, -100)
                cv2.imshow("dst", dst)
                cv2.waitKey(1000)
                time.sleep(0.5)
                cv2.destroyAllWindows()

        os.system("./camera.sh")

path = "/home/pi/camera"
file_list = os.listdir(path) # path 하위의 모든 파일 및 디렉토리를 리스트로 가져옴
size = len(file_list) # 해당 디렉토리의 바로 아래에 있는 파일/디렉토리 개수만 계산

for i in file_list[-1:-3:-1]:
        global first, second

        if i == -1:
                first = i
        if i == -2 :
                second = i


DATE = datetime.now()
new = Image.new("RGBA", (800, 480))
new.paste(first, (0,0))
new.paste(second, (400,0))

new.show()
