#include <cassert>

int main() {
  int count = 10;

  auto test_lambda = [count]() mutable -> int { return --count; };

  assert(test_lambda() == 9);
  assert(count == 10);
  assert(test_lambda() == 8);
  assert(count == 10);
  assert(test_lambda() == 7);
  assert(count == 10);
  assert(test_lambda() == 6);
  assert(count == 10);

  // Lambda modifies its own copy of count, not the one passed to it.
  assert(count == 10);

  // Passing count by reference fixes this. It also removes the need to make
  // the lambda mutable.
  //
  // Also note that the compiler can deduce that the return type is int for
  // this lambda.
  auto test_lambda_reference = [&count]() { return --count; };
  assert(test_lambda_reference() == 9);
  assert(count == 9);
  assert(test_lambda_reference() == 8);
  assert(count == 8);
  assert(test_lambda_reference() == 7);
  assert(count == 7);
  assert(test_lambda_reference() == 6);
  assert(count == 6);
}