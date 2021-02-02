SHELL := /bin/bash

.PHONY: deploy
deploy:
	export EXTERNAL_IP=`hostname -I | awk '{print $1}'` && echo $(EXTERNAL_IP) && docker-compose up