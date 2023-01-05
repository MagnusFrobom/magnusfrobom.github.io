from threading import Timer
import time
from tkinter import *
import pyttsx3 as psx3
import pyperclip as pc
from pygame import mixer


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



# Text window
text = Text(width=65, height=20, font="arial 10")
text.pack()

# Inserts the text from the computer CTRL-C clipboard.
text.insert(END, clip_text)

# Tkinter buttons

ppu_button = Button(root, text='Play', width=16, bg='green', fg='black', command=play_music)
ppu_button.pack(side=TOP)



stop_button = Button(root, text="Stop/Reset", command=stop)
stop_button.pack()

# Tkinter Taskbar
root.wm_state('iconic')
root.iconify()

# Binds space to Play/Pause/Resume button
root.bind('<space>', lambda event: play_music())

root.bind('<s>', lambda event: stop())


mainloop()
