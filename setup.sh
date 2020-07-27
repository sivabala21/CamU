#!/bin/bash
echo -e "                \e[31;1mInstalling Cam_U\e[0m"
apt-get -y update 
apt-get -y install python 
apt-get -y install python2 
#apt-get -y install php 
apt-get -y install unzip 
apt-get -y install wget 
clear
echo -e "\e[1;92m[*]Cam_U is installed To run CamU type '\e[93mpython3 CamU.py'\e[0m "
