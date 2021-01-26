#!/bin/bash

INDEX_NAME="$1"

for SERVER in $(seq -f "%02g" 1 20);
    do 
        echo "Alln $SERVER";
        ssh -q splunk@sra-index-alln-$SERVER grep -nr "$INDEX_NAME" /apps/splunk/etc/slave-apps/index-global/default/indexes.conf
        echo ""
        echo ""
        echo "RCDN $SERVER";
        ssh -q splunk@sra-index-rcdn-$SERVER grep -nr "$INDEX_NAME" /apps/splunk/etc/slave-apps/index-global/default/indexes.conf
        echo ""
        echo ""
    done
