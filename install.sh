#!/bin/sh

localectl set-locale LANG=ja_JP.UTF-8
yum -y clean all
yum install -y epel-release
yum -y update
yum groupinstall -y 'Development tools'
yum install httpd mod_wsgi httpd-devel python-devel blender -y
yum install -y python-pip
pip install pip --upgrade
pip install -r /vagrant/requirements.txt
systemctl stop firewalld
systemctl disable firewalld
