FROM python:3.9
WORKDIR /app
COPY app.py .
RUN python3 -m venv venv
RUN venv/bin/pip install flask psutil
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
CMD ["python", "app.py"]
