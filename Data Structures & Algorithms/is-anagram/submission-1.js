class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length != t.length) return false;

        var intArray = new Array(126).fill(0);
        for (var i = 0; i < s.length; i++) {
            intArray[s.charCodeAt(i)]++;
            intArray[t.charCodeAt(i)]--;
        }

        return intArray.every(x => x == 0);
    }
}
