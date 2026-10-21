class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        out = 0
        vowels = set('aeiou')

        for i in range(len(word) - 4):
            if (word[i] in vowels) and (word[i+1] in vowels) and (word[i+2] in vowels) and (word[i+3] in vowels) and (word[i+4] in vowels):
                seen = set(word[i:i+5])
                
                j = 4
                while (i+j < len(word)) and (word[i+j] in vowels):
                    seen.add(word[i+j])

                    if len(seen) == 5:
                        out += 1

                    j += 1


        return out

