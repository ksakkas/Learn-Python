# Πίνακες στην Python

dit = ["Department", "Informatics", "Telecomunication"]

x = dit[0]
print (x)

dit[1] = "UOI"
y = dit[1]
print (y)

x = len(dit)   # Επιστρέψτε τον αριθμό των στοιχείων 

dit.append("department")     # Προσθέστε ένα ακόμη στοιχείο
r = dit[3]
print (r)

dit.pop(3)    # Μπορείτε να χρησιμοποιήσετε τη μέθοδο pop () για να αφαιρέσετε ένα στοιχείο από τον πίνακα

print("----------------------")
for q in dit:
    print (q)

dit.remove("UOI")  # Μπορείτε επίσης να χρησιμοποιήσετε τη μέθοδο κατάργησης () για να αφαιρέσετε ένα στοιχείο από τον πίνακα
