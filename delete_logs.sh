#!/bin/bash

log_dir="/home/user1/sample"
log_files=$(find "$log_dir" -type f -name  "*.log*")
echo $?

while IFS= read -r itr; do
        echo "$itr"
        rm -rf  "$itr"  1>>/home/user1/rm_cmd.txt
        echo $?
done <<< "$log_files"
