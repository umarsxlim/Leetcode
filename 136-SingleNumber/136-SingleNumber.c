// Last updated: 1/5/2026, 11:48:18 PM
int singleNumber(int* nums, int numsSize) {
    int res = 0;

    for (int i = 0; i < numsSize; i++) {
        res ^= nums[i];
    }
    return res;
}