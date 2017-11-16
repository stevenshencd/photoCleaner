from Tkinter import *
import tkFileDialog
import fileOperator

def btnCleanClicked():
    f = fileOperator.fileOperator(entryPath.get())
    txtContent.insert(END,f.clean())
def btnDelClicked():
    print "Del click"

def btnBrowseClicked():
    path = tkFileDialog.askdirectory(initialdir='C:/')
    entryPath.delete(0, END)
    entryPath.insert(0, path)

# Define GUI appearance
root = Tk()
root.title("Copy processed raw data to processed folder")


btnClean = Button(root, text = "Clean", relief = GROOVE, command = btnCleanClicked)
btnClean.grid(row = 0, column = 0, sticky = W + E)
btnDel = Button(root, text = "Delete", relief = GROOVE, command = btnDelClicked)
btnDel.grid(row = 0, column = 1, sticky = W + E)
labelPath = Label(root, text = "Folder:")
labelPath.grid (row = 1, column = 0, sticky = W)
entryPath = Entry(root, relief = FLAT)
entryPath.grid(row = 1, column = 1, columnspan = 2, sticky = W + E)
btnBrowse = Button(root, text = "Browse", relief = GROOVE, command = btnBrowseClicked)
btnBrowse.grid(row = 1, column = 3, sticky = W + E)
txtContent = Text(root, relief = FLAT)
txtContent.grid(row = 2, column = 0, columnspan = 4, sticky = W + E + N + S)

root.mainloop()
