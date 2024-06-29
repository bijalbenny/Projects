import tkinter as tk
import mysql.connector
def connect_to_db():
    global db
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )
    global cursor
    cursor = db.cursor()
    print("Connected to MySQL")

# Function to create a table
def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS users (regNo INT PRIMARY KEY, username VARCHAR(255))")
    db.commit()

# Function to insert data into the table
def save_data():
    regNo = regNo_entry.get()
    username = username_entry.get()
    cursor.execute("INSERT INTO users (regNo, username) VALUES (%s, %s)", (regNo, username))
    db.commit()
    print("Data saved successfully")

# Function to search data based on registration number
def search_data():
    regNo = regNo_entry.get()
    cursor.execute("SELECT * FROM users WHERE regNo = %s", (regNo,))
    result = cursor.fetchone()
    if result:
        username_entry.delete(0, tk.END)
        username_entry.insert(tk.END, result[1])
    else:
        username_entry.insert(tk.END, "Error")
        print("No such registration number found")

# Function to show all data from the table
def show_all_data():
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    for row in result:
        print(row)

# Function to delete data based on registration number
def delete_data():
    regNo = regNo_entry.get()
    cursor.execute("DELETE FROM users WHERE regNo = %s", (regNo,))
    db.commit()
    print("Data deleted successfully")

# Initialize tkinter
root = tk.Tk()
root.title("MySQL GUI Program")

# Connect to MySQL database
connect_to_db()

# Create table (if not exists)
create_table()

# GUI elements
regNo_label = tk.Label(root, text="Registration Number:")
regNo_label.grid(row=0, column=0, padx=10, pady=10)
regNo_entry = tk.Entry(root)
regNo_entry.grid(row=0, column=1, padx=10, pady=10)

username_label = tk.Label(root, text="Username:")
username_label.grid(row=1, column=0, padx=10, pady=10)
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1, padx=10, pady=10)

# Buttons
save_button = tk.Button(root, text="Save",bg="lightgreen", command=save_data)
save_button.grid(row=2, column=0, padx=10, pady=10)

search_button = tk.Button(root, text="Search", command=search_data)
search_button.grid(row=2, column=1, padx=10, pady=10)

show_all_button = tk.Button(root, text="Show All", command=show_all_data)
show_all_button.grid(row=3, column=0, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete",bg="red", command=delete_data)
delete_button.grid(row=3, column=1, padx=10, pady=10)

# Start the tkinter main loop
root.mainloop()
