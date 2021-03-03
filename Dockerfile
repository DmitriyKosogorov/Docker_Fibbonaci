FROM python:3
WORKDIR /usr/src/app
COPY fib.py /usr/src/app
CMD ["python3", "fib.py"]
