class Solution():
    def maxScoreWords(self, words, letters, score):

        self.ans = 0
        words_score = {}
        words_counter = {}
        for word in words:
            words_score[word] = sum(score[ord(c) - ord('a')] for c in word )
            words_counter[word] = Couter(word)
       
        def dfs(idx,cur_score, cur_counter):
            self.ans = max(self.ans,cur_score)
            for i,word in enumerate(words[idx:]):
                flag = True
                for key in words_counter[word].keys():
                    if key not in cur_counter or words_counter[word][key]<cur_counter[key]:
                        flag = False
                        break 
                if flag:
                    dfs(i+idx,curr_score+words_score[word],cur_counter-words_counter[word])



        
        dfs(0, 0,Counter(letters))
        return self.ans