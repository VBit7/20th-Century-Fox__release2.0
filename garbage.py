

    # # "Add contact"
    # def show_add_contact_window(self, address_book):
    #     add_contact_window = AddContactWindow(self)
    #     add_contact_window.center_window()

    # # "Add phone"
    # def show_add_phone_window(self):
    #     add_phone_window = AddPhoneWindow(self)
    #     add_phone_window.center_window()

    # # "Add email"
    # def show_add_email_window(self):
    #     add_email_window = AddEmailWindow(self)
    #     add_email_window.center_window()

    # # "Add address"
    # def show_add_address_window(self):
    #     add_address_window = AddAddressWindow(self)
    #     add_address_window.center_window()

    # # "Add birthday"
    # def show_add_birthday_window(self):
    #     add_birthday_window = AddBirthdayWindow(self)
    #     add_birthday_window.center_window()


    # # "Search contact"
    # def show_search_contact_window(self):
    #     search_contact_window = SearchContactWindow(self)
    #     search_contact_window.center_window()

    # # "Search phone" - It is unclear whether it is necessary???
    # def search_phone(self):
    #     messagebox.showinfo("Action", "Search phone")

    # # "Search email" - It is unclear whether it is necessary???
    # def search_email(self):
    #     messagebox.showinfo("Action", "Search email")

    # # "Search address" - It is unclear whether it is necessary???
    # def search_address(self):
    #     messagebox.showinfo("Action", "Search address")

    # # "Search birthday" - It is unclear whether it is necessary???
    # def search_birthday(self):
    #     messagebox.showinfo("Action", "Search birthday")


    # # "Change contact"
    # def show_change_contact_window(self):
    #     change_contact_window = ChangeContactWindow(self)
    #     change_contact_window.center_window()

    # # "Change phone"
    # def show_change_phone_window(self):
    #     change_phone_window = ChangePhoneWindow(self)
    #     change_phone_window.center_window()

    # # "Change email"
    # def show_change_email_window(self):
    #     change_email_window = ChangeEmailWindow(self)
    #     change_email_window.center_window()

    # # "Change address"
    # def show_change_address_window(self):
    #     change_address_window = ChangeAddressWindow(self)
    #     change_address_window.center_window()

    # "Change birthday"
    # def show_change_birthday_window(self):
    #     change_birthday_window = ChangeBirthdayWindow(self)
    #     change_birthday_window.center_window()


    # "Delete contact"
    def show_delete_contact_window(self):
        delete_contact_window = DeleteContactWindow(self)
        delete_contact_window.center_window()

    # "Delete phone"
    def show_delete_phone_window(self):
        delete_phone_window = DeletePhoneWindow(self)
        delete_phone_window.center_window()

    # "Delete email"
    def show_delete_email_window(self):
        delete_email_window = DeleteEmailWindow(self)
        delete_email_window.center_window()

    # "Delete address"
    def show_delete_address_window(self):
        delete_address_window = DeleteAddressWindow(self)
        delete_address_window.center_window()

    # "Delete birthday"
    def show_delete_birthday_window(self):
        delete_birthday_window = DeleteBirthdayWindow(self)
        delete_birthday_window.center_window()



class AddPhoneWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Add Phone")
        self.iconbitmap('./img/icon.ico')

        self.user_var = tk.StringVar()
        self.phone_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        phone_label = tk.Label(self, text="Phone:")
        phone_entry = tk.Entry(self, width=30, textvariable=self.phone_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        phone_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.save_phone, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=3, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=3, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def save_phone(self):
        user = self.user_var.get()
        phone = self.phone_var.get()

        # <--  Here, the logic for "Add Phone"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nPhone: {phone}\n")
        self.destroy()


class AddEmailWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Add Email")
        self.iconbitmap('./img/icon.ico')

        self.user_var = tk.StringVar()
        self.email_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        email_label = tk.Label(self, text="Email:")
        email_entry = tk.Entry(self, width=30, textvariable=self.email_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        email_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        email_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.save_email, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=2, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=2, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def save_email(self):
        user = self.user_var.get()
        email = self.email_var.get()

        # <--  Here, the logic for "Add Email"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nEmail: {email}\n")
        self.destroy()


class AddAddressWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Add Address")
        self.iconbitmap('./img/icon.ico')

        self.user_var = tk.StringVar()
        self.address_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        address_label = tk.Label(self, text="Address:")
        address_entry = tk.Entry(self, width=30, textvariable=self.address_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        address_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        address_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.save_address, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=2, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=2, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def save_address(self):
        user = self.user_var.get()
        address = self.address_var.get()

        # <--  Here, the logic for "Add Address"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nAddress: {address}\n")
        self.destroy()


class AddBirthdayWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Add Birthday")
        self.iconbitmap('./img/icon.ico')

        self.user_var = tk.StringVar()
        self.date_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        # Date entry field
        date_label = tk.Label(self, text="Birthday:")
        date_entry = tk.Entry(self, width=30, textvariable=self.date_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        date_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        date_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.save_birthday, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=2, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=2, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def save_birthday(self):
        user = self.user_var.get()
        date = self.date_var.get()

        # <--  Here, the logic for "Add Birthday"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nBirthday: {date}")
        self.destroy()





class ChangePhoneWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Change Phone")
        self.iconbitmap('./img/icon.ico')

        self.user_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.new_phone_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        phone_label = tk.Label(self, text="Phone:")
        phone_entry = tk.Entry(self, width=30, textvariable=self.phone_var)

        new_phone_label = tk.Label(self, text="New Phone:")
        new_phone_entry = tk.Entry(self, width=30, textvariable=self.new_phone_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        phone_entry.grid(row=1, column=1, padx=10, pady=5)

        new_phone_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        new_phone_entry.grid(row=2, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.change_phone, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=5, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=5, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def change_phone(self):
        user = self.user_var.get()
        phone = self.phone_var.get()
        new_phone = self.new_phone_var.get()

        # <--  Here, the logic for "Change Phone"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nPhone: {phone}\nNew Phone: {new_phone}")
        self.destroy()


class ChangeEmailWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Change Email")
        self.iconbitmap('./img/icon.ico')

        self.user_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.new_email_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        email_label = tk.Label(self, text="Email:")
        email_entry = tk.Entry(self, width=30, textvariable=self.email_var)

        new_email_label = tk.Label(self, text="New Email:")
        new_email_entry = tk.Entry(self, width=30, textvariable=self.new_email_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        email_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        email_entry.grid(row=1, column=1, padx=10, pady=5)

        new_email_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        new_email_entry.grid(row=2, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.change_email, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=5, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=5, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def change_email(self):
        user = self.user_var.get()
        email = self.email_var.get()
        new_email = self.new_email_var.get()

        # <--  Here, the logic for "Change Email"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nEmail: {email}\nNew Email: {new_email}")
        self.destroy()


class ChangeAddressWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Change Address")
        self.iconbitmap('./img/icon.ico')

        self.user_var = tk.StringVar()
        self.address_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        address_label = tk.Label(self, text="New Address:")
        address_entry = tk.Entry(self, width=30, textvariable=self.address_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        address_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        address_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.change_address, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=5, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=5, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def change_address(self):
        user = self.user_var.get()
        address = self.address_var.get()

        # <--  Here, the logic for "Change Address"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nNew Address: {address}")
        self.destroy()


class ChangeBirthdayWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Change Birthday")
        self.iconbitmap('./img/icon.ico')

        self.user_var = tk.StringVar()
        self.birthday_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        birthday_label = tk.Label(self, text="New Birthday:")
        birthday_entry = tk.Entry(self, width=30, textvariable=self.birthday_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        birthday_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        birthday_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.change_birthday, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=5, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=5, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def change_birthday(self):
        user = self.user_var.get()
        birthday = self.birthday_var.get()

        # <--  Here, the logic for "Change Birthday"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nNew Birthday: {birthday}")
        self.destroy()




# class DeleteContactWindow(tk.Toplevel):
#     def __init__(self, main_app, *args, **kwargs):
#         tk.Toplevel.__init__(self, main_app, *args, **kwargs)

#         self.title("Delete Contact")
#         self.iconbitmap('./img/icon.ico')

#         self.user_var = tk.StringVar()

#         # Text input fields
#         user_label = tk.Label(self, text="Delete User Name:")
#         user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

#         # Placing widgets on a window
#         user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
#         user_entry.grid(row=0, column=1, padx=10, pady=5)

#         # Buttons "Save" and "Cancel"
#         save_button = tk.Button(self, text="Save", command=self.delete_contact, width=10, height=1)
#         cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

#         save_button.grid(row=1, column=0, sticky="e", padx=30, pady=10)
#         cancel_button.grid(row=1, column=1, sticky="e", padx=30, pady=10)

#     def center_window(self):
#         self.update_idletasks()
#         window_width = self.winfo_width()
#         window_height = self.winfo_height()
#         screen_width = self.winfo_screenwidth()
#         screen_height = self.winfo_screenheight()

#         x = (screen_width - window_width) // 2
#         y = (screen_height - window_height) // 2

#         self.geometry(f'+{x}+{y}')

#     def delete_contact(self):
#         user = self.user_var.get()

#         # <--  Here, the logic for "Delete Contact"
        
#         messagebox.showinfo("Contact Information", f"Delete User: {user}")
#         self.destroy()


# class DeletePhoneWindow(tk.Toplevel):
#     def __init__(self, main_app, *args, **kwargs):
#         tk.Toplevel.__init__(self, main_app, *args, **kwargs)

#         self.title("Delete Phone")
#         self.iconbitmap('./img/icon.ico')

#         self.user_var = tk.StringVar()
#         self.phone_var = tk.StringVar()

#         # Text input fields
#         user_label = tk.Label(self, text="User Name:")
#         user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

#         phone_label = tk.Label(self, text="Delete Phone:")
#         phone_entry = tk.Entry(self, width=30, textvariable=self.phone_var)

#         # Placing widgets on a window
#         user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
#         user_entry.grid(row=0, column=1, padx=10, pady=5)

#         phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
#         phone_entry.grid(row=1, column=1, padx=10, pady=5)

#         # Buttons "Save" and "Cancel"
#         save_button = tk.Button(self, text="Save", command=self.delete_phone, width=10, height=1)
#         cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

#         save_button.grid(row=5, column=0, sticky="e", padx=30, pady=10)
#         cancel_button.grid(row=5, column=1, sticky="e", padx=30, pady=10)

#     def center_window(self):
#         self.update_idletasks()
#         window_width = self.winfo_width()
#         window_height = self.winfo_height()
#         screen_width = self.winfo_screenwidth()
#         screen_height = self.winfo_screenheight()

#         x = (screen_width - window_width) // 2
#         y = (screen_height - window_height) // 2

#         self.geometry(f'+{x}+{y}')

#     def delete_phone(self):
#         user = self.user_var.get()
#         phone = self.phone_var.get()

#         # <--  Here, the logic for "Delete Phone"
        
#         messagebox.showinfo("Contact Information", f"User: {user}\nDelete Phone: {phone}")
#         self.destroy()


# class DeleteEmailWindow(tk.Toplevel):
#     def __init__(self, main_app, *args, **kwargs):
#         tk.Toplevel.__init__(self, main_app, *args, **kwargs)

#         self.title("Delete Email")
#         self.iconbitmap('./img/icon.ico')

#         self.user_var = tk.StringVar()
#         self.email_var = tk.StringVar()

#         # Text input fields
#         user_label = tk.Label(self, text="User Name:")
#         user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

#         email_label = tk.Label(self, text="Delete Email:")
#         email_entry = tk.Entry(self, width=30, textvariable=self.email_var)

#         # Placing widgets on a window
#         user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
#         user_entry.grid(row=0, column=1, padx=10, pady=5)

#         email_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
#         email_entry.grid(row=1, column=1, padx=10, pady=5)

#         # Buttons "Save" and "Cancel"
#         save_button = tk.Button(self, text="Save", command=self.delete_email, width=10, height=1)
#         cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

#         save_button.grid(row=5, column=0, sticky="e", padx=30, pady=10)
#         cancel_button.grid(row=5, column=1, sticky="e", padx=30, pady=10)

#     def center_window(self):
#         self.update_idletasks()
#         window_width = self.winfo_width()
#         window_height = self.winfo_height()
#         screen_width = self.winfo_screenwidth()
#         screen_height = self.winfo_screenheight()

#         x = (screen_width - window_width) // 2
#         y = (screen_height - window_height) // 2

#         self.geometry(f'+{x}+{y}')

#     def delete_email(self):
#         user = self.user_var.get()
#         email = self.email_var.get()

#         # <--  Here, the logic for "Delete Email"
        
#         messagebox.showinfo("Contact Information", f"User: {user}\nDelete Email: {email}")
#         self.destroy()


class DeleteAddressWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Delete Address")
        self.iconbitmap('./img/icon.ico')

        self.user_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.delete_address, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=1, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=1, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def delete_address(self):
        user = self.user_var.get()

        # <--  Here, the logic for "Delete Address"
        
        messagebox.showinfo("Contact Information", f"For User: {user} Address deleted\n")
        self.destroy()


class DeleteBirthdayWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Delete Birthday")
        self.iconbitmap('./img/icon.ico')

        self.user_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.delete_birthday, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=1, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=1, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def delete_birthday(self):
        user = self.user_var.get()

        # <--  Here, the logic for "Delete Birthday"
        
        messagebox.showinfo("Contact Information", f"For User: {user} Birthday deleted\n")
        self.destroy()
