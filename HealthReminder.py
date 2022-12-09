from pygame import mixer
from datetime import datetime
from time import time
# ---------function for play music------
def play_music(filename , stopper):
    print(f"enter {stopper} for stop alarm")
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

# ---------function for take log------
def log_now(msg):
    with open("healthReminder.txt" ,"a") as f:
        f.write(f"{msg} at datetime {datetime.now()} \n")
if __name__ == '__main__':
    print("Hey welcome i am your health trainer alarm . I remind you for drink water and pysical exercise\n")

    waterdrink =float(input("enter time in minutes for drink water"))
    exercise =  float(input("enter time in minutes for physical exercise"))
    init_water = time()
    init_ex = time()
    while True:
        if time()-init_water > waterdrink*60:
            print("its time to drink water")
            play_music("alarm.mp3","drunk")
            init_water=time()
            log_now("Drink water")
        if time()-init_ex > exercise*60:
            print("its time to do exercise")
            play_music("alarm.mp3","exdone")
            init_ex=time()
            log_now("Exercise done")




















