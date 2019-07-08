#!/usr/bin/env bash

function test_name {
  echo "$(pwd)"
}

function compare_output {
  TEST_PATH="$1"
  CORRECT_OUTPUT="$2"
  ACTUAL_OUTPUT="$3"

  if [ "$ACTUAL_OUTPUT" != "$CORRECT_OUTPUT" ]
  then
    printf "\e[91mTest failed (Output mismatch): $TEST_PATH\e[0m\n"
    printf "Expected: $CORRECT_OUTPUT\n"
    printf "Got: $ACTUAL_OUTPUT\n"
    exit 1
  else
    printf "\e[92mTest passed: $TEST_PATH\e[0m\n"
  fi
}

