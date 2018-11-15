import json
import requests
import time
import hashlib
import base64



URL = "http://api.xfyun.cn/v1/service/v1/tts"
AUE = "mp3"
APP_ID = "5be3e765"
API_KEY = "f23eb491399049defc19281f5a317844"

def getHeader():
        Param = {
            "auf": "audio/L16;rate=16000",  # 音频采样率
            "aue": "lame",  # 音频编码，raw(生成wav)或lame(生成mp3)
            "voice_name": "xiaoyan",
            "speed": "50",  # 语速[0,100]
            "volume": "77",  # 音量[0,100]
            "pitch": "50",  # 音高[0,100]
            "engine_type": "aisound"  # 引擎类型。aisound（普通效果），intp65（中文），intp65_en（英文）
        }
        # 配置参数编码为base64字符串，过程：字典→明文字符串→utf8编码→base64(bytes)→base64字符串
        Param_str = json.dumps(Param)  # 得到明文字符串
        Param_utf8 = Param_str.encode('utf8')  # 得到utf8编码(bytes类型)
        Param_b64 = base64.b64encode(Param_utf8)  # 得到base64编码(bytes类型)
        Param_b64str = Param_b64.decode('utf8')  # 得到base64字符串

        # 构造HTTP请求的头部
        time_now = str(int(time.time()))
        checksum = (API_KEY + time_now + Param_b64str).encode('utf8')
        checksum_md5 = hashlib.md5(checksum).hexdigest()
        header = {
            "X-Appid": APP_ID,
            "X-CurTime": time_now,
            "X-Param": Param_b64str,
            "X-CheckSum": checksum_md5
        }
        return header

def getBody(text):
        data = {'text':text}
        return data

def writeFile(file, content):
    with open(file, 'wb') as f:
        f.write(content)
    f.close()

def SaveAudio(content,fileName):
    r = requests.post(URL, headers=getHeader(), data=getBody(content))
    contentType = r.headers['Content-Type']
    if contentType == "audio/mpeg":
        sid = r.headers['sid']
        if AUE == "raw":
            writeFile(fileName + ".wav", r.content)
        else:
            writeFile(fileName + ".mp3", r.content)
        print("success, name = " + fileName)
    else:
        print(r.text)

content = "1 8国开1 0 还有10分钟就要投标了，朱天启，朱天启，请注意投标时间"
SaveAudio(content)