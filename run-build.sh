#!/usr/bin/env bash

# A "build"


LOGDIR=`mktemp -d 2>/dev/null || mktemp -d -t 'fancyapp-logs'`
LOGFILE="${LOGDIR}/log.txt"

touch "${LOGFILE}"

echo "Building fancy project..."

echo "$(date) : initializing..." >> "${LOGFILE}"
echo "$(date) : done." >> "${LOGFILE}"

echo "Build completed."
echo "Log written to ${LOGFILE}."
