#include <cassert>
#include <iostream>
#include <vector>

enum class Direction {
  UP,
  RIGHT,
  DOWN,
  LEFT,
};

class GridDimensions {
 public:
  GridDimensions(int width, int height);
  int get_width();
  int get_height();

 private:
  int width_;
  int height_;
};

GridDimensions::GridDimensions(int width, int height)
    : width_(width), height_(height) {}

int GridDimensions::get_width() { return width_; }
int GridDimensions::get_height() { return height_; }

////////////////////////////////////////////////////////////////////////////////

class GridMember {
 public:
  GridMember(int x, int y);
  bool move(GridDimensions &grid_dimensions, Direction direction);
  int get_x();
  int get_y();

 private:
  int x_;
  int y_;
};

GridMember::GridMember(int x, int y) : x_(x), y_(y) {}

bool GridMember::move(GridDimensions &grid_dimensions, Direction direction) {
  switch (direction) {
    case Direction::UP:
      if (y_ == 0) return false;
      y_--;
      break;
    case Direction::RIGHT:
      if (x_ >= grid_dimensions.get_width() - 1) return false;
      x_++;
      break;
    case Direction::DOWN:
      if (y_ >= grid_dimensions.get_height() - 1) return false;
      y_++;
      break;
    case Direction::LEFT:
      if (x_ == 0) return false;
      x_--;
      break;
  }

  return true;
}

int GridMember::get_x() { return x_; }
int GridMember::get_y() { return y_; }

////////////////////////////////////////////////////////////////////////////////

class Player : public GridMember {
 public:
};

////////////////////////////////////////////////////////////////////////////////

class Grid {
 public:
  Grid(GridDimensions grid_dimensions);
  void add_member(GridMember grid_member);
  GridMember *get_member(int member_idx);
  bool move_member(int member_idx, Direction direction);

 private:
  GridDimensions grid_dimensions_;
  ::std::vector<GridMember> grid_members_;
};

Grid::Grid(GridDimensions grid_dimensions)
    : grid_dimensions_(grid_dimensions) {}

void Grid::add_member(GridMember grid_member) {
  grid_members_.push_back(grid_member);
}

bool Grid::move_member(int member_idx, Direction direction) {
  return grid_members_[member_idx].move(grid_dimensions_, direction);
}

GridMember *Grid::get_member(int member_idx) {
  return &grid_members_[member_idx];
}

////////////////////////////////////////////////////////////////////////////////

void test_grid_bounds() {
  Grid grid(GridDimensions(15, 15));

  GridMember player(0, 0);
  grid.add_member(player);
  assert(!grid.move_member(0, Direction::UP));
  GridMember *fetched_player = grid.get_member(0);
  for (int i = 0; i < 14; i++) {
    assert(grid.move_member(0, Direction::DOWN));
  }

  assert(!grid.move_member(0, Direction::DOWN));
}

int main() { test_grid_bounds(); }
