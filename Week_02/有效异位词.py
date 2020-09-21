#solution 1:count the number of each char in the string and check whether the two dictionaries are the same.Even for unicode, this method can work well
class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

#solution 2: sorted and compare, time complexity: klogk, space complexity: O(k), k = max(len(s), len(t))
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
#solution 3: use fixed size array to store char numer
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        for c in t:
            count[ord(c) - ord("a")] -= 1
        for n in count:
            if n : return False
        return True 

