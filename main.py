import tkinter as tk
import json
import os


def submit():
    global usersData, log, passw, loginEntry, passwordEntry

    login = log.get()
    password = passw.get()

    if login in usersData and usersData[login]['password'] == password:
        print(f"Успешный вход: {login}")
    else:
        print("Неверный логин или пароль")

    loginEntry.delete(0, tk.END)
    passwordEntry.delete(0, tk.END)


def showregistrationFrame():
    global loginFrame, root, usersData

    login = tk.StringVar()
    password = tk.StringVar()

    registrFrame = tk.Frame(root, bg="#fff")

    tk.Label(registrFrame, text="Логин:").pack()
    registrLoginEntry = tk.Entry(registrFrame, justify="center", textvariable=login, bg="#fff")
    registrLoginEntry.pack()

    tk.Label(registrFrame, text="Пароль:").pack()
    registrPasswordEntry = tk.Entry(registrFrame, justify="center", textvariable=password, bg="#fff", show="*")
    registrPasswordEntry.pack()

    submitButton = tk.Button(registrFrame, text="Регистрация", command=lambda: createUser(login, password, registrFrame))
    submitButton.pack()

    backButton = tk.Button(registrFrame, text="Назад", command=lambda: backToLogin(registrFrame))
    backButton.pack()

    loginFrame.pack_forget()
    registrFrame.pack()


def createUser(login, password, registrFrame):
    global usersData

    login_val = login.get()
    password_val = password.get()

    if login_val in usersData:
        print("Пользователь уже существует!")
        return

    usersData[login_val] = {
        'password': password_val
    }
    saveUsersData()
    print(f"Пользователь {login_val} зарегистрирован!")
    backToLogin(registrFrame) 


def saveUsersData():
    global usersData
    with open("users_data.json", "w", encoding="utf-8") as file:
        json.dump(usersData, file, ensure_ascii=False, indent=2)


def loadUsersData():
    global usersData
    if os.path.exists("users_data.json") and os.path.getsize("users_data.json") > 0:
        try:
            with open("users_data.json", "r", encoding="utf-8") as file:
                usersData = json.load(file)
        except json.JSONDecodeError:
            usersData = {}
            saveUsersData()
    else:
        usersData = {}
        saveUsersData()


def backToLogin(registrFrame):
    global loginFrame
    registrFrame.destroy()
    loginFrame.pack()


def showLoginFrame():
    global loginFrame, passw, log, loginEntry, passwordEntry, root

    loginFrame = tk.Frame(root)
    passw = tk.StringVar()
    log = tk.StringVar()

    tk.Label(loginFrame, text="Логин:").pack()
    loginEntry = tk.Entry(loginFrame, justify="center", textvariable=log)
    loginEntry.pack()

    tk.Label(loginFrame, text="Пароль:").pack()
    passwordEntry = tk.Entry(loginFrame, justify="center", textvariable=passw, show="*")
    passwordEntry.pack()

    submitButton = tk.Button(loginFrame, text="Войти", command=submit)
    submitButton.pack()

    registerBtn = tk.Button(loginFrame, text="Регистрация", command=showregistrationFrame)
    registerBtn.pack()

    loginFrame.pack()


def init():
    global root, usersData
    usersData = {}
    loadUsersData()
    root = tk.Tk()
    root.geometry("800x600")
    root.title("БАНКУЕМ ЁПТА")
    showLoginFrame()
    root.mainloop()


if __name__ == '__main__':
    init()
