import os, random
from pygame import mixer, time

# mp3 재생 설정
freq = 16000    # frequency
bitsize = -16   # signed 16 bit. support 8,-8,16,-16s
channels = 1    # 1 is mono, 2 is stereo
buffer = 2048   # number of samples (experiment to get right sound)


# 음악이 저장된 경로 지정
music_list_dir = "./music"
angry_music_list_dir = music_list_dir + "/angry_music/"
disgust_music_list_dir = music_list_dir + "/disgust_music/"
fear_music_list_dir = music_list_dir + "/fear_music/"
happy_music_list_dir = music_list_dir + "/happy_music/"
neutral_music_list_dir = music_list_dir + "/neutral_music/"
sad_music_list_dir = music_list_dir + "/sad_music/"
surprised_music_list_dir = music_list_dir + "/surprised_music/"

# 감정별 음악 리스트
angry_music_list = os.listdir(angry_music_list_dir)
disgust_music_list = os.listdir(disgust_music_list_dir)
fear_music_list = os.listdir(fear_music_list_dir)
happy_music_list = os.listdir(happy_music_list_dir)
neutral_music_list = os.listdir(neutral_music_list_dir)
sad_music_list = os.listdir(sad_music_list_dir)
surprised_music_list = os.listdir(surprised_music_list_dir)

# 감정 리스트
emotion_list = ['ANGRY', 'DISGUST', 'DISGUSTED', 'CONFUSED', 'FEAR', 'HAPPY', 'NEUTRAL', 'SAD', 'SURPRISE', 'SURPRISED', 'CALM']


# 감정에 따른 무작위 음악 선택
def select_music(emotion):
    if emotion == "ANGRY":
        selected_music = random.choice(angry_music_list)
        print(angry_music_list_dir + selected_music)
        return angry_music_list_dir + selected_music
    elif emotion == "DISGUST" or emotion == "DISGUSTED":
        selected_music = random.choice(disgust_music_list)
        print(disgust_music_list_dir + selected_music)
        return disgust_music_list_dir + selected_music
    elif emotion == "FEAR" or emotion == "CONFUSED":
        selected_music = random.choice(fear_music_list)
        print(fear_music_list_dir + selected_music)
        return fear_music_list_dir + selected_music
    elif emotion == "HAPPY":
        selected_music = random.choice(happy_music_list)
        print(happy_music_list_dir + selected_music)
        return happy_music_list_dir + selected_music
    elif emotion == "NEUTRAL" or emotion == "CALM":
        selected_music = random.choice(neutral_music_list)
        print(neutral_music_list_dir + selected_music)
        return neutral_music_list_dir + selected_music
    elif emotion == "SAD":
        selected_music = random.choice(sad_music_list)
        print(sad_music_list_dir + selected_music)
        return sad_music_list_dir + selected_music
    elif emotion == "SURPRISE" or emotion == "SURPRISED":
        selected_music = random.choice(surprised_music_list)
        print(surprised_music_list_dir + selected_music)
        return surprised_music_list_dir + selected_music
    else:
        print("Invalid argument. Parameter Name: emotion")


def music_init():
    # pygame.mixer.init(freq, bitsize, channels, buffer)
    mixer.init(freq, bitsize, channels, buffer)


def music_start(emotion):
    if emotion in emotion_list:
        selected_music = select_music(emotion)

        mixer.init(freq, bitsize, channels, buffer)
        mixer.music.load(selected_music)
        mixer.music.play(0)

        clock = time.Clock()

        while mixer.music.get_busy():  # 음악 재생
            clock.tick(60)

            if mixer.music.get_pos() > 10000:  # 10초 지나면 음악이 멈춤
                break

        mixer.quit()


def emergency_siren():
    mixer.init(freq, bitsize, channels, buffer)
    mixer.music.load("./emergency_siren/Emergency_Siren.mp3")
    mixer.music.play(0)

    clock = time.Clock()

    while mixer.music.get_busy():  # 사이렌 울림
        clock.tick(60)

        if mixer.music.get_pos() > 10000:  # 10초 지나면 사이렌 종료
            break

    mixer.quit()
