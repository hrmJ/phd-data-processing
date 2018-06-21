#! /bin/bash

sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
apt -y install python3-psycopg2
apt -y install python3-lxml
apt -y install python3-sqlalchemy
apt -y install python3-pip
pip3 install progress
pip3 install termcolor
pip3 install bs4
