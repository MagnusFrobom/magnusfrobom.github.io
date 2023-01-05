from PIL import Image, ImageDraw
import pystray as pst


# Tray icon
icon = pst.Icon(
    'Text2Speech',
    icon=)

def create_image(width, height, color1, color2):
    image = Image.new('RGB', (64, 64), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle((width // 2, 0, width, height // 2),
                 fill=color2)
    dc.rectangle((0, height // 2, width // 2, height),
                 fill=color2)
    return image


def minimize_to_tray():
    icon.run()



def tick():
    global stime, time_elapsed, current_time
    if not mixer.music.get_busy():
       stime = False
    elapsed = time.time()-stime if stime else 0
    mins, secs = divmod(elapsed, 60)
    tick_label.config(text=f"{mins:02.0f}:{secs:06.3f}")
    tick_label.after(100, tick)


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




# Skip Backwards
def backwards():
    global stime, time_elapsed
    if stime:
        time_elapsed = time.time() - stime
        delta = min(time_elapsed, 5)
        mixer.music.rewind()
        mixer.music.set_pos(time_elapsed-delta)
        stime += delta  # adjust the "play start time" after backwards


# Skip Forward ->
def forwards():
    global stime, time_elapsed
    if stime:
        time_elapsed = time.time() + stime
        delta = max(time_elapsed, 5)
        mixer.music.rewind()
        mixer.music.set_pos(time_elapsed+delta)
        stime += delta  # adjust the "play start time" after backwards


min_tray = Button(root, text='Minimize to tray', width=10,
                  height=5, command=minimize_to_tray)
min_tray.pack(side=TOP)

tick_label = Label(root, font="arial 12")
tick_label.pack()


backwards_button = Button(root, text="<-", width=15, height=3, command=backwards)
backwards_button.pack(side=LEFT)


forwards_button = Button(root, text="->", width=15, height=3, command=forwards)
forwards_button.pack(side=RIGHT)



voice_rate = Scale(root, from_=0, to=200, tickinterval=10, orient=HORIZONTAL, command=speech_rate)
voice_rate.pack()



root.bind('<Left>', lambda event: backwards())

root.bind('<Right>', lambda event: forwards())

