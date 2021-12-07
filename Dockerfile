FROM python:3

WORKDIR /hexagonal_arch

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .