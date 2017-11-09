import sys

def sentiment_words_input(words):
  scores = {}
  for line in words:
    l = line.lower()
    term, score = l.split("\t")
    scores[term] = int(score)
  return scores

def tweets_seperator(dataset):
  tweets = []
  for line in dataset:
    l = line.lower()
    sample = l.split("\t")
    tweets.append(sample[2])
  return tweets

def result(p,n):
  if p == n:
    print "Neutral"
  elif p > n:
    print "Positive"
  else:
    print "Negative"

def analysis(tweet_text,scores):
  positive = 0
  negative = 0
  for tweet in tweet_text:
    sentiment = 0
    parts = tweet.split()
    for p in parts:
      if scores.has_key(p):
        sentiment += scores[p]
    if sentiment > 0:
      positive+=1
    elif sentiment < 0:
      negative+=1
  result(positive,negative)

words = open(sys.argv[1])
tweets = open(sys.argv[2])

scores = {}
tweet_text = []

scores = sentiment_words_input(words)

tweet_text = tweets_seperator(tweets)

analysis(tweet_text,scores)
