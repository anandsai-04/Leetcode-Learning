class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        if len(s) < k: 
            return False  # 🚫 If string is smaller than k, no valid substring exists

        for i in range(len(s) - k + 1):  # 🔍 Iterate through all possible substrings of length k
            count = 1  # 🧮 Count consecutive identical characters

            # ✅ Check if all k characters in the substring are the same
            for j in range(i, i + k - 1):
                if s[j] == s[j + 1]:
                    count += 1  # ➕ Increase count if consecutive characters are the same
                else:
                    break  # ❌ Break if mismatch occurs

            # 🔎 Ensure the substring is not part of a larger group
            if count == k and (i == 0 or s[i - 1] != s[i]) and (i + k == len(s) or s[i + k] != s[i]):
                return True  # 🎯 Found a valid special substring

        return False  # ❌ No valid substring found
