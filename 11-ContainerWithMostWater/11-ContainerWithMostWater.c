// Last updated: 1/6/2026, 5:34:04 PM
int maxArea(int* height, int heightSize) {
    int left = 0;
    int right = heightSize - 1;
    int max_area = 0;

    while (left <= right) { 
        int width = right - left;
        int length;
        
        if (height[right] <= height[left]) {
            length = height[right];
            right--;
        }
        else {
            length = height[left];
            left++;
        }

        int area = length * width;

        if (area >= max_area) {
            max_area = area;
        }
    }

    return max_area;
}