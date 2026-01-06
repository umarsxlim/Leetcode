// Last updated: 1/6/2026, 5:33:58 PM
void moveZeroes(int* nums, int numsSize) {
    int left = 0;

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != 0) {
            int temp = nums[left];
            nums[left] = nums[i];
            nums[i] = temp;
            left += 1;
        }
    }
}