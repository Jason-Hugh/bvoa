#!/bin/bash

######################################################################
# Basics:
apt-get -qq update
DEBIAN_FRONTEND=noninteractive apt-get -yq -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" upgrade
apt-get -qq --yes install wget nano vim less gnupg curl man coreutils git

apt-get -qq --yes install locales
sed -i 's/^# *\(en_US.UTF-8 UTF-8\)/\1/' /etc/locale.gen
locale-gen
update-locale LANG=en_US.UTF-8

######################################################################
# Python 3:
# python3, pip, and python symlink are provided by python:3.14-slim base image
pip install poetry
pip install psycopg2

######################################################################
# Database clients:
apt-get -qq --yes install postgresql-client libpq-dev
apt-get -qq --yes install python3-psycopg2

# ######################################################################
# # XML:
# apt-get -qq --yes install libxml2-dev libxslt1-dev libxml2-utils
# apt-get -qq --yes install libsaxonb-java
# python -m pip install lxml

# ######################################################################
# # RA:
# python -m pip install radb

# ######################################################################
# # MongoDB client:
# curl -fsSL https://pgp.mongodb.com/server-7.0.asc | \
#    sudo gpg -o /etc/apt/trusted.gpg.d/mongodb-server-7.0.gpg \
#    --dearmor
# echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" > /etc/apt/sources.list.d/mongodb-org-7.0.list
# apt-get -qq --yes update
# apt-get -qq --yes install mongodb-mongosh mongodb-org-tools
# python -m pip install pymongo

# ######################################################################
# # Spark:
# apt-get -qq --yes install openjdk-8-jdk
# python -m pip install pyspark

######################################################################
# JavaScript:
apt-get -qq --yes install npm

