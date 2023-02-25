import os, sys
import time
from picamera import PiCamera
import cv2
from PIL import Image, ImageEnhance
from datetime import datetime, timezone

path = "/home/pi/camera"
file_list = os.listdir(path) # path 하위의 모든 파일 및 디렉토리를 리스트로 가져옴
size = len(file_list) # 해당 디렉토리의 바로 아래에 있는 파일/디렉토리 개수만 계산

global first, second
new = Image.new("RGBA", (800, 480))

DATE = datetime.now()


file_names = os.listdir(path)

for filename in file_names:
        for i in range(2):
                img = os.path.splitext(filename)[0]
                if i == 0:
                        first = Image.open(f"{img}")
                        new.paste(first, (0,0))
                if i == 1:
                        second = Image.open(f"{img}")
                        new.paste(second, (0,0))
        break;

new.show()
