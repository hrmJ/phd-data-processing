#! /bin/bash

export LANGUAGE=en_US.UTF-8
export LC_ALL=en_US.UTF-8
sudo update-locale

sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
apt -y install python3-psycopg2 python3-lxml python3-pip
apt -y install python3-sqlalchemy postgresql postgresql-contrib
pip3 install progress
pip3 install termcolor
pip3 install bs4
