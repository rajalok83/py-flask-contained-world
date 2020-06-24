FROM python:3
RUN pip install flask
COPY . /app
WORKDIR /app
RUN chown -R nobody /app & chmod -R +x /app
USER 99
ENTRYPOINT ["python"]
CMD ["flask-api.py"]
