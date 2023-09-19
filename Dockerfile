FROM python:3.11
ENV USERNAME=runtimeterrorss1 
RUN mkdir -p /home/dockerdemo
COPY . /home/dockerdemo
EXPOSE 5000
WORKDIR /home/dockerdemo
RUN pip install -r requirements.txt
CMD ["python3","app.py"]
