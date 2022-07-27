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

# Text saved in clipboard (Auto-saves Ctrl-C on computer)
clip_text = pc.paste()
text_string = str(clip_text)

# TextToSpeech Engine
engine = psx3.init()

# Tkinter GUI
root = Tk()


def tick():
    global stime, time_elapsed
    if not mixer.music.get_busy():
        stime = None
    elapsed = time.time()-stime if stime else 0
    mins, secs = divmod(elapsed, 60)
    tick_label.config(text=f"{mins:02.0f}:{secs:06.3f}")
    tick_label.after(100, tick)


def play_music():
    global mix_state, stime, is_paused, time_elapsed
    if mix_state == 0:  # music not started
        outfile = "temp.wav"
        engine.save_to_file(text.get('1.0', END), outfile)
        engine.runAndWait()
        mixer.music.load(outfile)
        mixer.music.play()
        stime = time.time()
        time_elapsed = stime
        ppu_button.configure(text="Pause", bg='red')
        is_paused = False
        mix_state = 1
        return

    if mix_state == 1:  # music playing
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


def stop():
    global mix_state, stime, is_paused
    mixer.music.stop()
    mix_state = 0
    is_paused = True


def backwards():
    global stime, time_elapsed
    if stime:
        time_elapsed = time.time() - stime
        delta = min(time_elapsed, 5)
        mixer.music.rewind()
        mixer.music.set_pos(time_elapsed-delta)
        stime += delta  # adjust the "play start time" after backwards


def unpause():
    mixer.music.unpause()


text = Text(width=65, height=20, font="consolas 14")
text.pack()

text.insert(END, text_string)

# Tkinter buttons
ppu_button = Button(root, text='Play', width=16, bg='green', fg='black', command=play_music)
ppu_button.pack(side=TOP)

tick_label = Label(root, font="Consolas 12")
tick_label.pack()

backwards_button = Button(root, text="<-", command=backwards)
backwards_button.pack()

stop_button = Button(root, text="Stop", command=stop)
stop_button.pack()


# Binds space to Play/Pause/Resume button
root.bind('<space>', lambda event: play_music())

tick()

mainloop()
