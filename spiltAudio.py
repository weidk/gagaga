from pydub import AudioSegment
import os, re

wav = AudioSegment.from_wav('RNC001.WAV')# 打开mp3文件
for i in range(0,90):
    wav[i*60 * 1000:(i+1)*60 * 1000].export('part'+str(i)+'.wav', format="wav")  # 切割前17.5秒并覆盖保存