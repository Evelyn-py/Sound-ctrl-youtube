import speech_recognition as sr
import jieba
from movement import MovieMovement, DisplaySetting
from answer import Answer
import sound_to_text


class CompMovie(sound_to_text.SoundRecognition):
    def __init__(self):
        super(CompMovie, self).__init__()
        self.dict_path = r"C:\Users\Asus\PycharmProjects\pythonProject\SoundControl\movement_dict.txt"
        self.answer = Answer()
        # for comp_movie mode
        self.movie_movement = MovieMovement()
        self.movie_forward = ['快进', 'forward', 'skip', '前进']
        self.movie_backward = ['倒退', 'backward', 'back']
        self.movie_pause = ['stop', 'pause', '暂停', '停', '继续']
        self.movie_close = ['恢复设置', '关闭']
        self.full_screen = ['放大', 'full screen', '满屏']
        self.exit_full_screen = ['缩小', 'exit full screen', 'escape']
        self.next = ['下一个', 'next']

    def recognize_text(self, text):
        super(CompMovie, self).recognize_text(text)

    def if_clause(self, text):
        super(CompMovie, self).if_common(text)

        # pause
        if text in self.movie_pause:
            self.movie_movement.pause()

        # forward
        if text in self.movie_forward:
            self.movie_movement.forward()

        # backward
        if text in self.movie_backward:
            self.movie_movement.backward()

        # full screen
        if text in self.full_screen:
            self.movie_movement.full_screen()

        # exit full screen
        if text in self.exit_full_screen:
            self.movie_movement.exit_full_screen()

        # next
        if text in self.next:
            self.movie_movement.next()

        # close
        if text in self.movie_close:
            print('已关闭电脑追剧模式')
            self.answer.speak_from_text('已关闭电脑追剧模式')
            return sound_to_text.SoundRecognition().sound_to_text(sound_to_text.SoundRecognition().recognize_text(None))




