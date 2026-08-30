import pynput

print("pynput is working!")

#--------------------------------Detect Keyboard Print-------------------------------

from pynput import keyboard

def on_press(key):
    print("Pressed:", key)

listener = keyboard.Listener(on_press=on_press)

listener.start()
listener.join()


#--------------------------detect a specific key -------------------
def on_press(key):
    
    if key == keyboard.Key.space:
        print("Space pressed")
       
#Some special Keys 
"""keyboard.Key.space
keyboard.Key.enter
keyboard.Key.esc
keyboard.Key.shift
keyboard.Key.ctrl
keyboard.Key.alt
keyboard.Key.tab
keyboard.Key.backspace
    """
#Normal keys ------------ a,b,c,d,1
#special keys --------------- space,enter,esc

#---------------------------------example---------------------
def on_press(key):
    
    try:
        print("Character:", key.char)

    except AttributeError:
        print("Special key:", key)
        
        
        
        
        
        
        
        






#-----------------------------------stop the listener--------------------------
from pynput import keyboard

def on_press(key):

    print("Pressed:", key)

    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    
    




