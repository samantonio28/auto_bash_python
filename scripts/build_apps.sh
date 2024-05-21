#!/bin/bash

if [[ $1 ]]
then
    if [[ ! $1 =~ ^[0-9]+$ ]] || [[ $1 =~ ^[0]+$ ]]
    then   
        echo "incorrect size"
        exit 1
    fi
fi

if [ ! -d "./apps" ]
then
    mkdir "./apps"
fi

rm ./apps/*.exe

for file in ./c_files/*.c; do
    fst=${file/"./c_files/"/""}
    fst=${fst/".c"/""}
    NMAXES=("10" "500" "1000" "1500" "2000" "2500" "3000" "3500" "4000" "5000" "10000")

    if ! echo "${NMAXES[@]}" | grep "$1"
    then
        NMAXES+=("$1")
    fi

    for NMAX in "${NMAXES[@]}"; do
        echo -en "\e[K$fst\t$NMAX\r" 
        if ! gcc -std=gnu99 -O0 -Wall -Werror -DN="$NMAX" -Wpedantic -Wextra -Wvla -o "./apps/""$fst""_$NMAX"".exe" "$file" -lrt -lm; then
            exit 1
        fi
    done
done
echo
exit 0