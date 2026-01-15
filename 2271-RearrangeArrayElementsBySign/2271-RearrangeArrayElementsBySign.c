// Last updated: 1/15/2026, 9:29:36 PM
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* rearrangeArray(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;

    int *res = malloc(numsSize * sizeof(int));

    int posindex = 0;
    int negindex = 1;

    int i = 0;
    while (i < numsSize) {
        if (nums[i] > 0) {
            res[posindex] = nums[i];
            posindex += 2;
        } else {
            res[negindex] = nums[i];
            negindex += 2;
        }
        i++;
    }

    return res;
}