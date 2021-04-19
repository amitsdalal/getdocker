#!/usr/bin/env bash

OS=`awk '/^ID=/' /etc/*-release | awk -F'=' '{ print tolower($2) }'`

if [ $OS == ubuntu ]
then
echo ubuntu
elif [ $OS == centos ]
then 
echo centos
else
echo "os not detected as centos or ubuntu, do it apne app"
fi