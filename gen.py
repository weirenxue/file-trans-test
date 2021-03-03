import os 
import random

B  = 1
KB = 1024 * B
MB = 1024 * KB
GB = 1024 * MB
TB = 1024 * GB

TARGET_SIZE = 1 * TB

MAX_SIZE = 5 * MB
MIN_SIZE = 1 * B

accumulation = 0

while accumulation < TARGET_SIZE:
    with open('dummy/' + str(accumulation), 'wb') as outfile:
        dummySize = random.randint(MIN_SIZE, MAX_SIZE)
        accumulation += dummySize
        outfile.write(os.urandom(dummySize))
