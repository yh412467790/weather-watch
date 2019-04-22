FROM python:3.7

ADD weather_check.py /
ADD config.ini /

RUN pip3 install requests

ENTRYPOINT [ "python3.7", "weather_check.py" ]
CMD [""]
