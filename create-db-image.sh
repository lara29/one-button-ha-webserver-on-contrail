#!/bin/bash

cp ubuntu-image.img db.img

virt-customize -a db.img \
--root-password password:juniper123 \
--hostname db-server \
--run-command 'echo "ubuntu ALL=(root) NOPASSWD:ALL" | tee -a /etc/sudoers.d/ubuntu' \
--chmod 0440:/etc/sudoers.d/ubuntu \
--copy-in dbfb:/root/ \
--copy-in dbfb:/etc/network/if-up.d/ \
--run-command 'chmod +x /etc/network/if-up.d/dbfb' \
--install mysql-server,mysql-client \
--run-command 'cp /etc/mysql/mysql.conf.d/mysqld.cnf /etc/mysql/my.cnf' \
--run-command 'sed -i "/^bind-address/c\bind-address = 0.0.0.0" /etc/mysql/my.cnf'
