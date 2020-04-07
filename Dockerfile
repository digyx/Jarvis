FROM python:latest
ADD *.py ./
RUN pip install -r requirements.txt
CMD ["python", "./main.py", "--docker"]