#include <cassert>
#include <iostream>

class Base {
 public:
  virtual ~Base() = default;
  virtual ::std::string get_name() = 0;
};

class Derived1 : public Base {
 public:
  ~Derived1() {}
  ::std::string get_name() { return "Derived1"; }
};

class Derived2 : public Base {
 public:
  ~Derived2() {}
  ::std::string get_name() { return "Derived2"; }
};

int main() {
  Derived1 derived_1;
  Base *base = dynamic_cast<Base *>(&derived_1);

  assert(base->get_name() == "Derived1");
  assert(derived_1.get_name() == "Derived1");

  Derived1 derived_1_stack;
  bool did_detect_bad_cast = false;
  try {
    Derived2 &r1 = dynamic_cast<Derived2 &>(derived_1_stack);
  } catch (std::exception &e) {
    did_detect_bad_cast = true;
  }

  assert(did_detect_bad_cast);
}