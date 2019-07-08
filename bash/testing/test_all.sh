#!/usr/bin/env bash
cd "$(dirname "$0")"
cd ../..

TESTS="$(find . -name "test.sh")"
for TEST in $TESTS
do
  set +e
  sh $TEST
  set -e
done

