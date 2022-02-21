#include <memory>
#include <cassert>

class Test {
 public:
  Test(int a) : _a(a) {}

  int get_a() { return _a; }

 private:
  int _a;
};

auto test() {
  ::std::unique_ptr<Test> test_ptr_unique = ::std::make_unique<Test>(1);
  assert(test_ptr_unique->get_a() == 1);

  return test_ptr_unique;
}

int main() {
  auto test_ptr_unique = test();
  assert(test_ptr_unique->get_a() == 1);

  // Convert unique pointer -> shared pointer.
  ::std::shared_ptr<Test> test_shared_ptr = ::std::move(test_ptr_unique);
  assert(test_shared_ptr->get_a() == 1);
}