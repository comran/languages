#include <cassert>
#include <vector>

int uniquePathsWithObstacles(::std::vector<::std::vector<int>>& obstacleGrid) {
  ::std::vector<::std::vector<int>> dp;
  for (int i = 0; i < obstacleGrid.size(); i++) {
    dp.push_back(::std::vector<int>());

    for (int j = 0; j < obstacleGrid[0].size(); j++) {
      dp[i].push_back(0);
    }
  }

  dp[0][0] = 1;

  for (int i = 0; i < obstacleGrid.size(); i++) {
    for (int j = 0; j < obstacleGrid[0].size(); j++) {
      if (obstacleGrid[i][j] == 1) {
        dp[i][j] = 0;
      } else {
        if (i > 0) {
          dp[i][j] += dp[i - 1][j];
        }
        if (j > 0) {
          dp[i][j] += dp[i][j - 1];
        }
      }
    }
  }

  return dp[dp.size() - 1][dp[0].size() - 1];
}

int main() {
  {
    ::std::vector<::std::vector<int>> obstacles{
        ::std::vector<int>{0, 0, 0},
        ::std::vector<int>{0, 1, 0},
        ::std::vector<int>{0, 0, 0},
    };

    int result = uniquePathsWithObstacles(obstacles);
    assert(result == 2);
  }

  {
    ::std::vector<::std::vector<int>> obstacles{
        ::std::vector<int>{0, 0},
    };

    int result = uniquePathsWithObstacles(obstacles);
    assert(result == 1);
  }

  {
    ::std::vector<::std::vector<int>> obstacles{
        ::std::vector<int>{0, 1},
    };

    int result = uniquePathsWithObstacles(obstacles);
    assert(result == 0);
  }
}
