SHELL := /bin/bash

DOCKER_IMAGE_NAME = danci-explorer

# install dependencies
.PHONY: install-dependencies
install-dependencies:
	cp bootstrap.req.txt requirements.txt
	docker build --target python-basic -t $(DOCKER_IMAGE_NAME) .
	docker run --rm $(DOCKER_IMAGE_NAME) cat requirements.txt > requirements.txt

.PHONY: simple-serve
simple-serve:
	docker build --target python-basic -t $(DOCKER_IMAGE_NAME) .
	docker run -p 8000:8000 --rm $(DOCKER_IMAGE_NAME) bash -c "cd app/ && python -m http.server"

.PHONY: run
run:
	docker build --target builder -t $(DOCKER_IMAGE_NAME):full .
	docker run -p 5000:5000 --rm $(DOCKER_IMAGE_NAME):full bash -c "cd app/ && flask run --host=0.0.0.0"