from Tkinter import *
import fileOperator

def btnCleanClicked():
    print entryPath.get()
    f = fileOperator.fileOperator(entryPath.get())
    txtContent.insert(END,f.clean())

def btnDelClicked():
    print "Del click"

def btnBrowseClicked():
    print "Del click"

# Define GUI appearance
root = Tk()
root.title("Copy processed raw data to processed folder")

btnClean = Button(root, text = "Clean", command = btnCleanClicked)
btnClean.grid(row = 0, column = 0)
btnDel = Button(root, text = "Delete", command = btnDelClicked)
btnDel.grid(row = 0, column = 1, sticky = W)
labelPath = Label(root, text = "Directory")
labelPath.grid (row = 1, column = 0)
entryPath = Entry(root)
entryPath.grid(row = 1, column = 1)
btnBrowse = Button(root, text = "Browse", command = btnBrowseClicked)
btnBrowse.grid(row = 1, column = 3)
txtContent = Text(root)
txtContent.grid(row = 2, column = 0)

root.mainloop()
