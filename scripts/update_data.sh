#!/bin/bash

echo
if [ ! -d "./data" ]
then
    mkdir "./data"
fi

methods=("main" "time" "tsc")

prefix=""

for method in "${methods[@]}"
do
    if [ ! -d "./data/$method""_f" ]
    then
        mkdir "./data/$method""_f"
    fi
    if [ ! -f "./data/$method""_f/i.txt" ]
    then
        echo "0" > "./data/$method""_f/i.txt"
    fi

    read -r i < "./data/$method""_f/i.txt"
    for app in apps/"$method"*.exe     
    do                                                
        if ((0 <= i && i <= 9))
        then
            prefix="000"
        elif ((10 <= i && i <= 99))
        then
            prefix="00"
        elif ((100 <= i && i <= 999))
        then
            prefix="0"
        else
            prefix=""
        fi
        file=${app/"apps/"/""}
        file_to_echo=${file/".exe"/".txt"}
        file="./data/$method""_f/$prefix""$i""_""$file_to_echo"
        echo -en "\e[K$file_to_echo\r" 
        if [[ $method == "main" ]]
        then
            condition="1"
            while [[ $condition == "1" ]]
            do
                for ((j = 0; j < 500; j++)); do
                    ./"$app" >> "$file"
                done
                python3 ./scripts/is_rse_lt_1pct.py "$file"
                condition=$?
            done
        else
            ./"$app" > "$file"
        fi
        ((i++))
    done
    echo "$i" > "./data/$method""_f/i.txt"
    
done
echo
exit 0