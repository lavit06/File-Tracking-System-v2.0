#!/bin/bash

##**************************************************************************************
##**************************************************************************************
##**************************************************************************************
##**************************************************************************************
##************░█▀▀▄░▒█░░░░▒█▀▀█░▒█▀▀▀█░▒█▀▀▄░█▀▀▄░▒█▀▀▀█░▒█░▄▀░▒█▀▀▀░▀▀█▀▀**************
##************▒█▄▄█░▒█░░░░▒█░▄▄░▒█░░▒█░▒█▀▀▄▒█▄▄█░░▀▀▀▄▄░▒█▀▄░░▒█▀▀▀░░▒█░░**************
##************▒█░▒█░▒█▄▄█░▒█▄▄▀░▒█▄▄▄█░▒█▄▄█▒█░▒█░▒█▄▄▄█░▒█░▒█░▒█▄▄▄░░▒█░░**************
##**************************************************************************************
##************************** ▀▄▀▄▀▄GitHub - algobasket▄▀▄▀▄▀ ***************************
##**************************************************************************************
##********************************  Made By Algobasket  ********************************
##**************************************************************************************

# Run the shell script to add the host entry
sudo ./add-host-entry.sh

# Start Docker Compose
docker-compose up --build