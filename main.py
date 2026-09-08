# import mysql.connector

# # Connect to MySQL
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",       # replace with your MySQL username
#     password="Manohar123@", # replace with your MySQL password
#     database="bank_system"
# )
# cursor = conn.cursor()

# # Create account
# def create_account(name, initial_balance=0.0):
#     cursor.execute("INSERT INTO accounts (name, balance) VALUES (%s, %s)", (name, initial_balance))
#     conn.commit()
#     print("Account created successfully! ID:", cursor.lastrowid)

# # Deposit
# def deposit(account_id, amount):
#     cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_id = %s", (amount, account_id))
#     cursor.execute("INSERT INTO transactions (account_id, txn_type, amount) VALUES (%s, %s, %s)", (account_id, "Deposit", amount))
#     conn.commit()
#     print("Deposit successful!")

# # Withdraw
# def withdraw(account_id, amount):
#     cursor.execute("SELECT balance FROM accounts WHERE account_id = %s", (account_id,))
#     balance = cursor.fetchone()[0]
#     if balance >= amount:
#         cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_id = %s", (amount, account_id))
#         cursor.execute("INSERT INTO transactions (account_id, txn_type, amount) VALUES (%s, %s, %s)", (account_id, "Withdraw", amount))
#         conn.commit()
#         print("Withdrawal successful!")
#     else:
#         print("Insufficient funds!")

# # Check balance
# def check_balance(account_id):
#     cursor.execute("SELECT balance FROM accounts WHERE account_id = %s", (account_id,))
#     balance = cursor.fetchone()[0]
#     print("Current Balance:", balance)

# # View transaction history
# def view_transactions(account_id):
#     cursor.execute("SELECT txn_id, txn_type, amount, txn_date FROM transactions WHERE account_id = %s", (account_id,))
#     for txn in cursor.fetchall():
#         print(txn)

# # Search account
# def search_account(name):
#     cursor.execute("SELECT * FROM accounts WHERE name LIKE %s", ("%" + name + "%",))
#     for acc in cursor.fetchall():
#         print(acc)

# # Example usage
# if __name__ == "__main__":
#     create_account("Manohar", 5000)
#     deposit(1, 2000)
#     withdraw(1, 1000)
#     check_balance(1)
#     view_transactions(1)
#     search_account("Manohar")

# # Close connection
# cursor.close()
# conn.close()




import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",        # replace with your MySQL username
    password="Manohar123@", # replace with your MySQL password
    database="bank_system"
)
cursor = conn.cursor()

# Functions
def create_account():
    name = input("Enter your name: ")
    initial_balance = float(input("Enter initial deposit: "))
    cursor.execute("INSERT INTO accounts (name, balance) VALUES (%s, %s)", (name, initial_balance))
    conn.commit()
    print(f"Account created successfully for {name}! ID:", cursor.lastrowid)

def deposit():
    acc_id = int(input("Enter account ID: "))
    amount = float(input("Enter deposit amount: "))
    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_id = %s", (amount, acc_id))
    cursor.execute("INSERT INTO transactions (account_id, txn_type, amount) VALUES (%s, %s, %s)", (acc_id, "Deposit", amount))
    conn.commit()
    print("Deposit successful!")

def withdraw():
    acc_id = int(input("Enter account ID: "))
    amount = float(input("Enter withdrawal amount: "))
    cursor.execute("SELECT balance FROM accounts WHERE account_id = %s", (acc_id,))
    balance = cursor.fetchone()[0]
    if balance >= amount:
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_id = %s", (amount, acc_id))
        cursor.execute("INSERT INTO transactions (account_id, txn_type, amount) VALUES (%s, %s, %s)", (acc_id, "Withdraw", amount))
        conn.commit()
        print("Withdrawal successful!")
    else:
        print("Insufficient funds!")

def check_balance():
    acc_id = int(input("Enter account ID: "))
    cursor.execute("SELECT name, balance FROM accounts WHERE account_id = %s", (acc_id,))
    acc = cursor.fetchone()
    print(f"Account Holder: {acc[0]}, Balance: {acc[1]}")

def view_transactions():
    acc_id = int(input("Enter account ID: "))
    cursor.execute("SELECT txn_id, txn_type, amount, txn_date FROM transactions WHERE account_id = %s", (acc_id,))
    for txn in cursor.fetchall():
        print(txn)

def search_account():
    name = input("Enter name to search: ")
    cursor.execute("SELECT * FROM accounts WHERE name LIKE %s", ("%" + name + "%",))
    for acc in cursor.fetchall():
        print(acc)

# Menu-driven interface
def menu():
    while True:
        print("\n--- Bank Account Management System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. View Transactions")
        print("6. Search Account")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            view_transactions()
        elif choice == "6":
            search_account()
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()

# Close connection
cursor.close()
conn.close()
