text = input("")
emojis = {":)" : "🙂"  ,   ":(" : "🙁"  ,   ";)" : "😉"}


for sign in emojis.keys():

    text = text.replace(sign, emojis[sign])
   

print(text)