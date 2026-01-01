// Last updated: 1/1/2026, 10:53:40 PM
int countNegatives(int** grid, int gridSize, int* gridColSize) {
    int c = 0;

    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridColSize[i]; j++) {
            if (grid[i][j] < 0) {
                c += gridColSize[i] - j;
                break;
            }
        }
    }
    return c;
}