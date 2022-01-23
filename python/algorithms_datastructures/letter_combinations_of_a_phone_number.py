# LC 17

from typing import List


LETTERS = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = [LETTERS[int(x)] for x in digits]

        return self.combinations(letters)

    def combinations(self, letters):
        letters_len = len(letters)
        if letters_len == 0:
            return []
        if letters_len == 1:
            return list(letters[0])

        combinations = []
        other_combos = self.combinations(letters[1:])
        for letter in letters[0]:
            combinations.extend([letter + x for x in other_combos])

        return combinations


x = Solution()
assert x.letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
