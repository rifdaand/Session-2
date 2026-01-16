user= input ("Pilih Gunting/Batu/Kertas "  ).lower().strip()
print ("Kamu memilih "  + user )

import random
komputer = ["gunting","batu","kertas"]
pilihan_acak= random.choice(komputer)
print ("Komputer memilih " + pilihan_acak )

#Kondisi seri
if pilihan_acak == user:
    print ("hasil seri")

#user menang
elif ( user == "batu" and pilihan_acak == "gunting" ) or \
    ( user == "gunting" and pilihan_acak == "kertas" ) or \
    ( user == "kertas" and pilihan_acak == "batu" ):
    print ("kamu menang")

#user kalah
else:
    print ("kamu kalah")
