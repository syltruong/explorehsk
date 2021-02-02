SHELL := /bin/bash

.PHONY: build
build:
	export EXTERNAL_IP=`hostname -I | awk '{print $1}'` && echo $(EXTERNAL_IP) && docker-compose build