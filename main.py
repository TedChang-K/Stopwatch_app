
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import time

class StopwatchApp(App):
    def build(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.running = False

        self.label = Label(text="00:00:00", font_size='48sp')
        self.start_btn = Button(text="Start", on_press=self.start)
        self.stop_btn = Button(text="Stop", on_press=self.stop)
        self.reset_btn = Button(text="Reset", on_press=self.reset)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.label)
        layout.add_widget(self.start_btn)
        layout.add_widget(self.stop_btn)
        layout.add_widget(self.reset_btn)

        Clock.schedule_interval(self.update, 0.01)
        return layout

    def format_time(self, seconds):
        m = int(seconds // 60)
        s = int(seconds % 60)
        hs = int((seconds - int(seconds)) * 100)
        return f"{m:02}:{s:02}:{hs:02}"

    def update(self, dt):
        if self.running:
            current = time.time()
            self.elapsed_time = current - self.start_time
            self.label.text = self.format_time(self.elapsed_time)

    def start(self, instance):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True

    def stop(self, instance):
        if self.running:
            self.running = False
            display = self.format_time(self.elapsed_time)
            self.label.text = display[:-1] + "9"

    def reset(self, instance):
        self.running = False
        self.elapsed_time = 0
        self.label.text = "00:00:00"

if __name__ == '__main__':
    StopwatchApp().run()
