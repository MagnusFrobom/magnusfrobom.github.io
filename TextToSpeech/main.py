import pyttsx3
import pyperclip
import pygame
import tkinter as tk
import time


class VoiceWeaver:
    
    def __init__(self):
        # Initialize the audio mixer
        pygame.mixer.init()
        self.mixer_state = 0  # music play state

        # Initialize the timer variables
        self.start_time = 0.0
        self.is_paused = False
        self.time_elapsed = 0.0
        self.current_time = 0.0

        # Read the text from the clipboard
        clip_text = pyperclip.paste()
        self.split_text_string = str(clip_text.split())

        # Initialize the text-to-speech engine
        self.engine = pyttsx3.init()
        self.voice_rate = int()
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', self.voice_rate)
        volume = self.engine.getProperty('volume')
        self.engine.setProperty('volume', 1.0)

        # Set up the GUI
        self.root = tk.Tk()

        # Text window
        self.text = tk.Text(width=65, height=20, font="arial 10")
        self.text.pack()
        self.text.insert(tk.END, clip_text)

        # Play/pause/resume button
        self.play_pause_button = tk.Button(
            self.root, text='Play', width=16, bg='green', fg='black', command=self.play_music)
        self.play_pause_button.pack(side=tk.TOP)

        # Stop button
        self.stop_button = tk.Button(
            self.root, text="Stop/Reset", command=self.stop)
        self.stop_button.pack()

        # Bind the space bar to the play_music function
        self.root.bind('<space>', lambda event: self.play_music())

        # Bind the 's' key to the stop function
        self.root.bind('<s>', lambda event: self.stop())

    def set_speech_rate(self, r):
        self.voice_rate = r

    def play_music(self):
        if self.mixer_state == 0:  # Audio not started
            outfile = "temp.wav"
            self.engine.save_to_file(self.text.get('1.0', tk.END), outfile)
            self.engine.runAndWait()
            pygame.mixer.music.load(outfile)
            pygame.mixer.music.play()
            self.start_time = time.time()
            self.play_pause_button.configure(text="Pause", bg='red')
            self.is_paused = False
            self.mixer_state = 1
            return

        if self.mixer_state == 1:  # Audio playing
            pygame.mixer.music.pause()
            self.start_time = time.time()
            self.is_paused = True
            self.play_pause_button.configure(text="Resume", bg='blue')
        else:  # music paused
            pygame.mixer.music.unpause()
            self.start_time = time.time()
            self.is_paused = False
            self.play_pause_button.configure(text="Pause", bg='red')
        self.mixer_state = 3 - self.mixer_state  # swap pause state

    def stop(self):
        pygame.mixer.music.stop()
        self.mixer_state = 0
        self.is_paused = True
        self.play_pause_button.configure(text="Play", bg='green')


def main():
    player = VoiceWeaver()
    tk.mainloop()


if __name__ == "__main__":
    main()
