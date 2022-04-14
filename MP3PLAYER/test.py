from pygame import mixer

def main():

    song_path = "c:/Temp/music/After_You.mp3"
    song_path2 = "c:/temp/music/Winner_Winner_Funky_Chicken_Dinner.mp3"
    mixer.init()
    song = mixer.Sound(song_path)
    song.play()
    input("정지하려면 엔터")
    song.stop()

    song = mixer.Sound(song_path2)
    song.play()
    input("정지하려면 엔터")
    song.stop()
main()
