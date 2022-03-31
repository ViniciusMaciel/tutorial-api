FROM python:3.8-alpine
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./src/api.py /app/api.py
ENTRYPOINT [ "python" ]
CMD ["api.py" ]