class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        subs = []
        for i in range(len(words)):
            word = words[i]
            words[i] = ""
            for j in range(len(words)):
                if word in words[j]:
                    if word not in subs:
                        subs.append(word)
            words[i] = word
        return subs