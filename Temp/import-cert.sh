#!/bin/sh

#Using my little script
#I have created a little script that will retrieve the certificate and imports it into the DB.

#Create a file, lets call it import-cert.sh and the contents of the file is as follows:


#
# usage:  import-cert.sh remote.host.name [port]
#
REMHOST=$1
REMPORT=${2:-443}
exec 6>&1
exec > $REMHOST
echo | openssl s_client -connect ${REMHOST}:${REMPORT} 2>&1 |sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p'
certutil -d sql:$HOME/.pki/nssdb -A -t TC -n "$REMHOST" -i $REMHOST 
exec 1>&6 6>&-

#Make sure the script is executable.

#To add a certificate from a site you type the following:

#import-cert.sh dirae.lunarservers.com 2083
#In this case it uses port 2083 instead of the default port 443. If it’s the default port you don’t have to include the port.

#To see which certificates are included your database:
#certutil -L -d sql:$HOME/.pki/nssdb

#And should you want to delete a certificate
#certutil -D -n  -d sql:$HOME/.pki/nssdb

#I hope this solves a lot of frustrations about big red screens when accessing secure websites.