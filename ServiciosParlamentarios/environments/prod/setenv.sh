#!/bin/bash

readonly SP_PATH=/var/log/ServiciosParlamentarios
readonly USER=`whoami`

if [ ! -d "$SP_PATH" ]; then
        sudo mkdir $SP_PATH
fi

sudo chown $USER $SP_PATH -R
sudo chmod 700 $SP_PATH -R
