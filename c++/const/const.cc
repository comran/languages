#include <cassert>
#include <iostream>

void test1(const int i) {
  // Passed value is copied and made constant.
  assert(i == 0);
}
void test2(const int* i) {
  // Passing a pointer to a constant value.
  assert(*i == 0);
}

void test3(const int* const i) {
  // Passing a constant pointer to a constant value.
  assert(*i == 0);
}

void test4(int* const i) {
  // Passing a constant pointer to a modifiable value.
  assert(*i == 0);
  (*i)++;
}

void test5(const int* const* const i) { assert(**i == 1); }
void test6(const int* const* const i) { assert(**i == -1); }

int main() {
  int i[2] = {0, -1};
  test1(*i);
  test2(i);
  test3(i);
  test4(i);
  assert(*i == 1);

  int* j = &i[0];
  int* k = j;
  int* const* const l = &k;
  test5(l);

  // Increment pointer value of pointer that l points to. This will point to
  // index 1 of i.
  k++;
  test6(l);
}