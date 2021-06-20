from tkinter import *
#import database db module
#from db import Database class
from db import Database

#import messagebox library from tkinter
from tkinter import messagebox

#now here we will instanciate the db object
#it will create the table if not already present
db = Database('store.db')

#here are all the functions that will handle all the backend of our application

#this function is responsible for actually getting the data from the database
def populate_list():
    print("populate")
    #this will delete any previously stored information in our listBox
    parts_list.delete(0, END)
    # db.fetch() = def fetch(self): function inside our db.py module and we are accessing that using db object in this module
    #so here in this for loop we are going to loop through all the rows of our table and populate our listBox
    #beacause we know def fetch(self): is returning rows in db.py module
    part_name = ''
    customer_name = ''
    retailer_name = ''
    prince_rs = ''
    list_text = ''
    for row in db.fetch():
        #END = the new info will be inserted at the end of the list box
        #tnd the things we are inserting will be the row returned by the fetch() method
        print(row)
        parts_list.insert(END, row)

def add_item():
    print("add")
    #check if the input fields are empty or not is yest then do not add anything into the database
    if part_entry.get()== "" or customer_entry.get()=="" or Retailer_entry.get() == "" or Price_entry.get() == "":
        messagebox.showerror("Required Fields", "Input Fields are NULL!")
        return
    #inseting data into the database
    db.insert(part_entry.get(),customer_entry.get(),Retailer_entry.get(),Price_entry.get())
    # this will delete any previously stored information in our listBox
    parts_list.delete(0, END)
    parts_list.insert(END,(part_entry.get(),customer_entry.get(),Retailer_entry.get(),Price_entry.get()))
    #clearing the input fields of our application
    clear_input()
    populate_list()

#now here the remove function will be a little bit different
#we want to select the record that we want to remove and press remove button to remove it
#so here before remove_item(): function we will be requiring a select_item function to add select record function
#from our list box widget in tkinter
#basically we will binding our listBox to this
def select_item(event):
    print("Select Item")
    try:
        global selected_item
        #now we will be getting the index of the selected item in the listBox
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)
        print(selected_item)
        #here we will put the selected_item data into the input Fiedls
        #but before we put in the data related to our selected_item data we need to remove anything present int the input fields
        clear_input()
        # inserting the selected record details from the lisBox widget to our input Fields
        part_entry.insert(END, selected_item[1])
        customer_entry.insert(END, selected_item[2])
        Retailer_entry.insert(END, selected_item[3])
        Price_entry.insert(END, selected_item[4])
    except IndexError:
        pass

def remove_item():
    print("remove")
    db.remove(selected_item[0])
    #clearing the input fields after delete operation
    clear_input()
    populate_list()

def update_item():
    print("update")
    # check if the input fields are empty or not is yest then do not add anything into the database
    if part_entry.get() == "" or customer_entry.get() == "" or Retailer_entry.get() == "" or Price_entry.get() == "":
        messagebox.showerror("Required Fields", "Input Fields are NULL!")
        return
    db.update(selected_item[0], part_entry.get(),customer_entry.get(),Retailer_entry.get(),Price_entry.get())
    populate_list()

def clear_input():
    print("clear")
    #clearing the information present in the input fields of the application
    part_entry.delete(0,END)
    customer_entry.delete(0,END)
    Retailer_entry.delete(0,END)
    Price_entry.delete(0,END)

#here this function will pop up a message box containing the information related to the developer of this software
def Dev_info():
    messagebox.showinfo("Developer Info", "Name = Aditya Kumar" +"\n"+ "Roll_no = 1901230100001" +"\n"+ "Course = B.tech" +"\n"+ "Branch = Computer Science" +"\n"+ "College Code = 123")

#app variable will allow us to create a window
#app = window object
app = Tk()
#setting up the window titile
app.title("Part manager")
#setting up the window size on first boot
app.geometry("700x550")

# setting up the minimum size and maximum size for the application window
# set minimum window size value
app.minsize(700, 550)

# set maximum window size value
app.maxsize(700, 550)

#creating the input field for the user where the user will insert the details related to a particular computer part

#part name input field
#textView
part_text = StringVar()
part_label = Label(app, text="Part Name", font = ("bold",14),pady=20)
part_label.grid(row=0,column=0,sticky=W)

#EditText
#textvariable = part_text where part_text is a string so textvariable will also be a string
part_entry = Entry(app,textvariable = part_text)
part_entry.grid(row=0,column=1)

#customer input field
#textView
customer_text = StringVar()
customer_label = Label(app, text="Customer", font = ("bold",14))
customer_label.grid(row=0,column=2,sticky=W)

#EditText
#textvariable = customer_text where part_text is a string so textvariable will also be a string
customer_entry = Entry(app,textvariable = customer_text)
customer_entry.grid(row=0,column=3)

#Retailer input field
#textView
Retailer_text = StringVar()
Retailer_label = Label(app, text="Retailer", font = ("bold",14))
Retailer_label.grid(row=1,column=0,sticky=W)

#EditText
#textvariable = Retailer_text where part_text is a string so textvariable will also be a string
Retailer_entry = Entry(app,textvariable = Retailer_text)
Retailer_entry.grid(row=1,column=1)

#Price input field
#textView
Price_text = StringVar()
Price_label = Label(app, text="Price", font = ("bold",14))
Price_label.grid(row=1,column=2,sticky=W)

#EditText
#textvariable = part_text where part_text is a string so textvariable will also be a string
Price_entry = Entry(app,textvariable = Price_text)
Price_entry.grid(row=1,column=3)

#now here we are creating a listBox widget which will show the list of computer parts
#border =0 will create a border less listbox tkinter widget height=10 , width=50
parts_list = Listbox(app,border=0)
parts_list.grid(row=3,column=0,columnspan=4,rowspan=6,padx=10,pady=10, sticky = W+E+S+N)

#now creating a scrollbar for our ListBox widget which will allow us to scroll the contents of our ListBox
Scrollbar = Scrollbar(app)
Scrollbar.grid(row=3,column=4,sticky = N+S)
#now here we are connecting our scrollbar to our ListBox
parts_list.configure(yscrollcommand=Scrollbar.set)
#command = parts_list.yview->is telling scrollbar wighet to scroll the listBox in y axis when scrollbar is scrolled
#by the user in y axis
Scrollbar.configure(command = parts_list.yview)
#binding our select item function '<<ListboxSelect>>'  to our listBox and function that we are using is select_item()
parts_list.bind('<<ListboxSelect>>',select_item)

#now here we are going to add some buttons to our application
#add button will add new parts to the database and the list box conatining the list of computer parts
add_button = Button(app,text="Add Part",width=12,command=add_item)
add_button.grid(row=2,column=0,pady=20)

#remove button will remove the computer part selected from the listbox from the database
remove_button = Button(app,text="Remove Part",width=12,command=remove_item)
remove_button.grid(row=2,column=1)

#update button will update the existing computer part in the database
update_button = Button(app,text="Update Part",width=12,command=update_item)
update_button.grid(row=2,column=2)

#clear button will clear all the input field of the application so that suer can enter the next data
clear_button = Button(app,text="Clear Input",width=12,command=clear_input)
clear_button.grid(row=2,column=3)

#dreating a developer info button
Dev_button = Button(app,text="Developer info",command=Dev_info)
Dev_button.grid(row=2,column=4,sticky=E)


#now we want to populate our listbox with computer parts list if present any when our application boots up
populate_list()

#start program
app.mainloop()