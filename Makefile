SHELL := /bin/bash

EXTERNAL_IP = $(shell hostname -I | awk '{print $$1}')

.PHONY: build
build:
	echo $(EXTERNAL_IP) && export EXTERNAL_IP=$(EXTERNAL_IP) && docker-compose build

# use d flag for background task
.PHONY: deploy
deploy:	
	docker-compose up -d
