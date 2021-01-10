SHELL := /bin/bash

DOCKER_IMAGE_NAME = my-docker-image

# install dependencies
.PHONY: install-dependencies
install-dependencies:
	cp bootstrap.req.txt requirements.txt
	docker build --target python-basic -t $(DOCKER_IMAGE_NAME) .
	docker run --rm $(DOCKER_IMAGE_NAME) cat requirements.txt > requirements.txt
