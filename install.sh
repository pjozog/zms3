#!/bin/bash

PREFIX=/usr/local/bin/

if [ "$EUID" -ne 0 ]; then
    echo "This script must be run as root."
    exit
fi

echo "Installing to ${PREFIX}"

this_dir=$(dirname $0)
cp "${this_dir}/zms3.py" ${PREFIX}
cp "${this_dir}/zms3-stage" ${PREFIX}
cp "${this_dir}/zms3-upload" ${PREFIX}
