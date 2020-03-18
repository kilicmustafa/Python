#%%
    import sqlite3
    connection = sqlite3.connect("chinook.db")
    
    cursor = connection.execute("select * from customers where FirstName = 'Leonie' ")
    
    print(cursor)
    
    for row in cursor:
        print(row)
    
    
    
    
#%%
    import sqlite3
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute("""select * from customers where  FirstName = 'Leonie' 
                                order by city""")
    
    for row in cursor:
        print(row)
        
        
        
    #%%
    import sqlite3
    connection = sqlite3.connect("chinook.db")
    
    cursor = connection.execute("select * from customers where FirstName = 'Leonie' ")
    
    for row in cursor:
        print(row)
        
        
    #%%
    import sqlite3
    connection = sqlite3.connect("chinook.db")
    
    cursor = connection.execute("""select city,count(*) from customers 
                                group by city having count(*)>1
                                order by count(*) desc""")
    

#%%
    import sqlite3
    coonetion = sqlite3.connect("chinook.db")
    cursor = connection.execute("""select  city,count(*) from customers 
                                group by city having count(*)>1
                                order by count(*) desc""")
#%%
    import sqlite3
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute("""select * from customers
                                where FirstName like "%a" """)




#%% 
    import sqlite3
    connection = sqlite3.connect("chinook.db")
    connection.execute("""insert into customers
                       (firstName ,lastName ,city ,email) 
                    values('Mustafa' ,'Kılıç' ,'Erzincan' ,'kilicmustafa.tr@gmail.com')""")
    connection.commit()
    connection.close()