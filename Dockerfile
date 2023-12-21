FROM python:3.8

WORKDIR /root

COPY projeto/ /root/projeto/

COPY venv/ /root/venv/

COPY requirements.txt /root/

RUN python -m venv venv

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "projeto/manage.py", "runserver", "0.0.0.0:8000"]
