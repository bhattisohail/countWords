# def count_words(str):
#     str = str.lower()
#     str1 = str.split()
#     d={}
#     for i in str1:
#         d[i] = d.get(i,0)+1,mn p5 .
#     for w in sorted(d, key=d.get, reverse=True):
#         print(w, d[w])

# str = input("Enter a string: ")
# count_words(str)

def count_words(str):
    str = str.lower()
    str_1 = str.split()
    d={}
    for i in str_1:
        d[i]=d.get(i,0)+1
    print(d)
    for w in sorted(d, key=d.get, reverse=True):
        print(w, d[w])

str=input("Enter a string: ")
count_words(str)
