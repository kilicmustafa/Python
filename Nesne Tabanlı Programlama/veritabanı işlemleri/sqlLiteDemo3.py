#import sqlite3
#    connection = sqlite3.connect("chinook.db")
#    connection.execute("""insert into customers
#                       (firsName,lastName,city,email) 
#                       values ('Mustafa' ,'kilic' ,'erzincan' ,'kilicmustafa.tr@gmail.com') """)
#    connection.commit()
#    connection.close()

#import sqlite3
#connection = sqlite3.connect("chinook.db")
#connection.execute("""insert into customers
#                   (firstName ,lastName ,city ,email) 
#                values('Mustafa' ,'Kılıç' ,'Erzincan' ,'kilicmustafa.tr@gmail.com')""")
#connection.commit()
#connection.close()


#import sqlite3
#connection = sqlite3.connect("chinook.db")
#connection.execute("""update customers set City='alanya' 
#                   where City='Erzincan' """)
#connection.commit()
#connection.close()


#import sqlite3
#connection = sqlite3.connect("chinook.db")
#connection.execute(""" delete from customers 
#                   where city = 'alanya' """)
#connection.commit()
#connection.close()



import sqlite3
connection = sqlite3.connect("chinook.db")
a = connection.execute("""SELECT artists.Name,albums.Title FROM artists INNER JOIN albums
on albums.AlbumId = artists.ArtistId """)
for row in a:
    print("\n")
    print(row)
    print("*********************")
connection.commit()
connection.close()