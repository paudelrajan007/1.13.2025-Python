words=[]
for i in range(6):
    word=str(input(f"Write the word {i +1 }:"))
    words.append(word)
print("Before sorting words are in the list of :\t",words)
sord=sorted(words)
print("After sorting words are in the list of :",sord)
while True:
        delete=str(input("Enter the words you want to delete : (or if you want to end the loop enter -1 ) :"))
        if delete == -1:
              break
        if delete in sord :
         sord.remove(delete)
         print(f"{delete}has been removed from the list :",sord)
         print("Updated list is :",sord)
        else:
             print("WORDS ARE NOT IN THE LIST 'THANK YOU ':")