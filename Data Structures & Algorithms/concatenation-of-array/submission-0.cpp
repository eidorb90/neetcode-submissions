class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        std::vector<int> ans;
        size_t length = nums.size();
        for (int i=0; i <= length*2-1; i++) {
            ans.push_back(nums[i%length]);
        }
        return ans;
    }
};