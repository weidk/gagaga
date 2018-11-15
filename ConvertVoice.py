from aip import AipSpeech

APP_ID = '14625149'
API_KEY = 'uC4H3U9VbYGtwsWXP48ErmmL'
SECRET_KEY = 'j22h9OGcWcKWDzbXX5kG0zx5i8hv2MCO'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
result = client.asr(get_file_content('part3.wav'), 'wav', 16000, {'dev_pid': 1536})