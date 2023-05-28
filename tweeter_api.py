import tweepy

auth = tweepy.OAuthHandler('1Pw8Gzo24n59j1zB3gcYTPBsL', 'KH1cd0KiBT1BfHRH70nhBZBMnbf6JLJ2NRuwXcem0AkhNhHerQ')
auth.set_access_token('1566088478160744448-pqMweB6iLBbmrHD81OpOHfiAae0xqk', 'C6JFS9lYtgbOCR788cLJ2NM9Vt8z4V467D4G62FtYot5R')

api = tweepy.API(auth)

user = api.me()
print(user.name)