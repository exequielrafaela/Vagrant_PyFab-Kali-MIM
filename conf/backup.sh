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

tar -zcvf $Date.tar.gz /vagrant/
mcrypt $Date.tar.gz -k abc123 # ENCRYPT
rm $Date.tar.gz
mcrypt -k abc123 -d $Date.tar.gz.nc # DECRYPT