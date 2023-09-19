FROM python:3
ENV USERNAME runtimeterrorss1 
RUN mkdir -p /home/ca3
WORKDIR /home/ca3
COPY . /home/ca3
EXPOSE 5000

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask
CMD ["python","app.py"]
