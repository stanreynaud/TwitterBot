from nltk.corpus import wordnet as wn
from PIL import Image
from twython import Twython
import random
import emojis
import string
import time
import erysf as e

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
    
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def usernames(s):
    pos=0
    res=""
    while pos<len(s):
        if s[pos] == "@":
            start = pos
            pos+=1
            res=res+"@"
            while pos < len(s) and s[pos]!="\\" and (s[pos].isalpha() or s[pos]=="_"):
                res=res+s[pos]
                pos+=1
                

            res=res+" "
            return res
        else:
            pos=pos+1
    return res


nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}
verbs = {x.name().split('.', 1)[0] for x in wn.all_synsets('v')}
#adv = {x.name().split('.', 1)[0] for x in wn.all_synsets('a')}


foll = twitter.get_followers_ids()
for followers_ids in foll['ids']:
    #twitter.create_friendship(user_id=followers_ids)
    break

search = ["e","a"]#["e","tech","SPBbotmin","ShitpostBot 5000","stupid","reply","algorithm","weird","crazy","strange","InspiroBot","bot","robot","edgy","programming","python","deep learning","ai","computer","information technology"]
lanng = ["en","en","eu","fr","eu"]
query = {'q': random.choice(search),
        'result_type': 'mixed',
        'lang': 'eu',
        'count': random.randint(1,50),
        'lang': random.choice(lanng),
        }



while(True):




    query = {'q': random.choice(search),
            'result_type': 'mixed',
            'lang': 'eu',
            'count': random.randint(1,50),
            'lang': random.choice(lanng),
            }
    tweets={}

    for status in twitter.search(**query)['statuses']:
        if True:#int(status['favorite_count'])>= 500:
            #print(status['created_at'])
            #print(status['in_reply_to_screen_name'])
            
            tweets[status['in_reply_to_status_id']] = (status['text'].encode('utf-8'))


    while list(tweets.keys()) == []:
        print("finding correct one")
        tweets={}


        query = {'q': random.choice(search),
                'result_type': 'mixed',
                'lang': 'eu',
                'count': random.randint(1,50),
                'lang': random.choice(lanng),
                }

        
        for status in twitter.search(**query)['statuses']:
            if True:#int(status['favorite_count'])>= 500:
                #print(status['created_at'])
                #print(status['in_reply_to_screen_name'])
                
                tweets[status['in_reply_to_status_id']] = (status['text'].encode('utf-8'))
        reply_id=random.choice(list(tweets.keys()))
        text = tweets[reply_id]

    reply_id=random.choice(list(tweets.keys()))
    text = tweets[reply_id]
    
    #print(text,reply_id)

    mynouns=set()
    myverbs=set()

    splited = text.split()


    for word in splited:
        nounfound=False
        for xnoun in nouns:
            if len(xnoun) >= 4:
                if xnoun.replace("_"," ") in str(word).lower():
                    mynouns.add(xnoun.replace("_"," "))

        
        for xverb in verbs:
            if len(xverb) >= 2:
                if xverb.replace("_"," ") in str(word).lower():
                    myverbs.add(xverb.replace("_"," "))

    me = ["I","","","Me","Me would","Me want to","I want to","I'd","I have to","I will"]
    your = ["some","some of that","this","the","","your","that","my","his","her","its","those","these","their","our"]

    if len(myverbs)!= 0:
        chosev= random.choice(list(myverbs))
    else:
        chosev = random.choice(list(verbs)).replace("_"," ")

    if len((mynouns)-{chosev})!= 0:
        chosen= random.choice(list((mynouns)-{chosev}))
    else:
        chosen = random.choice(list(nouns)).replace("_"," ")

    chosei=random.choice(me)
    chosey=random.choice(your)

    if chosev=="go":
        chosev=chosev+" to"

    if chosen=="hank":
        chosen= random.choice(["leg","egg","ham","elk","boy","suffering"])


    if chosev=="be" and chosei=="I":
        chosev="am"

    if chosey == "":
        sentence=chosei+" "+chosev+" "+chosen
    else:
        sentence=chosei+" "+chosev+" "+chosey+" "+chosen


    #print(myverbs,mynouns)
    if chosey is "those" or chosey is "these" or chosey is "their" or chosey is "our" or chosey is "some":
        sentence=sentence+"s"

    if random.randint(1,100) <= 25:
        sentence = sentence+" ?"

    emoj = random.randint(0,3)
    sentence=sentence+' '
    while emoj !=0:
        emoji1 = random.choice(list(emojis.db.get_emoji_aliases().keys()))
        sentence = emojis.encode(sentence+emoji1)
        emoj=emoj-1

    #sentence= usernames(str(text))+" "+sentence
    #twitter.update_status(status=sentence)
    x=300
    y=150
    canvas = Image.new("RGBA", (x,y), e.f(0,x,y,x,y))
    e.rectanglesclean(canvas)
    canvas.resize((1800, 900), Image.ANTIALIAS).save("image.jpg", format="png")

    image = open('image.png', 'rb')
    response = twitter.upload_media(media=image)
    media_id = [response['media_id']]



    if random.randint(0,50) == 10:
        followers=[]
        r = twitter.get_followers_list()
        for follower in r["users"]:
            followers.append(str(follower["screen_name"]))
            break
        sentence = sentence+"\nThank you my "+random.choice(list(nouns)).replace("_"," ")+" @"+str(followers[0])+" realest "+random.choice(list(nouns)).replace("_"," ")+" I know"
        

    twitter.update_status(status=sentence,media_ids=media_id,in_reply_to_status_id=reply_id,auto_populate_reply_metadata=True)
    wait=random.randint(20,5*60)
    print("sent : "+usernames(str(text)),wait,"\n",text,"\n",mynouns,myverbs)
    time.sleep(wait)
