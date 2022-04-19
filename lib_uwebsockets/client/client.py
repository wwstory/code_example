
import asyncio
from websockets import connect
import cv2 as cv
import numpy as np
import time


async def hello(uri):
    while True:
        try:
            async with connect(uri) as websocket:
                # await websocket.send("Hello world!")
                while True:
                    r = await websocket.recv()
                    print('server data:', len(r))

                    img = np.fromstring(r, np.uint8).reshape(480, 640, 3)   # 480*640*3是接收的图像尺寸
                    cv.imshow('video', img)
                    cv.waitKey(1)

        except:
            print('sleep 1s to retry...')
            time.sleep(1)


asyncio.run(hello("ws://localhost:3000/img"))
