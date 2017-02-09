''' This program performs a sentiment analysis on tweets
    and ranks states by score, returning the "happiest state". 
'''

import sys
import json
import codecs

# You provide the sentiment rank and the Twitter feed files. 
def hw(sent_file,tweet_file):
    scores = {} 
    for line in sent_file:
       term, score  = line.split("\t")  
       scores[term] = int(score)

    statecodes = ['AL', 'AK', 'AS', 'AZ', 'AR', \
                  'CA', 'CO', 'CT', 'DE', 'DC', \
                  'FM', 'FL', 'GA', 'HI', 'ID', \
                  'IL', 'IN', 'IA', 'KS', 'KY', \
                  'LA', 'ME', 'MD', 'MA', 'MI', \
                  'MN', 'MO', 'MT', 'NE', 'NV', \
                  'NH', 'NJ', 'NM', 'NY', 'NC', \
                  'ND', 'OH', 'OK', 'OR', 'PA', \
                  'RI', 'SC', 'SD', 'TN', 'TX', \
                  'UT', 'VT', 'VA', 'WA', 'WV', \
                  'WI', 'WY']  

    states = dict.fromkeys(statecodes,0)

  
    for line in tweet_file:
        pyresponse = json.loads(line)
        if pyresponse.keys()[0] == "delete":
	    continue
        if pyresponse["place"] == None:
            continue
        elif pyresponse["place"]["country"] == "United States":
            location = ( pyresponse["place"]["full_name"]).split(",")
            state = location[1].replace(' ', '')
            if state in statecodes:
                tweet = pyresponse["text"]
                wordlist = tweet.split()
                sum = 0
                keys = scores.keys()
                for word in wordlist:
                    actual = word.encode('utf-8')
                    if keys.count(actual):
                       sum += scores[actual]
                freq = states[state] + sum
                states[state] = freq
    finlist = sorted(states, key = states.get, reverse=True)
    print finlist[0]

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file,tweet_file)

if __name__ == '__main__':
    main()
