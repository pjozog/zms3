#!/bin/bash

PREFIX=/usr/local/bin/

if [ "$EUID" -ne 0 ]; then
    echo "This script must be run as root."
    exit
fi

echo "Uninstalling from ${PREFIX}"

rm -f "${PREFIX}/zms3.py"
rm -f "${PREFIX}/zms3-stage"
rm -f "${PREFIX}/zms3-upload"
