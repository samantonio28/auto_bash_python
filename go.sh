#!/bin/bash

extra=""
if [[ $1 ]]
then
    if [[ ! $1 =~ ^[0-9]+$ ]] || [[ $1 =~ ^[0]+$ ]]
    then   
        echo "incorrect size"
        exit 1
    fi
    extra="$1"
fi

./scripts/build_apps.sh "$extra"
t_output=$?
if [[ $t_output != 0 ]]; then
    echo "problem with building apps"
    exit 2
fi
echo "  builded"

./scripts/update_data.sh
t_output=$?
if [[ $t_output != 0 ]]; then
    echo "problem with updating data"
    exit 3
fi
echo "  updated"

python3 "./scripts/make_preproc.py"
t_output=$?
if [[ $t_output != 0 ]]; then
    echo "problem with making preproc data" 
    exit 4
fi
echo "  preproc is made"

python3 "./scripts/make_postproc.py" "$extra"
t_output=$?
if [[ $t_output != 0 ]]; then
    echo "problem with postproc data"
    exit 5
fi
echo "  postproc is made"

echo "done"