#!/usr/bin/env bash
cd "$(dirname "$0")"

source ../../bash/testing/compare_output.sh

compare_output "$(test_name)" "$(go run hello.go)" "hello world"

