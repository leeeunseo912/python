import os
import sys
import eyed3
from pygame import mixer
from file_util import get_file_list

DIR_PATH = "c:/temp/music"
song_list = []
song = None
current_index = -1

def init():
    global song_list
    mixer.init()
    song_list = get_file_list(DIR_PATH,'.mp3')

    print(song_list)

def print_list():
    for ix, song in enumerate(song_list):
        print(f'{ix}] {song}')

    print()

#선곡해서 재생하기
def play():
    global current_index, song
    current_index = int(input('선곡: '))

    #이전에 재생중이면 먼저 정지

    play_music(current_index)


def stop():
    global song
    if song:
        song.stop()
    song = None
   

def play_prev():
    global song, current_index
    current_index -= 1

    if current_index == -1:
        current_index = len(song_list) - 1
    
    play_music(current_index)


def play_next():
    global song, current_index
    current_index += 1
    
    if current_index == len(song_list):
        current_index = 0
    # current_index = (current_index + 1) % len(song_list)

    play_music(current_index)

def exit():
    sys.exit(0)

def print_tag(file_path):
    try:       
        s = eyed3.load(file_path)
        print(f'가수 : {s.tag.artist}')
        print(f'앨범 : {s.tag.album}')
        print(f'곡명 : {s.tag.title}')
    except:
        print(file_path)


def play_music(index):
    global song
    if song:
        song.stop()

    song_path = os.path.join(DIR_PATH,song_list[index])
    print_tag(song_path)
    print(f'곡명: {index}] {song_list[index]}')
    song = mixer.Sound(song_path)
    song.play()


def print_menu():
    print("-"*40)
    print("1. 목록\t2. 재생\t3. 정지\t4. 이전\t5. 다음\t6. 종료")
    print("-"*40)



def main():
    init()
    while True:
        print_menu()
        
        menu = int(input("선택> "))

        if menu == 1:
            print_list()

        elif menu == 2:
            play()

        elif menu == 3:
            stop()

        elif menu == 4:
            play_prev()

        elif menu == 5:
            play_next()

        elif menu == 6:
            exit()

main()