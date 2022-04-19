# 介绍

demo实现利用`uWebSockets`库发送opencv采集的摄像头图像。

由于`uWebSockets`没有提供`CMakeLists.txt`，使用cmake配置比较麻烦，故采用`Makefile`配置项目。

## Server

### 依赖

```sh
apt install libopencv-dev
```

### server code

以下代码重命名为`demo.cpp`，执行`make test`重新编译：

- `demo.cpp`: （与`demo-out-base64.cpp`相同）
- `demo-out-base64.cpp`: opencv采集摄像头图像，编码为`base64`的二进制数据发送websocket。
- `demo-out-bytes.cpp`: opencv采集摄像头图像，以二进制图像数据发送websocket。
- `test_camera.cpp`: 测试opencv采集摄像头数据。
- `test_char_0.cpp`: 测试`char*`以`\0`结束，导致强转为`string_view`类型只发送一部分图像数据的问题。
- `test_opencv_uws.cpp`: 分别测试`opencv`与`uWebSockets`库是否正常能使用。（`image_paths`变量的图片可以是任意图片，需要自行添加到对应位置）
- `test_send_images.cpp`: 测试`opencv`读取图片，`uWebSockets`循环每3秒发送一次图片数据。（`image_paths`变量的图片可以是任意图片，需要自行添加到对应位置，图片过大，接收可能存在问题，可能是接收buff过小。）

### Run

```sh
make test
```

## Client

### client code

以下代码用于接收server发送的websocket数据（需要与对应的server代码配套使用）：

- `client.py`: python接收二进制图片数据，转为图像并显示。（与server代码的`demo-out-bytes.cpp`配套使用）（由于二进制图像数据只存储了图像数据，没有图像的尺寸，需要提前设置转换的图像分辨率。）
- `client_base64.py`: python接收base64编码的二进制数据，解码并显示图像。（与server代码的`demo-out-base64.cpp`配套使用）
- `client.html`: 网页接收base64编码的二进制数据，解码并显示图像。（与server代码的`demo-out-base64.cpp`配套使用）

### Run

```sh
# 使用`demo-out-base64.cpp`作为服务时
python3 client_base64.py
# 或 使用`demo-out-bytes.cpp`作为服务时
python3 client.py
# 或 使用`demo-out-base64.cpp`作为服务时
# 直接打开 client.html 页面
```

## Ref

- https://github.com/uNetworking/uWebSockets

