from threading import Timer
import time
from tkinter import *
import pyttsx3 as psx3
import pyperclip as pc
from pygame import mixer
import pystray as pst
from PIL import Image, ImageDraw


def create_image(width, height, color1, color2):
    image = Image.new('RGB', (64, 64), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle((width // 2, 0, width, height // 2),
                 fill=color2)
    dc.rectangle((0, height // 2, width // 2, height),
                 fill=color2)
    return image


# Tray icon
icon = pst.Icon(
    'Text2Speech',
    icon=create_image(64, 64, 'black', 'white'))

# PyGame Mixer
mixer.init()
mix_state = 0  # music play state

# Tick timer values
stime = 0.0
is_paused = False
time_elapsed = 0.0
current_time = 0.0

# Text saved in clipboard (Auto-saves Ctrl-C on computer)
clip_text = pc.paste()
split_text_string = str(clip_text.split())

# TextToSpeech settings
voice_rate = int()

engine = psx3.init()  # Text to speech Audio Engine
rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', voice_rate)  # setting up new voice rate

volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

# Tkinter GUI
root = Tk()


def minimize_to_tray():
    icon.run()


class RenewTimer:

    def __int__(self, timeout, callback):
        self.timer = Timer(timeout, callback)

        self.start_time = None
        self.cancel_time = None

        # Create new timer on resume
        self.timeout = timeout
        self.callback = callback

    def cancel(self):
        self.timer.cancel()

    def start(self):
        self.start_time = time.time()
        self.timer.start()

    def pause(self):
        self.cancel_time = time.time()
        self.timer.cancel()
        return self.get_remaining_time()

    def resume(self):
            self.timeout = self.get_remaining_time()
            self.timer = Timer(self.timeout, self.callback)
            self.start_time = time.time()
            self.timer.start()

    def get_remaining_time(self) -> object:
        if self.start_time is None or self.cancel_time is None:
            return self.timeout
        return self.timeout - (self.cancel_time - self.start_time)


'''
def tick():
    global stime, time_elapsed, current_time
    if not mixer.music.get_busy():
       stime = False
    elapsed = time.time()-stime if stime else 0
    mins, secs = divmod(elapsed, 60)
    tick_label.config(text=f"{mins:02.0f}:{secs:06.3f}")
    tick_label.after(100, tick)

'''


# Set the rate of speech
def speech_rate(r):
    global voice_rate
    voice_rate = r


def play_music():
    global mix_state, stime, is_paused, time_elapsed
    if mix_state == 0:  # Audio not started
        outfile = "temp.wav"
        engine.save_to_file(text.get('1.0', END), outfile)
        engine.runAndWait()
        mixer.music.load(outfile)
        mixer.music.play()
        stime = time.time()
        ppu_button.configure(text="Pause", bg='red')
        is_paused = False
        mix_state = 1
        return

    if mix_state == 1:  # Audio playing
        mixer.music.pause()
        stime = time.time()
        is_paused = True
        ppu_button.configure(text="Resume", bg='blue')
    else:  # music paused
        mixer.music.unpause()
        stime = time.time()
        is_paused = False
        ppu_button.configure(text="Pause", bg='red')
    mix_state = 3 - mix_state  # swap pause state


# Stop playback and reset from start
def stop():
    global mix_state, stime, is_paused
    mixer.music.stop()
    mix_state = 0
    is_paused = True
    ppu_button.configure(text="Play", bg='green')


'''
# Skip Backwards
def backwards():
    global stime, time_elapsed
    if stime:
        time_elapsed = time.time() - stime
        delta = min(time_elapsed, 5)
        mixer.music.rewind()
        mixer.music.set_pos(time_elapsed-delta)
        stime += delta  # adjust the "play start time" after backwards
'''
'''
# Skip Forward ->
def forwards():
    global stime, time_elapsed
    if stime:
        time_elapsed = time.time() + stime
        delta = max(time_elapsed, 5)
        mixer.music.rewind()
        mixer.music.set_pos(time_elapsed+delta)
        stime += delta  # adjust the "play start time" after backwards
'''

# Text window
text = Text(width=65, height=20, font="arial 10")
text.pack()

# Inserts the text from the computer CTRL-C clipboard.
text.insert(END, clip_text)

# Tkinter buttons
'''
backwards_button = Button(root, text="<-", width=15, height=3, command=backwards)
backwards_button.pack(side=LEFT)'''

ppu_button = Button(root, text='Play', width=16, bg='green', fg='black', command=play_music)
ppu_button.pack(side=TOP)

min_tray = Button(root, text='Minimize to tray', width=10, height=5, command=minimize_to_tray)
min_tray.pack(side=TOP)
'''
forwards_button = Button(root, text="->", width=15, height=3, command=forwards)
forwards_button.pack(side=RIGHT)
'''

'''
voice_rate = Scale(root, from_=0, to=200, tickinterval=10, orient=HORIZONTAL, command=speech_rate)
voice_rate.pack()
'''
tick_label = Label(root, font="arial 12")
tick_label.pack()

stop_button = Button(root, text="Stop/Reset", command=stop)
stop_button.pack()

# Tkinter Taskbar
root.wm_state('iconic')
root.iconify()

# Binds space to Play/Pause/Resume button
root.bind('<space>', lambda event: play_music())

root.bind('<s>', lambda event: stop())

'''
root.bind('<Left>', lambda event: backwards())

root.bind('<Right>', lambda event: forwards())
'''

mainloop()
