class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        var result;
        result = [...nums, ...nums];
        
        return result;
    }
}
