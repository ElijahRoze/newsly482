FROM python:3.12.8

RUN mkdir /server
COPY . /server
WORKDIR /server
RUN pip install "fastapi[standard]" pymongo feedparser nltk requests
RUN python /server/install.py
EXPOSE 8000
CMD ["fastapi", "dev", "main.py"]