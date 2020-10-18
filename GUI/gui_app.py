import tkinter
from tkinter import font as tkFont  # for convenience


class myapp_tk(tkinter.Tk):           # tkinter.Tk : βασική κλάση για πρότυπα       
    def __init__(self, parent):       # δήλωση συνάρτησης κατασκευαστή
        tkinter.Tk.__init__(self, parent)     #tkinter.Tk:  κατασκευαστής 
        self.parent = parent          #αναφορά γονέα
        self.initialize()             #μέθοδος δημιουργίας widget

    def initialize(self):        
        helv36 = tkFont.Font(family='Helvetica', size=16, weight='bold')

        self.grid()     #χρήση παραθύρου 216
    
        self.geometry('400x150')
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self, textvariable=self.entryVariable) #δημιουργία widget
        self.entry['font']=helv36
        self.entry.grid(column=0,row=0,sticky="EW") #εισαγωγή κειμένου 
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set("Δώστε κείμενο....")
        


        button = tkinter.Button(self, text="κλικ", command=self.OnButtonClick, width = 10)     #Κουμπί
        button['font']=helv36
        button.grid(column=1,row=0)               # θέση κουμπιού

        self.labelVariable = tkinter.StringVar()    #tkinter μεταβλητή για δέσμευση
        label = tkinter.Label(self, textvariable=self.labelVariable,anchor="w", fg="#ffffff", bg="#990033", font="50") #ετικέτα προς εμφάνιση κειμένου
        label.grid(column=0,row=1,columnspan=2,sticky="EW") 
        self.labelVariable.set("Hiii...")

        self.grid_columnconfigure(0, weight=1)   #προσαρμογή ανάλογα με το μέγεθος του παραθύρου
        self.resizable(True, False)      #σταθερό ύψος, μεταβαλλόμενο πλάτος
        self.entry.focus_set()           #focus το στοιχείο
        self.entry.selection_range(0, tkinter.END)  #επιλογή των δεδομένων του
        

    def OnButtonClick(self):
        self.labelVariable.set(self.entryVariable.get() + " Πατήσατε το κουμπί")
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)


    def OnPressEnter(self, event):
        self.labelVariable.set(self.entryVariable.get() + " Πατήσατε το Enter") 
        self.entry.focus_set()        
        self.entry.selection_range(0, tkinter.END)

        
        

if __name__=="__main__":      #δημιουργία κύριας συνάρτησης
    app = myapp_tk(None)      #απο το tkinter
    app.title("Ksakkas application") #τίτλος για την εφαρμογή
    app.mainloop()   #τρέχει μέχρι να γίνει κάποια ενέργεια