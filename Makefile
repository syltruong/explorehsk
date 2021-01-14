SHELL := /bin/bash

DOCKER_IMAGE_NAME = my-docker-image

# install dependencies
.PHONY: install-dependencies
install-dependencies:
	cp bootstrap.req.txt requirements.dev.txt
	docker build --target python-basic -t $(DOCKER_IMAGE_NAME) .
	docker run --rm $(DOCKER_IMAGE_NAME) cat requirements.dev.txt > requirements.dev.txt

.PHONY: simple-serve
simple-serve:
	docker build --target python-basic -t $(DOCKER_IMAGE_NAME) .
	docker run -p 8000:8000 --rm $(DOCKER_IMAGE_NAME) bash -c "cd app/ && python -m http.server"
