#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

PYTHON_FILES=$(find $SCRIPT_DIR -name "*.py")

EXIT_CODE=0
for PYTHON_FILE in $PYTHON_FILES
do
    python3 "$PYTHON_FILE"
    if [ $? -ne 0 ]
    then
        echo "FAILED: $PYTHON_FILE"
        EXIT_CODE=1
    else
        echo "SUCCEEDED: $PYTHON_FILE"
    fi
done

exit $EXIT_CODE
