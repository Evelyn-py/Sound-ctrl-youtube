import playsound
import random
import gtts
import os
import pyttsx3

class Answer:
    def __init__(self):
        self.playsound = playsound.playsound
        self.gtts = gtts.gTTS


    def random_sound(self, path):
        path = random.choice(path)
        try:
            self.playsound(path)
        except playsound.PlaysoundException:
            try:
                self.playsound(path)
            except playsound.PlaysoundException:
                self.playsound(path)

    def speak_from_text(self, text: str):
        path = os.getcwd() + r'\SpeakContainer' + r'\{}.mp3'.format(text[:5])
        try:
            os.open(path, os.O_RDONLY)
        except FileNotFoundError:
            self.gtts(text, lang='zh-CN').save(path)
        finally:
            try:
                self.playsound(path)
            except Exception:
                self.playsound(path)
            finally:
                os.remove(path)

    def start_name(self):
        path = [r"C:\Users\Asus\PycharmProjects\pythonProject\SoundControl\AnswerSound\什么呀.mp3",
                r"C:\Users\Asus\PycharmProjects\pythonProject\SoundControl\AnswerSound\你在干嘛.mp3"]
        self.random_sound(path)

    def self_intro(self):
        path = [r"C:\Users\Asus\PycharmProjects\pythonProject\SoundControl\AnswerSound\大家好我是.mp3",
                r"C:\Users\Asus\PycharmProjects\pythonProject\SoundControl\AnswerSound\心情不错的马嘉祺.mp3"]
        self.random_sound(path)

    def morning(self):
        path = [r"C:\Users\Asus\PycharmProjects\pythonProject\SoundControl\AnswerSound\昨晚有做梦吗（早安）.mp3",
                r"C:\Users\Asus\PycharmProjects\pythonProject\SoundControl\AnswerSound\早安该起床了美好的一天.mp3",
                r"C:\Users\Asus\PycharmProjects\pythonProject\SoundControl\AnswerSound\早安.mp3",
                r"C:\Users\Asus\PycharmProjects\pythonProject\SoundControl\AnswerSound\快起来吧.mp3"]
        self.random_sound(path)

    def night(self):
        path = [r"C:\Users\Asus\PycharmProjects\pythonProject\SoundControl\AnswerSound\晚安.mp3",
                r"C:\Users\Asus\PycharmProjects\pythonProject\SoundControl\AnswerSound\还不睡吗说完这句晚安.mp3",
                r"C:\Users\Asus\PycharmProjects\pythonProject\SoundControl\AnswerSound\早点休息.mp3"]
        self.random_sound(path)

    def eat(self):
        path = [r"C:\Users\Asus\PycharmProjects\pythonProject\SoundControl\AnswerSound\刚刚吃了.mp3"]
        self.random_sound(path)

    def close(self):
        path = [r"C:\Users\Asus\PycharmProjects\pythonProject\SoundControl\AnswerSound\拜拜.mp3"]
        self.random_sound(path)

    def sajiao(self):
        path = [r"C:\Users\Asus\PycharmProjects\pythonProject\SoundControl\AnswerSound\咩咩咩（撒娇）.mp3",
                r"C:\Users\Asus\PycharmProjects\pythonProject\SoundControl\AnswerSound\哎呀呀呀.mp3"]
        self.random_sound(path)
