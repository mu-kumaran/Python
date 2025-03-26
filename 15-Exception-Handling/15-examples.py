# Tweet exception

try:
    tweet = input("Enter your tweet(below 10 characters):")
    if len(tweet) > 10:
        raise Exception("Tweet character length is more than 5")
    else:
        print(tweet)
except Exception as err:
    print("Error:",err)


try:
    tweet = input("Enter your tweet not more than 140 characters):")
    if len(tweet) > 140:
        raise Exception("Tweet character length is more than 140")
    elif 'tweet' in tweet.lower():
        raise Exception("Tweet has the word 'tweet' in it")
except Exception as err:
    print("Error:",err)
