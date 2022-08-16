import unittest
import main

class TestMain(unittest.TestCase):
    def tick():
        global stime, time_elapsed
        if not mixer.music.get_busy():
            stime = None
        elapsed = time.time() - stime if stime else 0
        mins, secs = divmod(elapsed, 60)
        tick_label.config(text=f"{mins:02.0f}:{secs:06.3f}")
        tick_label.after(100, tick)
