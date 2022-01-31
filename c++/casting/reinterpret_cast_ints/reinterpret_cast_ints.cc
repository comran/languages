#include <cassert>

class CastClass {
 public:
  int get_one() { return this->one; }
  int get_two() { return this->two; }
  int get_three() { return this->three; }

 private:
  int one;
  int two;
  int three;
};

int main() {
  int test[3] = {1, 2, 3};

  assert(test[0] == 1);
  assert(test[1] == 2);
  assert(test[2] == 3);

  CastClass* test_reinterpret_cast = reinterpret_cast<CastClass*>(test);

  assert(test_reinterpret_cast->get_one() == 1);
  assert(test_reinterpret_cast->get_two() == 2);
  assert(test_reinterpret_cast->get_three() == 3);

  int* class_to_int_cast = reinterpret_cast<int*>(test_reinterpret_cast);

  assert(class_to_int_cast[0] == 1);
  assert(class_to_int_cast[1] == 2);
  assert(class_to_int_cast[2] == 3);
}
