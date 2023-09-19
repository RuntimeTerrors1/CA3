FROM python
ENV USERNAME=runtimeterrorss1 
RUN mkdir -p /home/ca3
COPY . /home/ca3
EXPOSE 5000
WORKDIR /home/ca3
RUN pip install -r requirements.txt
CMD ["python3","app.py"]
