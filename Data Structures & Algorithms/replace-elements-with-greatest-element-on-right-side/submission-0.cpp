class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        for (int i=0; i<=arr.size(); i++) {
            int next_biggest=-1000;
            if (i+1 > arr.size()) {
                break;
            }
            for (int j=i+1; j<arr.size(); j++) {
                if (arr[j] > next_biggest) {
                    next_biggest = arr[j];

                }

            }
            arr[i] = next_biggest;
        }
        arr.back() = -1;

        return arr;
    }
};