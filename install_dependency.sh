#!/bin/bash
echo "Lab1 gazebo introduction set up "

echo "install dependency"

sudo apt-get install -y \
	gazebo7 \
	python-pip \
	ros-kinetic-gazebo-ros-pkgs \
	ros-kinetic-gazebo-ros-control \
	ros-kinetic-joint-state-controller \
	ros-kinetic-velocity-controllers \
	ros-kinetic-diff-drive-controller \
	ros-kinetic-joy \
	python-frozendict \
	libxslt-dev \
	libxml2-dev \
	python-lxml \
	python-bs4 \
	python-tables \
    python-sklearn \
    apt-file \
    iftop \
    atop \
    ntpdate \
    python-termcolor \
    python-sklearn \
    libatlas-base-dev \
    python-dev \
    ipython \
    python-sklearn \
    python-smbus

sudo apt remove -y \
	python-ruamel.yaml \
	python-ruamel.ordereddict

pip install --upgrade --user \
	PyContracts==1.7.15 \
    DecentLogs==1.1.2\
	QuickApp==1.3.8 \
	conftools==1.9.1 \
	comptests==1.4.10 \
	procgraph==1.10.6 \
	pymongo==3.5.1 \
	ruamel.yaml==0.15.34

sudo apt-get install -y \
	bibtex2html \
	pdftk


