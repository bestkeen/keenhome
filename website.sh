#!/bin/bash

if [ $# -eq 0 ]; then
echo ">>>>>>>>Runnig script with parameters(start/stop)<<<<<<<<)"
exit 1

elif [[ $1 == "start" ]];then
/etc/init.d/nginx restart
uwsgi --ini InquireScore_uwsgi.ini
exit 1

elif [[ $1 == "stop" ]];then
/etc/init.d/nginx stop
killall -9 uwsgi
exit 1
fi
