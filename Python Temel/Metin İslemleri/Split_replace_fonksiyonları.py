# -*- coding: utf-8 -*-

#Substring 

message = "Insert to new Table" 

message_sub = message[2:14]
print ("message stringinin 2. elemanından 14.elemanına kadar olan harfler = " + message_sub)

message_sub_2 = message[:14]
print ("message stringinin 14.elemanına kadar olan karakterler = " + message_sub_2)

message_sub_3 = message[14:]
print ("message stiringinin 14.elemandan sonra olan karakterleri = " + message_sub_3)

#Len

message_len = len(message)
message[len(message)-1:len(message)]
print ("message stringinin son karakteri = " + message[len(message)-1:len(message)])

print(type(len(message)))
lenght = len(message)
print (len(message))
print (lenght)

print (message[lenght-1 :lenght])

#Replace ile metin değiştirme 

message_replace = message.replace("I","i")
print(message_replace)

message_replace_2 = message.replace("t","g")
print(message_replace_2)


#Split ve Strip ile metinkleri parçalama

message_split = message.split()
print(message_split)

message_split_2 = message.split()[2]
print(message_split_2)

#to :D
messags = ["İnsert" ,"to" ,"new" ,"Table"]
print(type(messags))

message = "Insert to new Table" 
print(type(message)) #str

message_replace_split = message.replace(" ",";")
print(type(message_replace_split)) #str

liste = list(message_replace_split.split(";"))
liste.append("DJ ferdi özkan iyi uçuşlar diler ")

print(liste)

message_replace_split = message_replace_split.split(";")
print(type(message_replace_split))
print (message_replace_split)

message_replace_split.append("Ahmet")
print (message_replace_split)
#message_replace_split  sonuna ";" dizisi eklemeyidene 
#print(message_replace_split)
#
#print(message_replace_split(";")[1])