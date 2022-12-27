FROM python:3.10.7

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*



WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

expose 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]