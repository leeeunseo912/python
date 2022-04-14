# MP3Player
#    데이터: 노래 목록, song, BASE_DIR, current_index
#    기능: 목록, 재생, 다음, 이전, 종료 ---> 메뉴 구성

from pygame import mixer
import eyed3
from file_util import get_file_list
from baseapp import Application
import os

class MP3Player(Application):
  def __init__(self) -> None:
    super().__init__("MP3Player")
    self.DIR_PATH = "c:/temp/music"  # 음악 파일 디렉토리
    self.song_list = []              # 재생 목록
    self.song = None                 # 현재 재생중인 파일
    self.current_index = -1          # 현재 재생 파일의 인덱스

  # 메뉴 구성, create_menu() override
  def create_menu(self):
    self.menu.add_menu('목록', self.print_list )
    self.menu.add_menu('재생', self.play)
    self.menu.add_menu('정지', self.stop)
    self.menu.add_menu('다음', self.play_next)
    self.menu.add_menu('이전', self.play_prev)
    self.menu.add_menu('종료', self.exit)   # 부모 클래스의 exit 메서드

  def init(self):
    super().init()  # 내부에서 create_menu() 호출

    mixer.init()
    self.song_list = get_file_list(self.DIR_PATH, '.mp3')

  def print_list(self):
    for ix, song in enumerate(self.song_list):
      print(f'{ix}] {song}')
    
    print()

  def print_tag(self, file_path):
    try:
      s = eyed3.load(file_path)
      print(f'가수: {s.tag.artist}')
      print(f'앨범: {s.tag.album}')
      print(f'곡명: {s.tag.title}')
    except:
      print(file_path)

  def play_music(self, index):
    # 이전에 재생중이면 먼저 정지
    if self.song:
      self.song.stop()

    song_path = os.path.join(self.DIR_PATH, self.song_list[index])
    self.print_tag(song_path)
    self.song = mixer.Sound(song_path)  # mixer 모듈안의 정의된 Sound 클래스의 인스턴스를 생성, __init__(self, filepath)
    self.song.play()

  def play(self):
    self.current_index = int(input('선곡: '))
    self.play_music(self.current_index)

  def stop(self):
      if self.song:
        self.song.stop()
      self.song = None

  def play_next(self):
    self.current_index += 1
    if self.current_index == len(self.song_list):
      self.current_index = 0

    # curent_index =  (curent_index+1) % len(song_list)
    self.play_music(self.current_index)

  def play_prev(self):
    self.current_index -= 1
    if self.current_index == -1:  # 첫번째 곡에서 이전이면, 마지막 곡으로
      self.current_index = len(self.song_list) - 1
    
    self.play_music(self.current_index)


def main():
  app = MP3Player()
  app.run()

main()  

