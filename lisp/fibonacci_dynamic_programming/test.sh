#!/usr/bin/env bash
cd "$(dirname "$0")"

source ../../bash/testing/compare_output.sh

compare_output "$(test_name)" "$(clisp fib_dynamic_programming.lsp)" "
1 
1 
2 
3 
5 
8 
13 
21 
34 
55 
89 
144 
233 
377 
610 
987 
1597 
2584 
4181 
6765 
10946 
17711 "

