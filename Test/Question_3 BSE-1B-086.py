def main():
    set1 = {1,2,3,4,5}
    set2 = {5,6,7,8,9}
    final_val= Union(set1,set2)
    print(final_val)
def Union(set1,set2): 
    finalset=[]
    for i in (set1):
        for j in (set2):
            if i in set1 and i in set2 and j in set1 and j in set2:
                finalset.append(i)
    return finalset
main()