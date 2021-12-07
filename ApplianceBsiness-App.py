import sqlite3
from tkinter import *
from tkinter.ttk import Treeview

# connect to database


# create the UI
master = Tk()
label = Label(master,
              text="Main")
label.pack(pady=10)
conn = sqlite3.connect("ApplianceBusiness.db")
cursor = conn.cursor()


def insert_test_database():
    sqlInsertAddress = "INSERT INTO Address VALUES (?, ?, ?, ?, ?, ?, ?)"
    sqlInsertCustomer = "INSERT INTO Customer VALUES (?, ?, ?, ?)"
    sqlInsertEmployee = "INSERT INTO Employee VALUES (?, ?, ?, ?, ?, ?)"
    sqlInsertProduct = "INSERT INTO Product VALUES (?, ?, ?, ?, ?, ?)"
    sqlInsertStock = "INSERT INTO Stock VALUES (?, ?, ?, ?)"
    sqlInsertSupplier = "INSERT INTO Supplier VALUES (?, ?)"
    sqlInsertSupplying = "INSERT INTO Supplying VALUES (?, ?, ?, ?)"
    sqlInsertEvent = "INSERT INTO Event VALUES (?, ?, ?, ?, ?)"
    sqlInsertEventTicket = "INSERT INTO Event_Ticket VALUES (? ,?)"
    sqlInsertInvoice = "INSERT INTO Invoice VALUES (? ,?, ?, ?, ?, ?)"
    # insert the address to database to test
    valAddress = [
        (1, 'Lowstreet 4', 'San Jose', 'CA', 95111, 'Peter@gmail.com', 6692331110),
        (2, 'Apple st 652', 'San Jose', 'CA', 95112, 'Peter@gmail.com', 6692331111),
        (3, 'Mountain 21', 'San Jose', 'CA', 95113, 'Peter@gmail.com', 6692331112),
        (4, 'Valley 345', 'San Jose', 'CA', 95114, 'Peter@gmail.com', 6692331113),
        (5, 'Ocean blvd 2', 'San Jose', 'CA', 95115, 'Peter@gmail.com', 6692331114),
        (6, 'Green Grass 1', 'San Jose', 'CA', 95116, 'Peter@gmail.com', 6692331115),
        (7, 'Sky st 331', 'San Jose', 'CA', 95117, 'Peter@gmail.com', 6692331116),
        (8, 'One way 98', 'San Jose', 'CA', 95118, 'Peter@gmail.com', 6692331117),
        (9, 'Yellow Garden 2', 'San Jose', 'CA', 95119, 'Peter@gmail.com', 6692331118),
        (10, 'Park Lane 38', 'San Jose', 'CA', 95120, 'Peter@gmail.com', 6692331119),
        (11, 'Central st 954', 'San Jose', 'CA', 95121, 'Peter@gmail.com', 6692331120),
        (12, 'Main Road 989', 'San Jose', 'CA', 95121, 'Peter@gmail.com', 6692331121),
        (13, 'Sideway 1633', 'San Jose', 'CA', 95123, 'Peter@gmail.com', 6692331121)
    ]
    # Insert value to Customer for test
    valCustomer = [
        (1, 'Peter', 'Son', 1),
        (2, 'Amy', 'Nguyen', 2),
        (3, 'Hannah', 'Burger', 3),
        (4, 'Micheal', 'Huynh', 4),
        (5, 'Sandy', 'Smith', 5),
        (6, 'Betty', 'Williams', 6),
        (7, 'Richard', 'Brown', 7),
        (8, 'Susan', 'Jones', 8),
        (9, 'Vicky', 'Garcia', 9),
        (10, 'Ben', 'Martinez', 10),
        (11, 'William', 'Hernandez', 11),
        (12, 'Chuck', 'Lopez', 12),
        (13, 'Viola', 'Wilson', 13)
    ]
    # insert data to Employee to Test
    valEmployee = [
        (111, 'Moore', 'Katie', 'Seller', 70000, 14),
        (112, 'Jackson', 'Peter', 'Seller', 70000, 15),
        (113, 'Martin', 'Jenny', 'Seller', 70000, 16),
        (114, 'Ben', 'Burger', 'Manager', 90000, 17),
    ]
    # insert data to Product to Test
    valProduct = [
        (101, "TV", "SamSung", 2020, 200, "TV 27 Inch"),
        (102, "TV", "SamSung", 2021, 300, "TV 32 Inch"),
        (103, "TV", "SamSung", 2020, 350, "TV 42 Inch"),
        (104, "TV", "SamSung", 2020, 500, "TV 50 Inch"),
        (105, "TV", "SamSung", 2019, 900, "TV 100 Inch"),
        (201, "Refrigerator", "SamSung", 2020, 299, "1 cubic"),
        (202, "Refrigerator", "SamSung", 2020, 399, "2 cubic"),
        (203, "Refrigerator", "SamSung", 2020, 499, "3 cubic"),
        (204, "Refrigerator", "SamSung", 2020, 599, "4 cubic"),
        (205, "Refrigerator", "SamSung", 2020, 699, "5 cubic"),
        (301, "TV", "Sony", 2020, 400, "TV 27 inch"),
        (302, "TV", "Sony", 2020, 500, "TV 32 inch"),
        (303, "TV", "Sony", 2020, 600, "TV 40 inch"),
        (304, "TV", "Sony", 2020, 700, "TV 49 inch"),
        (305, "TV", "Sony", 2020, 800, "TV 75 inch"),
        (401, "Refrigerator", "Sony", 2021, 110, "1 cubic"),
        (402, "Refrigerator", "Sony", 2021, 200, "2 cubic"),
        (403, "Refrigerator", "Sony", 2021, 320, "3 cubic"),
        (404, "Refrigerator", "Sony", 2021, 430, "4 cubic"),
        (405, "Refrigerator", "Sony", 2021, 580, "5 cubic"),
        (406, "Refrigerator", "Sony", 2021, 720, "6 cubic")
    ]
    # insert data to stock
    valStock = [
        (1, 101, 12, 1),
        (2, 102, 13, 1),
        (3, 103, 13, 1),
        (4, 104, 13, 1),
        (5, 105, 13, 1),
        (6, 201, 13, 1),
        (7, 202, 13, 1),
        (8, 203, 13, 1),
        (9, 204, 11, 1),
        (10, 205, 10, 1),
        (11, 301, 13, 2),
        (12, 302, 13, 2),
        (13, 303, 13, 2),
        (14, 304, 13, 2),
        (15, 305, 13, 2),
        (16, 401, 13, 2),
        (17, 402, 13, 2),
        (18, 403, 13, 2),
        (19, 404, 13, 2),
        (20, 405, 13, 2),
        (21, 406, 13, 2),

    ]
    # insert data to Supplier
    valSupplier = [
        (1, "SamSung Supply"),
        (2, "Sony Supply ")
    ]
    # insert data to Supplying
    valSupplying = [
        (1, 1, 101, 200),
        (2, 1, 102, 300),
        (3, 2, 303, 600),
        (4, 2, 404, 430)
    ]
    # insert into Event table to test Data
    valEvent = [
        (1, "Tet Holiday", "11/15/2021", "1/15/2022", "Lottery to win TV"),
        (2, "Summer", "05/15/2021", "07/15/2021", "Lottery to win Refrigerator")
    ]
    # insert into EventTicket to test Data
    valEventTicket = [
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 1),
        (5, 1),
        (6, 1),
        (7, 1),
        (8, 1),
        (9, 1),
        (10, 1),
        (11, 1),
        (12, 1),
    ]
    # insert into Invoice to test Data

    valInvoice = [
        (1, 101, 111, 1, 200, 1),
        (2, 102, 112, 1, 300, 2),
        (3, 103, 113, 2, 350, 3),
        (4, 104, 114, 2, 500, 4),
        (5, 105, 111, 3, 900, 5),
        (6, 201, 111, 3, 299, 6),
        (7, 202, 111, 4, 399, 7),
        (8, 203, 112, 4, 499, 8),
        (9, 204, 113, 5, 599, 9),
        (10, 301, 114, 5, 300, 10),
        (11, 302, 113, 6, 400, 11),
        (12, 303, 113, 6, 500, 12),
        (13, 304, 113, 6, 600, 13),
    ]
    cursor.executemany(sqlInsertAddress, valAddress)
    cursor.executemany(sqlInsertCustomer, valCustomer)
    cursor.executemany(sqlInsertEmployee, valEmployee)
    cursor.executemany(sqlInsertEvent, valEvent)
    cursor.executemany(sqlInsertEventTicket, valEventTicket)
    cursor.executemany(sqlInsertInvoice, valInvoice)
    cursor.executemany(sqlInsertProduct, valProduct)
    cursor.executemany(sqlInsertStock, valStock)
    cursor.executemany(sqlInsertSupplier, valSupplier)
    cursor.executemany(sqlInsertSupplying, valSupplying)
    print(cursor.fetchall())
    conn.commit()


def clear_test_database():
    cursor.execute("DELETE FROM Address")
    cursor.execute("DELETE FROM Customer")
    cursor.execute("DELETE FROM Employee")
    cursor.execute("DELETE FROM Event")
    cursor.execute("DELETE FROM Event_Ticket")
    cursor.execute("DELETE FROM Invoice")
    cursor.execute("DELETE FROM Product")
    cursor.execute("DELETE FROM Stock")
    cursor.execute("DELETE FROM Supplier")
    cursor.execute("DELETE FROM Supplying")
    conn.commit()


def create_frame_customer(customer_window):
    customer_window.title("Customer View")
    # sets the geometry of toplevel
    # A Label widget to show in toplevel
    frame_search = Frame(customer_window)
    frame_search.grid(row=0, column=0)
    lbl_search = Label(frame_search, text='Search By ID (1,2,3,4)',
                       font=('bold', 12), pady=20)
    lbl_search.grid(row=0, column=0, sticky=W)
    customer_search = StringVar()
    customer_search_entry = Entry(frame_search, textvariable=customer_search)
    customer_search_entry.grid(row=0, column=1)
    customer_search.set("1")
    frame_customer_view = Frame(customer_window)
    frame_customer_view.grid(row=4, column=0, columnspan=4, rowspan=6, pady=20, padx=20)

    columns = ['customer_ID', 'product_type', 'brand', 'description', 'total_Price', 'ticket_Number']
    customer_tree_view = Treeview(frame_customer_view, columns=columns, show="headings")
    customer_tree_view.column("customer_ID", width=30)
    for col in columns[1:]:
        customer_tree_view.column(col, width=120)
        customer_tree_view.heading(col, text=col)
    customer_tree_view.pack(side="left", fill="y")
    scrollbar = Scrollbar(frame_customer_view, orient='vertical')
    scrollbar.configure(command=customer_tree_view.yview)
    scrollbar.pack(side="right", fill="y")
    customer_tree_view.config(yscrollcommand=scrollbar.set)

    def search_hostname():
        hostname = customer_search.get()
        cursor.execute(
            "SELECT customer_ID, Product.type AS product_type, Product.brand AS brand, "
            "Product.Description AS description, total_Price"
            ", ticket_Number "
            " FROM Invoice"
            " INNER JOIN Product ON Product.product_ID = Invoice.product_ID"
            " WHERE customer_ID = ?", hostname)
        rows = cursor.fetchall()
        for i in customer_tree_view.get_children():
            customer_tree_view.delete(i)
        for row in rows:
            customer_tree_view.insert('', 'end', values=row)

    search_btn = Button(customer_window, text='Search',
                        width=12, command=search_hostname)
    search_btn.grid(row=0, column=2)


def create_frame_employee(employee_window):
    employee_window.title("Check Inventory")
    # sets the geometry of toplevel
    # A Label widget to show in toplevel
    frame_search = Frame(employee_window)
    frame_search.grid(row=0, column=0)
    lbl_search = Label(frame_search, text='Search By brand (SamSung,Sony)',
                       font=('bold', 12), pady=20)
    lbl_search.grid(row=0, column=0, sticky=W)
    employee_search = StringVar()
    employee_search_entry = Entry(frame_search, textvariable=employee_search)
    employee_search_entry.grid(row=0, column=1)
    employee_search.set("SamSung")
    frame_employee_view = Frame(employee_window)
    frame_employee_view.grid(row=4, column=0, columnspan=4, rowspan=6, pady=20, padx=20)

    columns = ['product_ID', 'product_type', 'brand', 'price', 'description', 'quality']
    employee_tree_view = Treeview(frame_employee_view, columns=columns, show="headings")
    employee_tree_view.column("product_ID", width=30)
    for col in columns[1:]:
        employee_tree_view.column(col, width=120)
        employee_tree_view.heading(col, text=col)
    employee_tree_view.pack(side="left", fill="y")
    scrollbar = Scrollbar(frame_employee_view, orient='vertical')
    scrollbar.configure(command=employee_tree_view.yview)
    scrollbar.pack(side="right", fill="y")
    employee_tree_view.config(yscrollcommand=scrollbar.set)

    def search_hostname():
        hostname = employee_search.get()
        cursor.execute(
            "SELECT Product.product_ID, type, brand, price, description, Stock.quantity AS quantity FROM Product "
            "INNER JOIN Stock ON Stock.product_ID = Product.product_ID"
            " WHERE brand =?", [hostname])

        rows = cursor.fetchall()
        for i in employee_tree_view.get_children():
            employee_tree_view.delete(i)
        for row in rows:
            employee_tree_view.insert('', 'end', values=row)

    search_btn = Button(employee_window, text='Search',
                        width=12, command=search_hostname)
    search_btn.grid(row=0, column=2)


def create_frame_owner(owner_window):
    owner_window.title("Check Performance of Employee")
    frame_search = Frame(owner_window)
    frame_search.grid(row=0, column=0)
    lbl_search = Label(frame_search, text='Check Performance of Employee',
                       font=('bold', 12), pady=20)
    lbl_search.grid(row=0, column=0, sticky=W)
    frame_owner_view = Frame(owner_window)
    frame_owner_view.grid(row=4, column=0, columnspan=4, rowspan=6, pady=20, padx=20)

    columns = ['Employee_ID', 'NumberOfSale', 'firstName', 'lastName']
    owner_tree_view = Treeview(frame_owner_view, columns=columns, show="headings")
    owner_tree_view.column("Employee_ID", width=30)
    for col in columns[1:]:
        owner_tree_view.column(col, width=120)
        owner_tree_view.heading(col, text=col)
    owner_tree_view.pack(side="left", fill="y")
    scrollbar = Scrollbar(frame_owner_view, orient='vertical')
    scrollbar.configure(command=owner_tree_view.yview)
    scrollbar.pack(side="right", fill="y")
    owner_tree_view.config(yscrollcommand=scrollbar.set)

    def search_hostname():
        cursor.execute("SELECT Invoice.employee_id , COUNT(Invoice.employee_id) AS NumberOfSale, Employee.firstName AS"
                       " firstName, Employee.lastName AS lastName FROM Invoice"
                       " INNER JOIN Employee ON Employee.employee_id=Invoice.employee_id"
                       " GROUP BY Invoice.employee_id ORDER BY COUNT (Invoice.employee_id) Desc"
                       " "
                       )
        rows = cursor.fetchall()
        for i in owner_tree_view.get_children():
            owner_tree_view.delete(i)
        for row in rows:
            owner_tree_view.insert('', 'end', values=row)

    search_btn = Button(owner_window, text='Check',
                        width=12, command=search_hostname)
    search_btn.grid(row=0, column=2)


# Customer Window
def customerWindow():
    customer_window = Toplevel(master)
    create_frame_customer(customer_window)


# Employee Window
def employeeWindow():
    employee_window = Toplevel(master)
    create_frame_employee(employee_window)


def ownerWindow():
    owner_window = Toplevel(master)
    create_frame_owner(owner_window)


def Insert_test():
    insert_test_database()


def Clear_database():
    clear_test_database()


btn_customer = Button(master, text="Customer", command=customerWindow)
btn_employee = Button(master, text="Employee", command=employeeWindow)
btn_owner = Button(master, text="Owner", command=ownerWindow)
btn_Insert_Test = Button(master, text="Load_database_Test", command=insert_test_database)
btn_clear_Test = Button(master, text="Clear database", command=Clear_database)
btn_customer.pack(pady=10)
btn_employee.pack(pady=10)
btn_owner.pack(pady=10)
btn_Insert_Test.pack(pady=10)
btn_clear_Test.pack(pady=10)
mainloop()
