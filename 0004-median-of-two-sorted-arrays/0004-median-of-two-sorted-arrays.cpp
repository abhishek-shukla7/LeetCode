class Solution {
public:
    double findMedianSortedArrays(vector<int>& A, vector<int>& B) {
        int m = A.size(), n = B.size();
        // Ensure A is the smaller array
        if (m > n) return findMedianSortedArrays(B, A);
        int lo = 0, hi = m, half = (m + n + 1) / 2;
        while (lo <= hi) {
            int i = (lo + hi) / 2;
            int j = half - i;
            double Aleft  = (i == 0 ? INT_MIN : A[i - 1]);
            double Aright = (i == m ? INT_MAX : A[i]);
            double Bleft  = (j == 0 ? INT_MIN : B[j - 1]);
            double Bright = (j == n ? INT_MAX : B[j]);

            if (Aleft <= Bright && Bleft <= Aright) {
                if ((m + n) % 2) {
                    return max(Aleft, Bleft);
                } else {
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0;
                }
            } else if (Aleft > Bright) {
                hi = i - 1;
            } else {
                lo = i + 1;
            }
        }
        return 0.0; // should never reach here
    }
};
