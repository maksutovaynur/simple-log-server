#!/bin/bash

BASE_DIR=$(realpath $(dirname $0))
cd $BASE_DIR
touch .env

CMD=$1
COMMANDS=('run' 'stop' 'token-add' 'token-list' 'clean' 'env')


if [[ ! "$CMD" ]]
then
  echo "Usage:
    ./manage.sh <command> <args>
    command = (${COMMANDS[@]})
  "
  exit 0
fi

if ! [[ ${COMMANDS[*]} =~ "$CMD" ]]
then
  echo "Command '$CMD' not found. Please use one of [${COMMANDS[@]}]"
  exit 1
fi

if [ $CMD == "run" ]
then
  sudo chown -R $USER .data
  docker-compose up --build -d
elif [ $CMD == "stop" ]
then
  docker-compose down
elif [ $CMD == "token-add" ]
then
  docker exec -it cash_api python -m src.scripts.add_token $2
elif [ $CMD == "token-list" ]
then
  docker exec -it cash_api python -m src.scripts.list_tokens
elif [ $CMD == "env" ]
then
  nano .env
elif [ $CMD == "clean" ]
then
  read -p "This will delete all existing database data. Are you sure? [y/N] " -n 1 -r
  echo    # (optional) move to a new line
  if [[ ! $REPLY =~ ^[Yy]$ ]]
  then
    echo "No clean will be performed. Exit."
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1 # handle exits from shell or function but don't exit interactive shell
  else
    docker-compose down
    sudo rm -rf ./.data
  fi
fi


