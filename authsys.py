import mysql.connector

# Připojení k databázi
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydb"
)

# Získání dat formuláře
username = input("Enter your username: ")
password = input("Enter your password: ")

# Příprava a spuštění dotazu
cursor = conn.cursor()
query = "SELECT * FROM users WHERE username='{}' AND password='{}'".format(username, password)
cursor.execute(query)

# Získávání uživatelských dat
result = cursor.fetchone()
if result:
    user_id, username, password, user_type_id = result
    cursor.execute(f"SELECT user_type_name FROM user_types WHERE user_type_id={user_type_id}")
    user_type = cursor.fetchone()[0]
    # Zobrazií profilovou stránku
    print("Welcome, " + username + ". Your user type is " + user_type)
else:
    # Zobrazí přihlašovací formulář s chybovou zprávou
    print("Invalid username or password. Please try again.")
    show_login_form()

cursor.close()
conn.close()