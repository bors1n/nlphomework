import numpy as np
def tf(sent, word):
        return sent.count(word) / len(sent)

def idf(word, dict_w):
        return np.log10(len(corpus) / dict_w[word])

N = int(input())
corpus = []
for i in range(N):
  sentenses = input().split()[1:]
  corpus.append(sentenses)

word_dict = {}
W = int(input())
for i in range(W):
  s = input().split()
  word_dict[s[0]] = s[1]


K = int(input())
req_all = []
req_all_ = []
for i in range(K):
  req = list(input().split()[1:])
  req_ = list(set((req)))
  req_all.append(req)
  req_all_.append(req_)


word_set = list(word_dict.keys())
word_count = {}
corpus = np.array(corpus)
for word in word_set:
        word_count[word] = 0
        for sent in corpus:
                if word in sent:
                        word_count[word] += 1
words_tfidf = {}
for i in range(len(req_all_)):
        words_tfidf = {}
        sen = req_all[i]
        for j in range(len(req_all_[i])):
                word_ = req_all_[i][j]
                tfidf = tf(sen, word_) * idf(word_, word_count)
                words_tfidf[word_] = tfidf
        print(len(words_tfidf))
        for k in word_dict.keys():
                if k in words_tfidf.keys():
                        print(int(word_dict[k]), words_tfidf[k])
                else:
                        continue



