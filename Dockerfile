FROM python:3.10.5

WORKDIR /app
COPY . /app


RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "model/RestAPI.py"]