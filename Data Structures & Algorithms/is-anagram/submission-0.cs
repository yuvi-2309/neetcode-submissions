public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) return false;

        var charInt = new int[126];
        for (var i = 0; i < s.Length; i++) {
            charInt[s[i]]++;
            charInt[t[i]]--;
        }

        foreach (var integer in charInt) {
            if (integer != 0) return false;
        }

        return true;
    }
}
