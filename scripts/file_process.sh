#!/bin/bash
#########################################################################
# File Name: t.sh
# Author: Junyi Li
# Personal page: dukeenglish.github.io
# Created Time: 00:09:13 2020-02-23
#########################################################################
set -o errexit
for file in *
    do
        echo $file
        if ! test -f $file
        then
            echo $file
            cd $file
#            mv README.md tt.md
            python ../pytmp.py tt.md > README.md
#             rm -rf tt.md
            cd ..
        fi
    done
    # mv README.md tt.md
#python p
