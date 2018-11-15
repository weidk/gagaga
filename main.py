from heads import *

# 读取今日投标信息
def QueryTBInfo():
    InfoDf = pd.read_sql("select * from openquery(TEST1,'select * from VTY_TBCLIENT_BASEINFO')",Engine)
    return InfoDf

# 叫喇叭
def GaGaGa1(x):
    seconds = (x['投标时间'] - datetime.datetime.now()).seconds / 60
    if seconds>=9 and seconds<=10:
        name = ''
        for n in range(len(x.BONDNAME[0:6])):
            name = name+ x.BONDNAME[n]+' '
        sentence = name +" 还有10分钟将结束投标，"+x.NAME+"，"+x.NAME+"，请注意投标时间。"
        print(sentence)
        result = client.synthesis(sentence, 'zh', 4, {
            'vol': 5,
            'per': 3,
        })

        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open('voice/'+x.BONDNAME+'.mp3', 'wb') as f:
                f.write(result)
        playsound('voice/'+x.BONDNAME+'.mp3')

def GaGaGa(x):
    seconds = (x['投标时间'] - datetime.datetime.now()).seconds / 60
    if seconds>=9 and seconds<=10:
        name = ''
        for n in range(len(x.BONDNAME[0:6])):
            name = name+ x.BONDNAME[n]+' '
        sentence = name +" 还有10分钟将结束投标，"+x.NAME+"，"+x.NAME+"，请注意投标时间。"
        print(sentence)
        SaveAudio(sentence,'voice/'+x.BONDNAME)
        playsound('voice/'+x.BONDNAME+'.mp3')
        SaveAudio(sentence,'voice/180211')
        # playsound('voice/180210.mp3')


if __name__ == '__main__':
    while True:
        try:
            if datetime.datetime.now().hour>9 and datetime.datetime.now().hour<17:
                InfoDf = QueryTBInfo()
                if InfoDf.shape[0]>0:
                    Rst = InfoDf.apply(GaGaGa,axis=1)
            time.sleep(40)
        except:
            time.sleep(40)
            pass
