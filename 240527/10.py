from pydub import AudioSegment
import uuid
import os
from tkinter import *
window = Tk()

monitor_height = window.winfo_screenheight()
monitor_width = window.winfo_screenwidth()
x_height = 640
y_width = 640
window.resizable(False, False)

window.geometry(f"{x_height}x{y_width}")


def convert(flac_file, mp3_file):

    # Load the FLAC file
    audio = AudioSegment.from_file(flac_file, format=input("codec : "))
    # Export the audio to MP3
    audio.export(mp3_file, format="mp3")



def go_convert():
    print("button active")
# 사용 예시
input_str = input("문자열을 입력하세요: ")
modified_str = input_str.replace("\\", "/")
my_variable = modified_str
print("변경된 문자열:", my_variable)




mp3_file = f"{str(uuid.uuid4())}audio.mp3"
convert(my_variable, mp3_file)



convert_btn = Button(window,command=go_convert)
convert_btn.pack()

window.mainloop()