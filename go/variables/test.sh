#!/usr/bin/env bash
cd "$(dirname "$0")"

source ../../bash/testing/compare_output.sh

compare_output "$(test_name)" "$(go run variables.go)" "test
1 2 3
test 2"

