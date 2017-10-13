#!/bin/bash

CUR_FILE=${BASH_SOURCE[0]}
CUR_DIR=$(cd `dirname $CUR_FILE`;pwd)

SERVER_FILE="typing_server.py"
SERVER_PATH=$CUR_DIR/../$SERVER_FILE
SERVER_NAME=(`basename $SERVER_FILE .py`)

process_num(){
    process_num=$(ps -ef | grep $SERVER_FILE | grep -v grep | wc -l)
    echo $process_num
}

start(){
    process_num=$(process_num)

    if [ ${process_num} -ne 0 ]; then
        echo "${SERVER_NAME}已启动, 请使用重启命令"

        return 1
    else
        nohup python $SERVER_PATH > /dev/null 2>&1 &

        sleep 1

        process_num=$(process_num)
        if [ ${process_num} -ne 0 ]; then
            echo "${SERVER_NAME}启动成功"
        else
            echo "${SERVER_NAME}启动失败"
        fi
    fi
}

stop(){
    process_num=$(process_num)

    if [ ${process_num} -eq 0 ]; then
        echo "${SERVER_NAME}未启动,不用停止"

        return 1
    else

        ps -ef | grep $SERVER_FILE | grep -v grep | awk '{print $2}' | xargs kill

        sleep 1

        process_num=$(process_num)
        if [ ${process_num} -eq 0 ]; then
            echo "${SERVER_NAME}停止成功"
        else
            echo "${SERVER_NAME}停止失败"
        fi
    fi
}

restart(){
    stop
    sleep 0.5
    start
}

status(){
    process_num=$(process_num)

    if [ $process_num -ne 0 ]; then
        echo -e "$SERVER_NAME \033[32m[active]\033[0m"
    else
        echo -e "$SERVER_NAME \033[31m[dead]\033[0m"
    fi
}

usage(){
    me=`basename $0`
    echo >&2 "Usage: bash $me {start|stop|restart|status}"
    exit 1
}


if [ $# -eq 0 ]; then
    usage
    exit
fi

case $1 in
    start|stop|restart|status)
    $1
    ;;
    *)
    usage
    exit
esac
