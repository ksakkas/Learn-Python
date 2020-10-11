# Κλάσεις στην Python

class mclass:    # Δημιουργία κλάσης με όνομα mclass
    x = 5        

p1 = mclass()    # Δημιουργήστε ένα αντικείμενο με το όνομα p1 και εκτυπώστε την τιμή του x
print(p1.x)   

print("--------------------")

class Person:
    def __init__(self, name, age):     # Η συνάρτηση __init __ () καλείται αυτόματα κάθε φορά που η κλάση χρησιμοποιείται για τη δημιουργία ενός νέου αντικειμένου.
                                       # Αντιστοιχίσετε τιμές για το όνομα και την ηλικία
        self.name = name
        self.age = age

p1 = Person("Kostas", 21)

print(p1.name)
print(p1.age)



