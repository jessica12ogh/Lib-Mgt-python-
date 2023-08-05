from tkinter import *
from tkinter import ttk
import pymongo
from datetime import datetime
# mongodb+srv://jessicalinus:0PWAPGOdGUecFR3M@cluster0.kbrlevl.mongodb.net/
#  MongoDB connection details
client = pymongo.MongoClient('mongodb://localhost:27017/library')

# Access a specific database (replace "mydatabase" with your database name)
db = client["mylibrary"]
s = db["students"] 
iv = db["books"]  # Collection for books
im = db["members"]  # Collection for members
ig = db["issued_books"]  # Collection for issued books
ir = db["returned_books"]  # Collection for returned books

class Main(object):
    def __init__(self,master):
        self.master = master
        
        

#         # Frames
        mainFrame = Frame(self.master)
        mainFrame.pack()
#         #top frame
        topFrame = Frame(mainFrame, bd=14, width=1350 , padx=20, bg='#FF00FF' ,relief="sunken", borderwidth=2)
        topFrame.pack(side=TOP)
    
#         #center frame
        centerFrame = Frame(mainFrame, bd=10, width=1350, bg='#ffffff' ,relief=RIDGE,)
        centerFrame.pack(side=TOP)
#          #center left frame
        centerLeftFrame = Frame(centerFrame, width=900, height=700, bg='#ffffff',relief="sunken", borderwidth=2)
        centerLeftFrame.pack(side=LEFT)
#         #center right frame
        centerRightFrame = Frame(centerFrame, width=1350, height=700, bg='#ffffff',relief="sunken", borderwidth=2)
        centerRightFrame.pack(side=RIGHT)

#         #search section
        searchBar = LabelFrame(centerRightFrame, width=400, height=70,text="Search Box", bg='#f8f',)
        searchBar.pack(fill=BOTH)
        self.lblsearch = Label(searchBar, text="Search for Books", font='arial 12 bold', bg='#ffffff', fg='#f8f')
        self.lblsearch.grid(row=0, column=0, padx=10, pady=10)
        self.entSearch = Entry(searchBar, font='arial 12 bold', width=20, bd=5)
        self.entSearch.grid(row=0, column=1,columnspan=2, padx=10, pady=10, )
        self.btnsearch = Button(searchBar, text="Search", font='arial 12 bold', width=10,bg='#ffffff', fg='#f8f', command=self.searchBook)
        self.btnsearch.grid(row=0, column=4, padx=15, pady=10,)

#  # Student Home Page
#         studentHomePage = LabelFrame(centerRightFrame, width=400, height=170, text="Student Home", bg='#f8f', )
#         studentHomePage.pack(fill=BOTH)
#         btnStudentHome = Button(studentHomePage, text="Student Home", font='arial 12 bold', width=10, bg='#ffffff', fg='#f8f', command=lambda: self.student_home(id))
#         btnStudentHome.grid(row=0, column=0, padx=15, pady=10, )
#         # Home Page
#         homePage = LabelFrame(centerRightFrame, width=400, height=170, text="Home", bg='#f8f', )
#         homePage.pack(fill=BOTH)
#         btnHome = Button(homePage, text="Home", font='arial 12 bold', width=10, bg='#ffffff', fg='#f8f', command=self.home)
#         btnHome.grid(row=0, column=0, padx=15, pady=10, )
#           # Delete Book Page
#         deleteBookPage = LabelFrame(centerRightFrame, width=400, height=170, text="Delete Book", bg='#f8f', )
#         deleteBookPage.pack(fill=BOTH)
#         btnDeleteBook = Button(deleteBookPage, text="Delete Book", font='arial 12 bold', width=10, bg='#ffffff', fg='#f8f', command=self.deleteBook)
#         btnDeleteBook.grid(row=0, column=0, padx=15, pady=10, )

#         # Delete Member Page
#         deleteMemberPage = LabelFrame(centerRightFrame, width=400, height=170, text="Delete Member", bg='#f8f', )
#         deleteMemberPage.pack(fill=BOTH)
#         btnDeleteMember = Button(deleteMemberPage, text="Delete Member", font='arial 12 bold', width=10, bg='#ffffff', fg='#f8f', command=self.deleteMember)
#         btnDeleteMember.grid(row=0, column=0, padx=15, pady=10, )

#         # Delete Issue Page
#         deleteIssuePage = LabelFrame(centerRightFrame, width=400, height=170, text="Delete Issue", bg='#f8f', )
#         deleteIssuePage.pack(fill=BOTH)
#         btnDeleteIssue = Button(deleteIssuePage, text="Delete Issue", font='arial 12 bold', width=10, bg='#ffffff', fg='#f8f', command=self.deleteIssue)
#         btnDeleteIssue.grid(row=0, column=0, padx=15, pady=10, )

#         # Delete Return Page
#         deleteReturnPage = LabelFrame(centerRightFrame, width=400, height=170, text="Delete Return", bg='#f8f', )
#         deleteReturnPage.pack(fill=BOTH)
#         btnDeleteReturn = Button(deleteReturnPage, text="Delete Return", font='arial 12 bold', width=10, bg='#ffffff', fg='#f8f', command=self.deleteReturn)
#         btnDeleteReturn.grid(row=0, column=0, padx=15, pady=10, )
 # Update Book Page
        updateBookPage = LabelFrame(centerRightFrame, width=400, height=170, text="Update Book", bg='#f8f', )
        updateBookPage.pack(fill=BOTH)
        btnUpdateBook = Button(updateBookPage, text="Update Book", font='arial 12 bold', width=10, bg='#ffffff', fg='#f8f', command=self.updateBook)
        btnUpdateBook.grid(row=0, column=0, padx=15, pady=10, )

        # Update Member Page
        updateMemberPage = LabelFrame(centerRightFrame, width=400, height=170, text="Update Member", bg='#f8f', )
        updateMemberPage.pack(fill=BOTH)
        btnUpdateMember = Button(updateMemberPage, text="Update Member", font='arial 12 bold', width=10, bg='#ffffff', fg='#f8f', command=self.updateMember)
        btnUpdateMember.grid(row=0, column=0, padx=15, pady=10, )

        # Update Issue Page
        updateIssuePage = LabelFrame(centerRightFrame, width=400, height=170, text="Update Issue", bg='#f8f', )
        updateIssuePage.pack(fill=BOTH)
        btnUpdateIssue = Button(updateIssuePage, text="Update Issue", font='arial 12 bold', width=10, bg='#ffffff', fg='#f8f', command=self.updateIssue)
        btnUpdateIssue.grid(row=0, column=0, padx=15, pady=10, )

        # Update Return Page
        updateReturnPage = LabelFrame(centerRightFrame, width=400, height=170, text="Update Return", bg='#f8f', )
        updateReturnPage.pack(fill=BOTH)
        btnUpdateReturn = Button(updateReturnPage, text="Update Return", font='arial 12 bold', width=10,bg='#ffffff', fg='#f8f', command=self.updateReturn)
        btnUpdateReturn.grid(row=0, column=0, padx=15, pady=10, )
# #          # Penality Update Page
#         penalityUpdatePage = LabelFrame(centerRightFrame, width=400, height=170, text="Penality Update", bg='#f8f', )
#         penalityUpdatePage.pack(fill=BOTH)
#         btnPenalityUpdate = Button(penalityUpdatePage, text="Penalty Update", font='arial 12 bold', width=10, bg='#ffffff', fg='#f8f', command=self.penality_update)
#         btnPenalityUpdate.grid(row=0, column=0, padx=15, pady=10, )

#         # Penality View Page
#         penaltyViewPage = LabelFrame(centerRightFrame, width=400, height=170, text="Penalty View", bg='#f8f', )
#         penaltyViewPage.pack(fill=BOTH)
#         btnPenaltyView = Button(penaltyViewPage, text="Penalty View", font='arial 12 bold', width=10, bg='#ffffff', fg='#f8f', command=self.viewPenalty)
#         btnPenaltyView.grid(row=0, column=0, padx=15, pady=10, )

#         # Issued Book Page
#         issuedBookPage = LabelFrame(centerRightFrame, width=400, height=170, text="Issued Book", bg='#f8f', )
#         issuedBookPage.pack(fill=BOTH)
#         btnIssuedBook = Button(issuedBookPage, text="Issued Book", font='arial 12 bold', width=10, bg='#ffffff', fg='#f8f', command=self.viewIssuedBook)
#         btnIssuedBook.grid(row=0, column=0, padx=15, pady=10, )

#         #list section
        listBar = LabelFrame(centerRightFrame, width=400, height=170,text="List Box", bg='#f8f', )
        listBar.pack(fill=BOTH)
        lblList = Label(listBar, text="List of Books", font='times 16 bold', bg='white', fg='#ffffff')
        lblList.grid(row=0, column=2, padx=10, pady=10)
        self.listChoice = IntVar()
        rb1 = Radiobutton(listBar, text="All Books",var=self.listChoice,value=1, font='arial 12 bold', bg='white', fg='#f8f',) 
        rb2 = Radiobutton(listBar, text="Available Books",var=self.listChoice,value=2, font='arial 12 bold', bg='white', fg='#f8f',command=self.availableBook)
        rb3 = Radiobutton(listBar, text="Issued Books",var=self.listChoice,value=3, font='arial 12 bold', bg='white', fg='#f8f',command=self.issuedBook)
        rb1.grid(row=1, column=0)
        rb2.grid(row=1, column=1)
        rb3.grid(row=1, column=2)
        btnList = Button(listBar, text="List Books", font='arial 12 bold', width=10,bg='#f8f', fg='white', command=self.listBook)
        btnList.grid(row=1, column=3, padx=40, pady=20, )

#         #book details section
        bookDetails = LabelFrame(centerRightFrame, width=400, height=170,text="Book Details", bg='#f8f', )
        bookDetails.pack(fill=BOTH)
        lblBookName = Label(bookDetails, text="Book Name", font='arial 12 bold', bg='#f8f', fg='white')
        lblBookName.grid(row=0, column=0, padx=10, pady=10)

        lblAuthor = Label(bookDetails, text="Author", font='arial 12 bold', bg='#f8f', fg='white')
        lblAuthor.grid(row=0, column=2, padx=10, pady=10)

        lblEdition = Label(bookDetails, text="Edition", font='arial 12 bold', bg='#f8f', fg='white')
        lblEdition.grid(row=1, column=0, padx=10, pady=10)

        lblStatus = Label(bookDetails, text="Status", font='arial 12 bold', bg='#f8f', fg='white')
        lblStatus.grid(row=1, column=2, padx=10, pady=10)

        lblBookPublish = Label(bookDetails, text="Date of Publish", font='arial 12 bold', bg='#f8f', fg='white')
        lblBookPublish.grid(row=0, column=0, padx=10, pady=10)

#         #Title & Image section
        imageBar = LabelFrame(centerLeftFrame, width=400, height=350)
        imageBar.pack(fill=BOTH)
        self.titleRight = Label(imageBar, text="Welcome To Our Library", font='arial 20 bold', bg='#f8f', fg='white')
        self.titleRight.grid(row=0)
       
        self.lblImg = Label(imageBar )
        self.lblImg.grid(row=1, column=0, padx=10, pady=10)

# #################################################Tool bar section###############################################
    # add a book section
        self.btnbook = Button(topFrame, text="Add Book", compound=LEFT, font='arial 12 bold',command=self.open_add_book_page,)  
        self.btnbook.pack(side=LEFT, padx=20,)  
        self.btnbook.bind("<Button-1>", self.open_add_book_page)
         # add a member button
        self.btnmember = Button(topFrame, text="Add Member",compound=LEFT,   font='arial 12 bold',padx=10, command=self.open_add_member_page, )
        self.btnmember.configure( compound=LEFT)
        self.btnmember.pack(side=LEFT, padx=20)
        self.btnmember.bind("<Button-1>", self.open_add_member_page)
                #give book section
        self.btngive = Button(topFrame, text="Give Book", font='arial 12 bold', compound=LEFT, command=self.open_give_book_page)
        self.btngive.pack(side=LEFT, padx=20)
        self.btngive.bind("<Button-1>", self.open_give_book_page)
           #return book section
        self.btnreturn = Button(topFrame, text="Return Book", font='arial 12 bold', compound=LEFT, command=self.open_return_book_page)
        self.btnreturn.pack(side=LEFT, padx=20)
        self.btngive.bind("<Button-1>", self.open_return_book_page)
        
        
#   ##################################################Tabs section##################################################
         #tabs
        self.tabs = ttk.Notebook(centerLeftFrame, width=900, height=700)
        self.tabs.pack()
        
# ##################################################Tab1 section##################################################
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text="Library Management", compound=LEFT)
        self.tabs.add(self.tab2, text="Statistics", compound=LEFT)
        
        #list of books section
        self.listOfBooks = LabelFrame(self.tab1, width=40, height=30, font='times 12 bold', bd=5)
        self.listOfBooks.grid(row=0, column=0, padx=(8,0), pady=8, sticky=N)

#         # Listbox widget for displaying the list of books
        self.listBox = Listbox(self.listOfBooks, width=80, height=30, font='times 12 bold', bd=5)
        self.listBox.pack(side=LEFT, fill=BOTH)

#         # Scrollbar for the Listbox
        self.sb = Scrollbar(self.listOfBooks, orient=VERTICAL, command=self.listBox.yview)
        self.sb.pack(side=RIGHT, fill=Y)

#         # Configure Listbox yview with the Scrollbar
        self.listBox.config(yscrollcommand=self.sb.set)

          
# ##########################Tab2  section##############################################
#         #tab2
        self.lblBookCount=Label(self.tab2, text="Total Books", font='verdena 14 bold',pady=20,)
        self.lblBookCount.grid(row=0,)
        self.lblMemberCount=Label(self.tab2, text="Total Members", font='verdena 14 bold',pady=20,)
        self.lblMemberCount.grid(row=1,sticky=W)
        self.lblIssuedCount=Label(self.tab2, text="Total Issued Books", font='verdena 14 bold',pady=20,)
        self.lblIssuedCount.grid(row=2,sticky=W)

       
    def open_add_book_page(self):
        self.clear_widgets()
        mainFrame = Frame(self.master)
        mainFrame.pack()
        self.title_label = Label(mainFrame, text="Add Book", font='arial 16 bold')
        self.title_label.pack(pady=20)

        self.name_entry =Entry(mainFrame,text="Title", font='arial 12')
        self.name_entry.pack(pady=10)

        self.address_entry =Entry(mainFrame,text="Author", font='arial 12')
        self.address_entry.pack(pady=10)

        self.contact_entry =Entry(mainFrame,text="Edition", font='arial 12')
        self.contact_entry.pack(pady=10)

        self.email_entry =Entry(mainFrame,text="date", font='arial 12')
        self.email_entry.pack(pady=10)

        self.submit_button =Button(mainFrame, text="Submit", font='arial 12 bold', command=self.addBook)
        self.submit_button.pack()
        self.submit_button =Button(mainFrame, text="Home", font='arial 12 bold', command=self.home)
        self.submit_button.pack()
         
    def open_add_member_page(self):
        self.clear_widgets()
        mainFrame = Frame(self.master)
        mainFrame.pack()
        self.title_label =Label(mainFrame, text="Add Member", font='arial 16 bold')
        self.title_label.pack(pady=20)

        self.name_entry =Entry(mainFrame,text="Name", font='arial 12')
        self.name_entry.pack(pady=10)

        self.address_entry =Entry(mainFrame,text="Address", font='arial 12')
        self.address_entry.pack(pady=10)

        self.contact_entry =Entry(mainFrame,text="Contact", font='arial 12')
        self.contact_entry.pack(pady=10)

        self.email_entry =Entry(mainFrame,text="Email", font='arial 12')
        self.email_entry.pack(pady=10)

        self.submit_button =Button(mainFrame, text="Submit", font='arial 12 bold', command=self.addMember)
        self.submit_button =Button(mainFrame, text="Home", font='arial 12 bold', command=self.home)
        self.submit_button.pack()



    def open_give_book_page(self):
        self.clear_widgets()
        mainFrame = Frame(self.master)
        mainFrame.pack()
        self.title_label =Label(mainFrame, text="Give Book", font='arial 16 bold')
        self.title_label.pack(pady=20)

        self.name_entry =Entry(mainFrame,text="Name", font='arial 12')
        self.name_entry.pack(pady=10)
        self.name_entry =Entry(mainFrame,text="Title", font='arial 12')
        self.name_entry.pack(pady=10)
        self.name_entry =Entry(mainFrame,text="Date", font='arial 12')
        self.name_entry.pack(pady=10)

        self.submit_button =Button(mainFrame, text="Submit", font='arial 12 bold', command=self.giveBook)
        self.submit_button =Button(mainFrame, text="Home", font='arial 12 bold', command=self.home)
        self.submit_button.pack()

    

       
        
        
    def open_return_book_page(self):
        self.clear_widgets()
        mainFrame = Frame(self.master)
        mainFrame.pack()
        self.title_label =Label(self.master, text="Return Book", font='arial 16 bold')
        self.title_label.pack(pady=20)
        self.name_entry =Entry(mainFrame,text="Name", font='arial 12')
        self.name_entry.pack(pady=10)
        self.name_entry =Entry(mainFrame,text="Title", font='arial 12')
        self.name_entry.pack(pady=10)
        self.name_entry =Entry(mainFrame,text="Date", font='arial 12')
        self.name_entry.pack(pady=10)


        self.submit_button =Button(self.master, text="Submit", font='arial 12 bold', command=self.returnBook)
        self.submit_button =Button(self.master, text="Home", font='arial 12 bold', command=self.home)
        self.submit_button.pack()

    def clear_widgets(self):
        for widget in self.master.winfo_children():
            widget.destroy()



 
    def searchBook(self):
        name1 = input("Enter the title of the book or Book Author's name: ")
        t = {'$or': [{"title": name1}, {"author": name1}]}
        # In below condition ID is disabled to show to the user
        t1 = iv.find_one(t, {"_id": 0, "title": 1, "author": 1, "edition": 1, "status": 1, "date": 1})
        if t1 != None:
            t1 = iv.DataFrame(t1, index=[0])
            print(t1)
        else:
            print("Book not found")

    def availableBook(self):
        i=iv.find({"status":"Available"},{"_id":0,"title":1,"author":1,"edition":1,"status":1,"date":1}).sort("_id")
        print(i)
    def issuedBook(self):
        u=iv.find({"status":"Issued"},{"_id":0,"title":1,"author":1,"edition":1,"status":1,"date":1}).sort("_id")
        print(u)
    def listBook(self):
        k=iv.find()
        print(k)
    def addBook(self):
        title=input("Enter the title of the book ")
        author=input("Enter the author of the book ")
        edition=input("Enter the edition of the book ")
        status="Book Available"
        date=input("Enter the date of the book ")
        iv=self.db["books"]
        iv.insert_one({"title":title,"author":author,"edition":edition,"status":status,"date":date})
        print("Book added successfully")
    def addMember(self):
        name=input("Enter the name of the member ")
        address=input("Enter the address of the member ")
        contact=input("Enter the contact of the member ")
        email=input("Enter the email of the member ")
        im.insert_one({"name":name,"address":address,"contact":contact,"email":email})
        im = self.db["members"]
        print("Member added successfully")
    def giveBook(self):
        name=input("Enter the name of the member ")
        title=input("Enter the title of the book ")
        date=input("Enter the date of the book ")
        ig=self.db["issued_books"]
        ig.insert_one({"name":name,"title":title,"date":date})
        print("Book issued successfully")
    def returnBook(self):
        name=input("Enter the name of the member ")
        title=input("Enter the title of the book ")
        date=input("Enter the date of the book ")
        ir=self.db["returned_books"]
        ir.insert_one({"name":name,"title":title,"date":date})
        print("Book returned successfully")
    def deleteBook(self):
        name=input("Enter the title of the book ")
        iv.delete_one({"title":name})
        print("Book deleted successfully")
    def deleteMember(self):
        name=input("Enter the name of the member ")
        im.delete_one({"name":name})
        print("Member deleted successfully")
    def deleteIssue(self):
        name=input("Enter the name of the member ")
        title=input("Enter the title of the book ")
        ig.delete_one({"name":name,"title":title})
        print("Issue deleted successfully")
    def deleteReturn(self):
        name=input("Enter the name of the member ")
        title=input("Enter the title of the book ")
        ir.delete_one({"name":name,"title":title})
        print("Return deleted successfully")
    def updateBook(self):
        name=input("Enter the title of the book ")
        author=input("Enter the author of the book ")
        edition=input("Enter the edition of the book ")
        status="Updated"
        date=input("Enter the date of the book ")
        iv.update_one({"title":name},{"$set":{"author":author,"edition":edition,"status":status,"date":date}})
        print("Book updated successfully")
    def updateMember(self):
        name=input("Enter the name of the member ")
        address=input("Enter the address of the member ")
        contact=input("Enter the contact of the member ")
        email=input("Enter the email of the member ")
        im.update_one({"name":name},{"$set":{"address":address,"contact":contact,"email":email}})
        print("Member updated successfully")
    def updateIssue(self):
        name=input("Enter the name of the member ")
        title=input("Enter the title of the book ")
        date=input("Enter the date of the book ")
        ig.update_one({"name":name,"title":title},{"$set":{"status":"ReIssued","date":date}})
        print("Issue updated successfully")
    def updateReturn(self):
        name=input("Enter the name of the member ")
        title=input("Enter the title of the book ")
        ir.update_one({"name":name,"title":title},{"$set":{"status":"Returned"}})
        print("Return updated successfully")
    def issueList(self):
        i=ig.find()
        print(i)
    def returnList(self):
        r=ir.find()
        print(r)
    def memberList():
        m=im.find()
        print(m)
#delete all book
    def deleteAllBook(self):
        iv.delete_many({})
        print("All Books deleted successfully")
#delete all member
    def deleteAllMember(self):
        im.delete_many({})
        print("All Members deleted successfully")
#delete all issue
    def deleteAllIssue(self):
        ig.delete_many({})
        print("All Issues deleted successfully")
#delete all return
    def deleteAllReturn(self):
        ir.delete_many({})
        print("All Returns deleted successfully")
#update all book
    def updateAllBook(self):
        name=input("Enter the title of the book ")
        author=input("Enter the author of the book ")
        edition=input("Enter the edition of the book ")
        status="Updated"
        date=input("Enter the date of the book ")
        iv.update_many({"title":name},{"$set":{"author":author,"edition":edition,"status":status,"date":date}})
        print("All Books updated successfully")
#update all member
    def updateAllMember(self):
        name=input("Enter the name of the member ")
        address=input("Enter the address of the member ")
        contact=input("Enter the contact of the member ")
        email=input("Enter the email of the member ")
        im.update_many({"name":name},{"$set":{"address":address,"contact":contact,"email":email}})
        print("All Members updated successfully")
#update all issue
    def updateAllIssue(self):
        name=input("Enter the name of the member ")
        title=input("Enter the title of the book ")
        date=input("Enter the date of the book ")
        ig.update_many({"name":name,"title":title},{"$set":{"status":"ReIssued","date":date}})
        print("All Issues updated successfully")
#update all return
    def updateAllReturn(self):
        name=input("Enter the name of the member ")
        title=input("Enter the title of the book ")
        ir.update_many({"name":name,"title":title},{"$set":{"status":"Returned"}})
        print("All Returns updated successfully")
#penality update
    def penality_update():
        r = ir.find()
        for i in r:
            d1 = datetime.strptime(i["date"], "%d/%m/%Y")
            d2 = datetime.now()
            d = d2 - d1
            if d.days > 15:
                s.update_one({"name": i["name"]}, {"$inc": {"book_penalty": 1}})
#penality view
    def viewPenalty(id):
        d=s.find_one({"_id":id})
        print("Your penalty is ",d["book_penalty"])
#view issued book
    def viewIssuedBook(id):
        i=ig.find({"name":id},{"_id":0,"title":1,"date":1}).sort("_id")
        print(i)
#student name
    def studentName():
        name=input("Enter your name ")
        return name
#student email
    def studentEmail():
        email=input("Enter your email ")
        return email
#student department
    def studentDepartment():
        department=input("Enter your department ")
        return department
#student year
    def studentYear():
        year=input("Enter your year ")
        return year
#student semester
    def studentSemester():
        semester=input("Enter your semester ")
        return semester
#student password
    def password():
        password=input("Enter your password ")
        return password
#student phone number
    def phoneNumber():
        phoneNumber=input("Enter your phone number ")
        return phoneNumber
#student home page
    def student_home(id):
        print("Student Home")
        print("Enter 1 to search book\nEnter 2 to view issued book\nEnter 3 to view penalty\nEnter 4 to logout")
        option=input("Enter your choice ")
        if option=="1":
            searchBook()
            student_home(id)
        elif option=="2":
            viewIssuedBook(id)
            student_home(id)
        elif option=="3":
            viewPenalty(id)
            student_home(id)
        elif option=="4":
            home()
        else:
            print("Invalid choice")
            student_home(id)
 #Home page
    def home(self):
        penality_update()
        option=input("Enter 1 for Admin\nEnter 2 for Student\n")
        if option == "1":
            print("Hi student,Welcome to the Library")
            option1=("Enter 1 to register\nEnter 2 to login\n")
        if option1=="1":

            student_register()
            #for student login
        elif option1=="2":
            student_login()
        else:
            print("Invalid choice")
            home()    

    
#student registration
    def student_register():
        d = {
            "_id": phoneNumber(),
            "password": password(),
            "name": studentName(),
            "email": studentEmail(),
            "department": studentDepartment(),
            "year": studentYear(),
            "semester": studentSemester(),
            "book_issued": 0,
            "book_penalty": 0
        }
        s.insert_one(d)
        print("Student registered successfully")
        home()

#student login
    def student_login():
        print("Student Login")
        id = input("Enter your ID: ")
        password = input("Enter your password: ")
        d = s.find_one({"_id": id, "password": password})
        if d is not None:
            print("Login successfully")
            student_home(id)
        else:
            print("Invalid ID or Password")
            student_login()


    
#main function
    def main():
        root = Tk()
        app = Main(root)
        root.title("Library Management System")  
        root.geometry("1350x750+350+200")
    
        root.mainloop()

if __name__ == '__main__':

    Main.main()