import time as Time

log_text = ""
number = 0

def register_ui(MainUi):
    global ui
    ui = MainUi

def log(string, time=True, line=True, error=False):
    global log_text, number

    if error:
        log_text += "<font color=#FF0000>"

    if time:
        t = Time.localtime(Time.time())
        log_text += "%d [%s:%s:%s] " % (number, str(t[3]).zfill(2), str(t[4]).zfill(2), str(t[5]).zfill(2))
        number += 1


    log_text += string

    if line:
        log_text += "<br>"

    if error:
        log_text += "</font>"

    ui.Log(log_text)