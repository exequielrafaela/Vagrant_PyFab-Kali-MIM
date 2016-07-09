sudo mkdir -p /var/www/personas.santanderrio.com.ar/public_html
sudo mkdir -p /var/www/binbash.com.ar/public_html

#sudo chown -R $USER:$USER /var/www/ejemplo.com/public_html
#sudo chown -R $USER:$USER /var/www/pruebas.com/public_html

sudo chmod -R 755 /var/www

#wget -P /var/www/ -E -H -k -K -p https://www.personas.santanderrio.com.ar/hb/html/login/principal.jsp?rndPrm31=1467435290174


$ sudo wget \
     --recursive \
     --no-clobber \
     --page-requisites \
     --html-extension \
     --convert-links \
     --restrict-file-names=windows \
     --domains website.org \
     --no-parent \
         https://www.personas.santanderrio.com.ar/hb/html/login/principal.jsp?rndPrm630=1467614755855

$ wget \
     --recursive \
     --no-clobber \
     --page-requisites \
     --html-extension \
     --convert-links \
     --restrict-file-names=windows \
     --domains website.org \
     --no-parent \
         http://www.binbash.com.ar

sudo a2enmod ssl
sudo a2ensite personas.santanderrio.com.ar.conf
sudo a2ensite binbash.com.ar.conf

