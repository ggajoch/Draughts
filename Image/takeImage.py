from threading import Timer
import time
import cv2
from MainApp.logger import log
import MainApp.conf as conf
import socket
socket.setdefaulttimeout(2)

request = False
timerStop = False
success = False
def get_img():
    global request
    request = True
    while request:
        time.sleep(0.1)
    if success:
        img = cv2.imread("shot.jpg")
        return img
    else:
        return None

def take_photo():
    import MainApp.conf as Conf
    import urllib

    global success

    log("Connecting... ",line=False)

    try:
        urllib.urlretrieve("http://" + str(Conf.get('IP')) + ":8080/shot.jpg", "shot.jpg")
    except Exception as ex:
        success = False
        log("Cannot connect!" + str(ex), error=True,time=False)
        return False
    else:
        log("OK",False)
        success = True
        return True

    #os.system(r"wget --tries 1 --timeout 3 http://" + str(conf.get('IP')) + ":8080/shot.jpg -O shot.jpg --quiet")


timer = Timer(0,0)

def check_for_request():  # periodically checking for new request from other threads
    global request
    if request:
        take_photo()
        request = False
    global timer
    if not timerStop:
        timer = Timer(0.1, check_for_request)
        timer.start()
check_for_request()

def timer_stop():
    global timerStop, timer
    timerStop = True
    timer.cancel()