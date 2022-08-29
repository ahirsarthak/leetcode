# LC 17 Phone Number
# O(n4^n)

 def letterCombinations(self, digits: str) -> List[str]:

      letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                  "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

       if not digits:
            return []

        result = [""]

        for digit in digits:
            result = [x+y for x in result for y in letters[digit]]
        return result
