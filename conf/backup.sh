#!/bin/bash

#Encrypted Backup Script

#tar -zcvf archive-name.tar.gz directory-name
#Where,
#-z : Compress archive using gzip program
#-c : Create archive
#-v : Verbose i.e display progress while creating archive
#-f : Archive File name

Date="BACKUP-$(date +"%Y-%m-%d")"
echo "####################################"
echo "######### Date: $Date #########"
echo "####################################"

mkdir /vagrant/conf/backup
tar -zcvf /vagrant/conf/backup/$Date.tar.gz /vagrant/
mcrypt /vagrant/conf/backup/$Date.tar.gz -k abc123 # ENCRYPT
rm /vagrant/conf/backup/$Date.tar.gz
mcrypt -k abc123 -d /vagrant/conf/backup/$Date.tar.gz.nc # DECRYPT