FROM python:3.8-alpine
ADD . /
RUN pip install -r requirements.txt
RUN chmod 777 ./run_tests.sh
CMD ["sh", "./run_tests.sh"]