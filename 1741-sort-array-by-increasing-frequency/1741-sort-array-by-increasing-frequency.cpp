class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {

        int n = nums.size();

        vector<int> freq(201, 0);

       
        for (int i = 0; i < n; i++) {
            freq[nums[i] + 100]++;
        }

        
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {

                if (freq[nums[j] + 100] > freq[nums[j + 1] + 100] ||
                   (freq[nums[j] + 100] == freq[nums[j + 1] + 100] &&
                    nums[j] < nums[j + 1])) {

                    swap(nums[j], nums[j + 1]);
                }
            }
        }

        return nums;
    }
};
