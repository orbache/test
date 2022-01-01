FROM python:latest
LABEL create_by="Evyatar Orbach"
WORKDIR /home
COPY requirements.txt ./
COPY conPs.py .
COPY templates ./templates
RUN pip install --no-cache-dir --upgrade pip && \
	pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python","conPs.py"]