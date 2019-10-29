## Introduction

Simple boilerplate web scraper program to look for a XPATH in a URL webpage and send out a slack message.

Uses a base docker image with pip, python3, chrome and selenium for python installed. 
https://github.com/gyanesh-mishra/selenium-chrome-pip

## Getting Started

1. Create a file `.env` following the pattern from `.env.example`.
2. Run `make image` to build and tag the docker image.
3. Run `make run` to run the docker container.
