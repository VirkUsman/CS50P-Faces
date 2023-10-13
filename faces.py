text = input("")
emojis = {":)" : "🙂"  ,   ":(" : "🙁"  ,   ";)" : "😉"}
# Maker a dictionary for emojies

# print("Original Text : " + text) just for checking

for sign in emojis.keys():
    # keys() with get the only key values of dictionary of emojis
    text = text.replace(sign, emojis[sign])
    # replace function will replace the text sign with emojies dictionary key:value.

print(text)