#!/usr/bin/env bash
cd "$(dirname "$0")"

source ../../bash/testing/compare_output.sh

# Skip test on mac os.
if [[ "$OSTYPE" == "darwin"* ]]
then
  exit 0
fi

nasm -f elf64 hello.asm
ld -s -o hello hello.o

compare_output "$(test_name)" "$(./hello)" "hello world"

