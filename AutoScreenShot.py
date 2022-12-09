from PIL import Image , ImageGrab
import speech_recognition as sr
def TakeScreenshot():
    image=ImageGrab.grab()
    image.show()
if __name__ == '__main__':
      TakeScreenshot()

