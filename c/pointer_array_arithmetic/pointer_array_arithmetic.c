#include <assert.h>

int main() {
  int test[3] = {1, 2, 3};

  assert(test[0] == 1);
  assert(test[1] == 2);
  assert(test[2] == 3);

  assert(*test == 1);
  assert(*(test + 1) == 2);
  assert(*(test + 2) == 3);
}
