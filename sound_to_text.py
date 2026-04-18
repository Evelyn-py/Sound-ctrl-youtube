import speech_recognition as sr
import pyaudio
import datetime
from answer import Answer
import jieba
import parse_movement
import sys
import movement

class SoundRecognition:
    def __init__(self):
        self.answer = Answer()
        self.display_setting = movement.DisplaySetting()
        self.name = ['小马', '马', '小', '老公', '宝贝']
        self.self_intro = ['名字', '全名']
        self.morning = ['早安', 'morning', '早上好', '早']
        self.night = ['晚安', '晚上', '睡了', '睡觉', 'night', 'good night']
        self.comp_movie = ['电脑追剧模式', '电脑追剧', '追剧', '追剧模式']
        self.close = ['close', '拜拜', '再见', '关闭', 'bye']
        self.eat = ['吃饭', '吃']
        self.louder = ['声量调大', '大声', '调大声量']
        self.softer = ['声量调小', '小声', '调小声量']
        self.sajiao = ['撒娇']
        self.browsing_mode = ['browse', 'browsing', '浏览模式']
        self.slide_down = ['滑下', '拉下']
        self.slide_up = ['滑上', '拉上']
        self.dict_path = r"C:\Users\Asus\PycharmProjects\pythonProject\SoundControl\sound_to_text_dict.txt"

    def sound_to_text(self, callback):
        """
        1. record
        2. transfer the record into text
        :return: recognize_text
        """
        # obtain from the microphone
        r = sr.Recognizer()

        with sr.Microphone(chunk_size=5000) as source:
            print('和小马说说话叭 ')
            audio = r.listen(source, phrase_time_limit=2)

            # recognize speech using google
            try:
                recognize = r.recognize_google(audio, language='zh')
                print('小马认为你说: ' + recognize)
            except sr.UnknownValueError:
                print('小马不明白')
                recognize = 'Nothing'
            except sr.RequestError as e:
                print('小马出现错误: {}'.format(e))
                recognize = 'Nothing'
            finally:
                recognize = str(recognize)  .lower()
                callback(recognize)

    def recognize_text(self, text):
        """
        search key text for execute different movement
        :param text: return text from recognize using Google
        :return:sound_to_text_next
        """

        jieba.load_userdict(self.dict_path)
        if text is not None:
            text_jieba = jieba.cut(text, cut_all=False)
            for text in text_jieba:
                print(text)
                self.if_clause(text)
                self.if_common(text)

        return self.sound_to_text(self.recognize_text)

    def name_start(self, text: str):
        """
        call name to start whole process
        :param text:
        :return:sound_to_text_next
        """
        jieba.load_userdict(self.dict_path)

        if text is not None:
            text_jieba = jieba.cut(text, cut_all=True, use_paddle=True)
            for text in text_jieba:
                print(text)
                self.answer.start_name()
                return self.sound_to_text(self.recognize_text)


    def if_clause(self, text):
        # self introduction
        if text in self.self_intro:
            self.answer.self_intro()

        # morning
        if text in self.morning:
            self.answer.morning()

        # good night
        if text in self.night:
            self.answer.night()

        # computer movie mode
        if text in self.comp_movie:
            print('已开启电脑追剧模式')
            self.answer.speak_from_text('已开启电脑追剧模式')
            return parse_movement.CompMovie().recognize_text(None)

        # eat
        if text in self.eat:
            self.answer.eat()

        # close
        if text in self.close:
            print('拜拜')
            self.answer.close()
            sys.exit()

        # 撒娇
        if text in self.sajiao:
            self.answer.sajiao()

    def if_common(self, text):
        # louder
        if text in self.louder:
            self.display_setting.louder()
        # softer
        if text in self.softer:
            self.display_setting.softer()

        # slide_up
        if text in self.slide_up:
            self.display_setting.slide_up()

        # slide_down
        if text in self.slide_down:
            self.display_setting.slide_down()


    def run(self):
        self.sound_to_text(self.name_start)


if __name__ == '__main__':
    SoundRecognition().run()
