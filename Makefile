SHELL := /bin/bash

.PHONY: build
build:
	docker-compose build

# use d flag for background task
.PHONY: deploy
deploy:	
	docker-compose up -d
