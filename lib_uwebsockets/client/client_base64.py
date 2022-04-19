
import asyncio
from websockets import connect
import cv2 as cv
import numpy as np
import time
import base64


async def hello(uri):
    while True:
        try:
            async with connect(uri) as websocket:
                # await websocket.send("Hello world!")
                while True:
                    r = await websocket.recv()
                    print('server data:', len(r))

                    # r = 'data:image/jpeg;base64,' + str(r, encoding='utf-8')  # error, no exist 'data:image/jpeg;base64,'
                    r = str(r, encoding='utf-8')
                    r = base64.b64decode(r)

                    img = np.asarray(bytearray(r), dtype='uint8')
                    img = cv.imdecode(img, cv.IMREAD_COLOR)

                    # img = np.fromstring(r, np.uint8)
                    # img = cv2.imdecode(img, cv.COLOR_BGR2RGB)
                    cv.imshow('video', img)
                    cv.waitKey(1)

        except:
            print('sleep 1s to retry...')
            time.sleep(1)


asyncio.run(hello("ws://localhost:3000/img"))
