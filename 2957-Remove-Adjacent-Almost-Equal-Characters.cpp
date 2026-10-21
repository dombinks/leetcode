class Solution {
public:
    int removeAlmostEqualCharacters(string word) {
        int ops = 0;

        for (int i = 0; i < (word.size() - 1); i++) {
            char a = word[i];
            char b = word[i+1];

            if (a - b <= 1 && a - b >= -1) {
                ops += 1;
                i++;
            }
        }

        return ops;
    }
};
