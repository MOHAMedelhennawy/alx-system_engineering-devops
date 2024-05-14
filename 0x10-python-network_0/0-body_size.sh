#!/usr/bin/env bash
string=`curl -s $1`

echo ${#string}
