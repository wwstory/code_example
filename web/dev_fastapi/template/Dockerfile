FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

EXPOSE 8000

ENV PROJECT_DIR=/root/proj

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install motor easydict minio python-multipart && \
    pip install pytest httpx requests pytest-asyncio

WORKDIR ${PROJECT_DIR}

# run
RUN mkdir -p ${PROJECT_DIR}; cd ${PROJECT_DIR}
COPY . .

# RUN pytest >> test.log

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
