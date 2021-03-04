SHELL := /bin/bash

DOCKER_IMAGE_NAME = explorehsk

# install dependencies
.PHONY: install-dependencies
install-dependencies:
	cp bootstrap_req.txt requirements.txt
	docker build --target basic -t $(DOCKER_IMAGE_NAME):basic .
	docker run --rm $(DOCKER_IMAGE_NAME):basic cat requirements.txt > requirements.txt

.PHONY: install-dependencies-dev
install-dependencies-dev:
	cp bootstrap_req_dev.txt requirements.dev.txt
	docker build --target dev -t $(DOCKER_IMAGE_NAME):dev .
	docker run --rm $(DOCKER_IMAGE_NAME):dev cat requirements.dev.txt > requirements.dev.txt

# this step needs to be ran before serving the backend flask API
# it dumps `data/model.pkl`
.PHONY: build-model
build-model:
	docker build --target builder -t $(DOCKER_IMAGE_NAME):full .
	docker run -v $(shell pwd)/data:/data --rm $(DOCKER_IMAGE_NAME):full bash -c "python -m src.build_model /data"

# this step is to run the backend server
.PHONY: run
run:
	docker build --target basic -t $(DOCKER_IMAGE_NAME):basic .
	docker run -p 5000:5000 --rm $(DOCKER_IMAGE_NAME):basic bash -c "cd app/ && flask run --host=0.0.0.0"