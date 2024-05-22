# DigiCore Password Manager - v1.0
# Author: Aung Ko Latt (s8111819)
# Purpose: Securely store and manage website/service credentials
# Development Start Date: 2024-05-08

import customtkinter as ct
from tkinter import messagebox

# Define function to create the credential text file if it doesn't exist
def create_credential_file():
    try:
        with open("Secret_Vault.txt", "x") as f:  # Create file in exclusive mode
            f.write("Website/Service\t\t\t\t Username\t\t\t Password\n")  # Add header row
    except FileExistsError:
        pass  # File already exists, no need to create it

# Create the main application window
app = ct.CTk()
ct.set_appearance_mode("dark")  # Set dark mode appearance
ct.set_default_color_theme("blue")
app.geometry("600x350")
app.title("DigiCore Password Manager")

# Create a heading label
title_label = ct.CTkLabel(app, text="DigiCore Password Manager", font=("Google San", 24, "bold"))
title_label.pack(pady=(20, 10))

# Create a frame for input fields
input_frame = ct.CTkFrame(app)
input_frame.pack(fill="x", pady=(40, 40))

# Create labels and entry fields
label_website = ct.CTkLabel(input_frame, text="Website/Service:", font=("Google San", 14, "bold"))
label_website.grid(row=0, column=0, padx=30, pady=5, sticky="w")
entry_website = ct.CTkEntry(input_frame, width=250, height=25)
entry_website.grid(row=0, column=1, padx=30, pady=5)

label_username = ct.CTkLabel(input_frame, text="Username:", font=("Google San", 14, "bold"))
label_username.grid(row=1, column=0, padx=30, pady=5, sticky="w")
entry_username = ct.CTkEntry(input_frame, width=250, height=25)
entry_username.grid(row=1, column=1, padx=30, pady=5)

label_password = ct.CTkLabel(input_frame, text="Password:", font=("Google San", 14, "bold"))
label_password.grid(row=2, column=0, padx=30, pady=5, sticky="w")
entry_password = ct.CTkEntry(input_frame, show="*", width=250, height=25)  # Hide password text
entry_password.grid(row=2, column=1, padx=30, pady=5)

# Define function to add new credentials
def add_credentials():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if not all([website, username, password]):
        messagebox.showinfo("Error", "Please fill in all fields.")
        return

    try:
        with open("Secret_Vault.txt", "a") as f:
            f.write(f"{website}\t\t\t\t{username}\t\t\t{password}\n")
        messagebox.showinfo("Success", "Credentials added successfully!")
        clear_entry_fields()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Define function to view stored credentials
def view_credentials():
    try:
        with open("Secret_Vault.txt", "r") as f:
            contents = f.read()
        if not contents.strip():  # Check if file is empty
            messagebox.showinfo("Information", "No credentials stored yet.")
        else:
            view_window = ct.CTkToplevel()
            view_window.geometry("600x400")
            view_window.title("Stored Credentials")
            text_view = ct.CTkTextbox(view_window)
            text_view.pack(expand=True, fill="both")
            text_view.insert("end", contents)
            view_window.mainloop()
    except FileNotFoundError:
        messagebox.showinfo("Information", "No credential file found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Define function to delete stored credentials
def delete_credentials():
    response = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete all stored credentials?")
    if response:
        try:
            with open("Secret_Vault.txt", "w") as f:
                f.write("Website/Service\t\t\t\tUsername\t\t\tPassword\n")  # Rewrite the header
            messagebox.showinfo("Success", "All credentials have been deleted.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Create buttons for actions
button_frame = ct.CTkFrame(app)
button_frame.pack(pady=10)

button_add = ct.CTkButton(button_frame, text="Add", command=add_credentials, font=("Google San", 13, "bold"), width=100, height=30,)
button_add.pack(side="left", padx=10)

button_view = ct.CTkButton(button_frame, text="View", command=view_credentials, font=("Google San", 13, "bold"), width=100, height=30,)
button_view.pack(side="left", padx=10)

button_delete = ct.CTkButton(button_frame, text="Delete", command=delete_credentials, font=("Google San", 13, "bold"), width=100, height=30,)
button_delete.pack(side="left", padx=10)

button_exit = ct.CTkButton(button_frame, text="Exit", command=app.destroy, font=("Google San", 13, "bold"), width=100, height=30,)
button_exit.pack(side="left", padx=10)

# Create a developer signature
dev_label=ct.CTkLabel(app, text="Developed by AKLATT", font=("Google San", 10,))
dev_label.pack(side="right", padx=45)


# Define function to clear entry fields
def clear_entry_fields():
    entry_website.delete(0, ct.END)
    entry_username.delete(0, ct.END)
    entry_password.delete(0, ct.END)

# Ensure credential file exists
create_credential_file()

# Start the application
app.mainloop()
