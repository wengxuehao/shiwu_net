#!/bin/sh
## service name
#项目的目录
SERVICE_DIR=/root/shiwu/shiwu
#gunicorn的名字
SERVICE_NAME=gunicorn
#gunicorn的配置文件名
SERVICE_CONF=gunicon.py
#pid存放的位置
PID=gunicorn/.pid
export PATH=$PATH:/usr/local/python3/bin
cd $SERVICE_DIR
git checkout . && git clean -xdf
git pull

start(){
       nohup gunicorn build.wsgi:application -c $SERVICE_DIR/$SERVICE_CONF >/dev/null 2>&1 &
       echo $! > $SERVICE_DIR/$PID
       echo "*** start $SERVICE_NAME ***"
}
stop(){
       kill `cat $SERVICE_DIR/$PID`
       rm -rf $SERVICE_DIR/$PID
       echo "*** stop $SERVICE_NAME ***"

       sleep 2
       P_ID=`ps -ef | grep -w "$SERVICE_NAME" | grep -v "grep" | awk '{print $2}'`
       if [ "$P_ID" == "" ]; then
           echo "*** $SERVICE_NAME process not exists or stop success ***"
       else
           echo "*** $SERVICE_NAME process pid is:$P_ID ***"
           echo "*** begin kill $SERVICE_NAME process,kill is:$P_ID ***"
           kill -9 $P_ID
       fi
}
f_usage() {
   echo "USAGE: restart [options]"
   echo "OPTIONS:"
   echo "       start"
   echo "       stop "
   echo "       restart"
}
case "$1" in

   "start")
       start
       ;;
   "stop")
       stop
       ;;
   "restart")
       stop
       sleep 2
       start
       echo "*** restart $SERVICE_NAME ***"
       ;;
   *)
   f_usage
   ;;

esac
exit 0