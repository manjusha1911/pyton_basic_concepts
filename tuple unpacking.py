# t=("Sai","Ram","Krishna")
# (Manjusha,nany,honey,vasu)=t
# print(Manjusha)
# print(nany)
# print(honey)
# # print(vasu) error


t=("Sai","Ram","Krishna","saibaba","jaisree ram","harhar mahadev")
(Manjusha,nany,*honey,vasu)=t
print(Manjusha)
print(nany)
print(honey)
print(vasu)

'''
Sai
Ram
['Krishna', 'saibaba', 'jaisree ram']
harhar mahadev
'''

t = ("apple", "banana", "cherry")
i=0
while i<len(t):
    print(t[i])
    i+=1

t = ("apple", "banana", "cherry")
for i in t:
    print(i)