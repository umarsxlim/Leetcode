// Last updated: 1/1/2026, 10:53:34 PM
int maximumWealth(int** accounts, int accountsSize, int* accountsColSize) {
    int wealthiest = 0;
    int wealth = 0;

    for (int i = 0; i < accountsSize; i++) {
        for (int j = 0; j < accountsColSize[i]; j++) {
            wealth += accounts[i][j];
        }
        if (wealth >= wealthiest) {
                wealthiest = wealth;
                wealth = 0;
        }
        else {
            wealth = 0;
        }
    }
    return wealthiest;
}