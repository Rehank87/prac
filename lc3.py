s = "Hello, World!"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = counter = 0
        char_set = set()
        print(f"counter is {counter}")

        for right in range(len(s)):
            print(f"right is {right}")
            print(f"left is {left}")
            while s[right] in char_set:
                print(f"{s[right]} is already in char_set")
                char_set.remove(s[left])
                print(f"{s[left]} is removed")
                left += 1
                print(f"left incremented to {left}")
                print(char_set)

            char_set.add(s[right])
            print(f"{s[right]} added to char_set")
            print(char_set)
            counter = max(counter, right - left  + 1)
            print(f"counter is now {counter}")
            print(f"========================")
        return counter


result = Solution()
print(result.lengthOfLongestSubstring(s))