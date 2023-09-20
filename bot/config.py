

from decouple import config

try:
    APP_ID = config(" ", default=12278858, cast=int)
    API_HASH = config(" ", default="ce109d0baed40d7da8a762be8737da4f")
    BOT_TOKEN = config(" ", default="6680969743:AAHpx2FWxrJDDBZTasyyUk05h7a0zG6aeMc")
    OWNER= 5591954930
    DEV = 1966867320
    ffmpegcode = ["-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By AnshuSharma (https://github.com/Anshusharma75/TG-videoCompress)' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
    THUMB = config(" ", default="https://graph.org/file/ad7cf597e889acb726c14.jpg")
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit(1)
