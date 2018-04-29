#!/bin/sh

repository="$1"
command="glue -t brakeman -f json $1"
$command


