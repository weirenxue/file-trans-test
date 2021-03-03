import os
from shutil import copyfile
import time

whereAmI = os.path.dirname(__file__)
dummyFolder = os.path.join(whereAmI, 'dummy')
nasDummyFolder = r'your/destination'

def showConvertedElapsed(seconds):
    second = 1
    minute = 60 * second
    hour = 60 * minute
    day = 24 * hour

    天 = int(seconds // day)
    seconds %= day
    時 = int(seconds // hour)
    seconds %= hour
    分 = int(seconds // minute)
    seconds %= minute
    秒 = round(seconds, 3)
    
    print(f"{天} 天 {時} 小時 {分} 分 {秒} 秒")

t = time.time()
for file in os.listdir(dummyFolder):
    try:
        copyfile(os.path.join(dummyFolder, file), os.path.join(nasDummyFolder, file))
    except:
        pass
elapsed = time.time() - t
showConvertedElapsed(elapsed)
