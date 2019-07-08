#include <iostream>

class HelloWorld {
 public:
  HelloWorld () : hello_string_("Hello world!") {}

  void PrintHello () {
    ::std::cout << hello_string_ << ::std::endl;
  }

 private:
  const char * hello_string_;
};

int main () {
  HelloWorld hello_world;
  hello_world.PrintHello();

  return 0;
}
