FROM python:3.9
ADD . /home/Account/
WORKDIR /home/Account
RUN pip install -r requirements.txt
EXPOSE 8000
#RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000
