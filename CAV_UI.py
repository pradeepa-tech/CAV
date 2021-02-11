from tkinter import *

# root=Tk()
attack_specs={}
 # Value saved here

class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.entry = Entry(self)
        self.button = Button(self, text="Click to add the untrusted channel and specs", command=self.on_button)
        self.button.pack()
        self.entry.pack()

    def on_button(self):
        Temp=self.entry.get().split()
        attack_specs.update({Temp[0]:Temp[1]})
        self.entry.delete(0,"end")
        # variable1.append(self.entry.get())

app = SampleApp()
app.mainloop()
# def attack_specs():
# 	data=Entry(root, width=7)
# 	variable1.append(data.get())
# 	data.pack()

# root.bind('<Return>', attack_specs) 
# channel=Button(root,text="Click to add the untrusted channel",command=attack_specs)
# channel.pack()


# root.mainloop()
print(attack_specs)

