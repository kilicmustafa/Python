#Set union A birleşim B

SetA = {1,2,3,4,5,7,15,27}
SetB = {5,6,7,8,9,10,1,3}

print("------------- A birkleşim B ---------------")
print(SetA | SetB)

SetC = SetA.union(SetB)  # Set bir ile set iki yi birlerştirip ortak elemanları bir kez yazar 
print(SetC)



print("---------------A kesişim B-----------------")
# Set intersection A kesişim B

print(SetA & SetB)
SetD = SetA.intersection(SetB)
print(SetD)

print("---------------- A fark B ve B fark A ---------------------")
#difference A fark B veya B fark A

print(SetA - SetB)
print(SetB - SetA)
print(SetA.difference(SetB))
print(SetB.difference(SetA))


#smetric 
print("----------------A fark B ile B fark A nın birleşimi yani kesişim hariç hepsi --------------------")
print(SetA ^ SetB)
print(SetA.symmetric_difference(SetB))




print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#union 

print(SetA.union(SetB))
print(SetA | SetB)

#intersection

print(SetA.intersection(SetB))
print(SetA & SetB)

#difference

print(SetA.difference(SetB))
print(SetB.difference(SetA))
print(SetA - SetB)
print(SetB - SetA)

# symmetric_difference

print(SetA.symmetric_difference(SetB))
print(SetB.symmetric_difference(SetA))

print(SetA ^ SetB)
