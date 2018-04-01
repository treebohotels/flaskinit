#!/bin/bash
#rm -rf ~/direct_config
set -x

export ENV=$1
export VERSION=$2
export APP=$3
export CONFIG_BRANCH=$4



export SERVICE=$APP
export HOME=/opt/$APP

if [ ! -d "$HOME" ]; then
    echo "Creating  directory at  $HOME"
    mkdir -p $HOME
fi

cd $HOME


rm -rf $HOME/direct_config
git clone -n -b $CONFIG_BRANCH git@bitbucket.org:treebo/direct_config.git --depth 1 $HOME/direct_config
cd $HOME/direct_config
git checkout HEAD $SERVICE
cd $HOME

sed -i --in-place "s|DUMMY_HOME|$HOME|g" $HOME/docker/docker_env"/"common.env
sed -i --in-place "s|DUMMY_HOME|$HOME|g" $HOME/docker/docker_env"/"$ENV.env


source $HOME/docker/docker_env"/"common.env
source $HOME/docker/docker_env"/"$ENV.env

echo "Using docker_env file: $APP_ENV_PATH"


if [ ! -d "$HOST_LOG_ROOT" ]; then
    echo "Creating HOST_LOG_ROOT directory at: $HOST_LOG_ROOT"
    mkdir -p $HOST_LOG_ROOT
fi


if [ "$ENV" == "dev" ]; then
     docker-compose -p $SERVICE_NAME -f $HOME/docker/compose/docker-dev.yml up --build -d
else
	 docker-compose -p $SERVICE_NAME -f $HOME/docker/compose/docker-base.yml up --build -d

fi
