from googlesearch import search

print("Welcome to google search")

#Take query

query = input("What do you want to searchon google?")

for i in search(query,start=0,stop=10) :
    print(i)