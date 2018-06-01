FROM python:3.6

RUN mkdir /imageprocessing
WORKDIR /imageprocessing
ADD . /imageprocessing/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/imageprocessing/app.py"]
