#!make

run:
	@echo "+\n++ Running application ...\n+"
	@docker run -d --shm-size=2g --env-file=.env swu-informer

image:
	@echo "+\n++ Building image ...\n+"
	@docker build . -t swu-informer