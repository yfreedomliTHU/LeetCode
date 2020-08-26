#https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hashmap = {"2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz",
                    }
        result = []
        tmp = []
        def back(index):
            if index == len(digits):
                result.append("".join(tmp))
            else:
                for x in hashmap[digits[index]]:
                    tmp.append(x)
                    back(index+1)
                    tmp.pop() # pop and get next letter of digits[index]
        
        back(0)
        
        return result
