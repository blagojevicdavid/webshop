import sqlite3 
  
connection = sqlite3.connect("database.db")   # povezuje se na bazu
crsr = connection.cursor()  #####
  
#sql_command = """CREATE TABLE sites (  id INTEGER PRIMARY KEY,  email VARCHAR(20),  link VARCHAR(50),  keywords CHAR(100),  pridruzen DATE);"""
#sql_command = """INSERT INTO sites VALUES (NULL, "mail", "dusansilni.srb", "mirko", "NULL");"""
#sql_command = """DELETE FROM sites"""
#sql_command = """SELECT * FROM sites"""
#crsr.execute(sql_command) 



# CREATE TABLE users ( id INTEGER PRIMARY KEY,  ime VARCHAR(25), prezime VARCHAR(30), email VARCHAR(40), brojtelefona VARCHAR(25), password VARCHAR(25), korpa VARCHAR(150), naruceno VARCHAR(150), zavrseno VARCHAR(200), datum DATE)

# INSERT INTO users VALUES (NULL, "David", "Blagojevic", "davidblagojevic7@gmail.com", "066498934", "password", NULL, NULL, NULL, "3.5.2020")

#([('ime', 'David'), ('prezime', 'Blagojevic'), ('registerEmail', 'davidblagojevic7@gmail.com'), ('brojTelefona', '066498934'), ('password', '12345678'), ('btn', 'Register')])

# CREATE TABLE products ( id INTEGER PRIMARY KEY, naziv VARCHAR(150), cijena VARCHAR(7), kratakopis VARCHAR(200), opis VARCHAR(1000), slike VARCHAR(600), opcional VARCHAR(100) )

# INSERT INTO products VALUES (NULL, 'Otpornik 100kOhm 100kom', '3', 'Otpornik 100kOhm 1% tolerancija', NULL, NULL, NULL  )



while True:
    #try:
    command = str(input('> '))

    crsr.execute(command)

    ans= crsr.fetchall()

    print(ans)

    connection.commit()  #cuva promjene
    #except:
     #   print('Invalid command')
  




connection.close() 