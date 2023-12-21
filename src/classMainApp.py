import tkinter as tk
from tkinter import ttk, messagebox

from src.classAddressBook import AddressBook, Record
# from src import sorter


class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("20th Century Fox Presents")
        self.iconbitmap('./img/icon.ico')
        self.width = 800
        self.height = 600
        self.geometry(f"{self.width}x{self.height}")
        self.center_window()

        # Add lines
        # canvas = tk.Canvas(self, height=1, bg="black")
        # canvas.grid(row=0, column=0, columnspan=4, pady=5, sticky="we")
        # canvas = tk.Canvas(self, height=1, bg="black")
        # canvas.grid(row=6, column=0, columnspan=4, pady=20, sticky="we")
        # canvas = tk.Canvas(self, height=1, bg="black")
        # canvas.grid(row=9, column=0, columnspan=4, pady=20, sticky="we")

        # Add labels
        # label = tk.Label(self, text="  Address Book Management:  ", font=("Helvetica", 12))
        label = tk.Label(self, text="ADDRESS BOOK MANAGEMENT:", font=("Calibri", 13))
        label.grid(row=0, column=0, columnspan=4, pady=10)
        label = tk.Label(self, text="NOTES MANAGEMENT:", font=("Calibri", 13))
        label.grid(row=6, column=0, columnspan=4, pady=10)
        label = tk.Label(self, text="OTHER ACTIONS:", font=("Calibri", 13))
        label.grid(row=9, column=0, columnspan=4, pady=10)

        # Add buttons
        self.add_buttons()

    def center_window(self):        
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def add_buttons(self):
        PADX = 40
        PADY = 5
        WIDTH = 16
        HEIGHT = 2

        # For "Add" Contacts. Group 1:
        # btn_add_contact = tk.Button(self, text="Add", command=self.show_add_contact_window, width=WIDTH, height=HEIGHT)
        btn_add_contact = tk.Button(self, text="Add", command=lambda: AddContactWindow(self, address_book), width=WIDTH, height=HEIGHT)
        # btn_add_phone = tk.Button(self, text="Add phone", command=self.show_add_phone_window, width=WIDTH, height=HEIGHT)
        # btn_add_email = tk.Button(self, text="Add email", command=self.show_add_email_window, width=WIDTH, height=HEIGHT)
        # btn_add_address = tk.Button(self, text="Add address", command=self.show_add_address_window, width=WIDTH, height=HEIGHT)
        # btn_add_birthday = tk.Button(self, text="Add birthday", command=self.show_add_birthday_window, width=WIDTH, height=HEIGHT)

        btn_add_contact.grid(row=1, column=0, sticky="w", padx=PADX, pady=PADY)
        # btn_add_phone.grid(row=2, column=0, sticky="w", padx=PADX, pady=PADY)
        # btn_add_email.grid(row=3, column=0, sticky="w", padx=PADX, pady=PADY)
        # btn_add_address.grid(row=4, column=0, sticky="w", padx=PADX, pady=PADY)
        # btn_add_birthday.grid(row=5, column=0, sticky="w", padx=PADX, pady=PADY)

        # For "Search" Contacts. Group 2:
        # btn_search_contact = tk.Button(self, text="Search contact", command=self.show_search_contact_window, width=WIDTH, height=HEIGHT)
        btn_search_contact = tk.Button(self, text="Search", command=lambda: SearchContactWindow(self, address_book), width=WIDTH, height=HEIGHT)
        # btn_search_phone = tk.Button(self, text="Search phone", command=self.search_phone, width=WIDTH, height=HEIGHT)
        # btn_search_email = tk.Button(self, text="Search email", command=self.search_email, width=WIDTH, height=HEIGHT)
        # btn_search_address = tk.Button(self, text="Search address", command=self.search_address, width=WIDTH, height=HEIGHT)
        # btn_search_birthday = tk.Button(self, text="Search birthday", command=self.search_birthday, width=WIDTH, height=HEIGHT)

        btn_search_contact.grid(row=1, column=1, sticky="e", padx=PADX, pady=PADY)
        # btn_search_phone.grid(row=2, column=1, sticky="e", padx=PADX, pady=PADY)
        # btn_search_email.grid(row=3, column=1, sticky="e", padx=PADX, pady=PADY)
        # btn_search_address.grid(row=4, column=1, sticky="e", padx=PADX, pady=PADY)
        # btn_search_birthday.grid(row=5, column=1, sticky="e", padx=PADX, pady=PADY)

        # For "Change" Contacts. Group 3:
        # btn_change_contact = tk.Button(self, text="Change contact", command=self.show_change_contact_window, width=WIDTH, height=HEIGHT)
        btn_change_contact = tk.Button(self, text="Change", command=lambda: ChangeContactWindow(self, address_book), width=WIDTH, height=HEIGHT)
        # btn_change_phone = tk.Button(self, text="Change phone", command=self.show_change_phone_window, width=WIDTH, height=HEIGHT)
        # btn_change_email = tk.Button(self, text="Change email", command=self.show_change_email_window, width=WIDTH, height=HEIGHT)
        # btn_change_address = tk.Button(self, text="Change address", command=self.show_change_address_window, width=WIDTH, height=HEIGHT)
        # btn_change_birthday = tk.Button(self, text="Change birthday", command=self.show_change_birthday_window, width=WIDTH, height=HEIGHT)

        btn_change_contact.grid(row=1, column=2, sticky="e", padx=PADX, pady=PADY)
        # btn_change_phone.grid(row=2, column=2, sticky="e", padx=PADX, pady=PADY)
        # btn_change_email.grid(row=3, column=2, sticky="e", padx=PADX, pady=PADY)
        # btn_change_address.grid(row=4, column=2, sticky="e", padx=PADX, pady=PADY)
        # btn_change_birthday.grid(row=5, column=2, sticky="e", padx=PADX, pady=PADY)

        # For "Delete" Contacts. Group 4:
        # btn_delete_contact = tk.Button(self, text="Delete contact", command=self.show_delete_contact_window, width=WIDTH, height=HEIGHT)
        btn_delete_contact = tk.Button(self, text="Delete", command=lambda: DeleteWindow(self, address_book), width=WIDTH, height=HEIGHT)
        # btn_delete_phone = tk.Button(self, text="Delete phone", command=self.show_delete_phone_window, width=WIDTH, height=HEIGHT)
        # btn_delete_email = tk.Button(self, text="Delete email", command=self.show_delete_email_window, width=WIDTH, height=HEIGHT)
        # btn_delete_address = tk.Button(self, text="Delete address", command=self.show_delete_address_window, width=WIDTH, height=HEIGHT)
        # btn_delete_birthday = tk.Button(self, text="Delete birthday", command=self.show_delete_birthday_window, width=WIDTH, height=HEIGHT)

        btn_delete_contact.grid(row=1, column=3, sticky="e", padx=PADX, pady=PADY)
        # btn_delete_phone.grid(row=2, column=3, sticky="e", padx=PADX, pady=PADY)
        # btn_delete_email.grid(row=3, column=3, sticky="e", padx=PADX, pady=PADY)
        # btn_delete_address.grid(row=4, column=3, sticky="e", padx=PADX, pady=PADY)
        # btn_delete_birthday.grid(row=5, column=3, sticky="e", padx=PADX, pady=PADY)

        # For "Add" Notes. Group 1:
        btn_add_note = tk.Button(self, text="Add note", command=self.show_add_note_window, width=WIDTH, height=HEIGHT)
        btn_add_tag = tk.Button(self, text="Add tag", command=self.show_add_tag_window, width=WIDTH, height=HEIGHT)

        btn_add_note.grid(row=7, column=0, sticky="w", padx=PADX, pady=PADY)
        btn_add_tag.grid(row=8, column=0, sticky="w", padx=PADX, pady=PADY)

        # For "Search" Notes. Group 2:
        btn_search_note = tk.Button(self, text="Search note", command=self.show_search_note_window, width=WIDTH, height=HEIGHT)
        btn_search_tag = tk.Button(self, text="Search tag", command=self.show_search_tag_window, width=WIDTH, height=HEIGHT)

        btn_search_note.grid(row=7, column=1, sticky="e", padx=PADX, pady=PADY)
        btn_search_tag.grid(row=8, column=1, sticky="e", padx=PADX, pady=PADY)

        # For "Change" Notes. Group 3:
        btn_change_note = tk.Button(self, text="Change note", command=self.show_change_note_window, width=WIDTH, height=HEIGHT)
        btn_change_tag = tk.Button(self, text="Change tag", command=self.show_change_tag_window, width=WIDTH, height=HEIGHT)

        btn_change_note.grid(row=7, column=2, sticky="e", padx=PADX, pady=PADY)
        btn_change_tag.grid(row=8, column=2, sticky="e", padx=PADX, pady=PADY)

        # For "Delete" Notes. Group 4:
        btn_delete_note = tk.Button(self, text="Delete note", command=self.show_delete_note_window, width=WIDTH, height=HEIGHT)
        btn_delete_tag = tk.Button(self, text="Delete tag", command=self.show_delete_tag_window, width=WIDTH, height=HEIGHT)

        btn_delete_note.grid(row=7, column=3, sticky="e", padx=PADX, pady=PADY)
        btn_delete_tag.grid(row=8, column=3, sticky="e", padx=PADX, pady=PADY)

        # For Other. "Sorting Files":
        btn_sorting_files = tk.Button(self, text="Sorting files", command=self.show_sorting_files_window, width=WIDTH, height=HEIGHT)

        btn_sorting_files.grid(row=10, column=0, sticky="w", padx=PADX, pady=PADY)


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


    # "Add note"
    def show_add_note_window(self):
        add_note_window = AddNoteWindow(self)
        add_note_window.center_window()

    # "Add tag"
    def show_add_tag_window(self):
        add_tag_window = AddTagWindow(self)
        add_tag_window.center_window()


    # "Search note"
    def show_search_note_window(self):
        search_note_window = SearchNoteWindow(self)
        search_note_window.center_window()

    # "Search tag"
    def show_search_tag_window(self):
        search_tag_window = SearchTagWindow(self)
        search_tag_window.center_window()


    # "Change note"
    def show_change_note_window(self):
        change_note_window = ChangeNoteWindow(self)
        change_note_window.center_window()

    # "Change tag"
    def show_change_tag_window(self):
        change_tag_window = ChangeTagWindow(self)
        change_tag_window.center_window()


    # "Delete note"
    def show_delete_note_window(self):
        delete_note_window = DeleteNoteWindow(self)
        delete_note_window.center_window()

    # "Delete tag"
    def show_delete_tag_window(self):
        delete_tag_window = DeleteTagWindow(self)
        delete_tag_window.center_window()


    # Other - "Sorting files"
    def show_sorting_files_window(self):
        sorting_files_window = SortingFilesWindow(self)
        sorting_files_window.center_window()



class AddContactWindow(tk.Toplevel):
    def __init__(self, parent, address_book):
        super().__init__(parent)
        self.title("Add Contact")
        self.iconbitmap('./img/icon.ico')

        # Setting the window position to the center of the screen
        window_width = 350
        window_height = 220
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.address_book = address_book

        self.name_label = tk.Label(self, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)

        # List of names for the Combobox
        existing_names = [record.name.name for record in self.address_book.data.values()]
        self.name_var = tk.StringVar()
        self.name_combobox = ttk.Combobox(self, textvariable=self.name_var, values=existing_names, width=37)
        self.name_combobox.set("Select or Enter Name")
        self.name_combobox.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        self.phone_label = tk.Label(self, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

        self.phone_var = tk.StringVar()
        self.phone_entry = tk.Entry(self, textvariable=self.phone_var, width=40)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        self.email_label = tk.Label(self, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)

        self.email_var = tk.StringVar()
        self.email_entry = tk.Entry(self, textvariable=self.email_var, width=40)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        self.address_label = tk.Label(self, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)

        self.address_var = tk.StringVar()
        self.address_entry = tk.Entry(self, textvariable=self.address_var, width=40)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

        self.birthday_label = tk.Label(self, text="Birthday:")
        self.birthday_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)

        self.birthday_var = tk.StringVar()
        self.birthday_entry = tk.Entry(self, textvariable=self.birthday_var, width=40)
        self.birthday_entry.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

        self.add_button = tk.Button(self, text="Save", command=self.add_contact, width=10, height=1)
        self.add_button.grid(row=5, column=0, padx=30, pady=10, sticky=tk.W)

        self.cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)
        self.cancel_button.grid(row=5, column=1, padx=30, pady=10, sticky=tk.E)
        # To horizontally align the buttons
        self.add_button.grid(row=5, column=0, padx=30, pady=10, sticky=tk.W, columnspan=2)
    
    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()
        birthday = self.birthday_var.get()

        # Check if the name is not the default value
        # if name == "Select or Enter Name":
        #     messagebox.showwarning("Warning", "Please select or enter a valid name.")
        #     return

        try:
            # Attempt to retrieve an existing record by name
            existing_record = self.address_book.find(name)

            if existing_record:
                # If the name exists, add phone, email, address, and birthday (if provided)
                if phone:
                    existing_record.add_phone(phone)
                if email:
                    existing_record.add_email(email)
                if address:
                    existing_record.address = address
                if birthday:
                    existing_record.add_birthday(birthday)
            else:
                # If the name does not exist, create a new contact
                new_record = Record(name, birthday)
                if phone:
                    new_record.add_phone(phone)
                if email:
                    new_record.add_email(email)
                if address:
                    new_record.address = address

                self.address_book.add_record(new_record)

            # Save the changes and close the window
            self.address_book.save_to_json("address_book.json")
            messagebox.showinfo("Contact added", f"Contact name: {name}\nPhone number: {phone}\nEmail: {email}\nAddress: {address}\nBirthday: {birthday}")
            self.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))


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



class SearchContactWindow(tk.Toplevel):
    def __init__(self, parent, address_book):
        super().__init__(parent)
        self.title("Search Contact")
        self.iconbitmap('./img/icon.ico')

        # Setting the window position to the center of the screen
        window_width = 1075
        window_height = 320
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")


        self.address_book = address_book

        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("Name", "Phone", "Email", "Address", "Birthday")
        self.tree.heading("#0", text="ID")
        self.tree.column("#0", width=50)
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Address", text="Address")
        self.tree.heading("Birthday", text="Birthday")
        self.tree.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        self.label = tk.Label(self, text="Enter search string:")
        self.label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(self, textvariable=self.search_var, width=40, )
        self.search_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        self.search_button = tk.Button(self, text="Search", command=self.search_contacts, width=16)
        self.search_button.grid(row=2, column=0, columnspan=2, pady=5)

    def search_contacts(self):
    # Очистити вміст Treeview перед новим пошуком
        self.tree.delete(*self.tree.get_children())

        search_string = self.search_var.get()

        found_contacts = self.address_book.find_data_in_book(search_string)

        # Вивести знайдені контакти в Treeview
        if found_contacts:
            for record in found_contacts:
                record_data = {
                    "Name": record.name.name,
                    "Phone": ", ".join(phone.value for phone in record.phones),
                    "Email": ", ".join(email.value for email in record.emails),
                    # "Address": record.address.address if record.address else "N/A",
                    "Address": record.address if record.address else "N/A",
                    "Birthday": str(record.birthday) if record.birthday else "N/A"
                }
                self.tree.insert("", "end", text="ID", values=(record_data["Name"], record_data["Phone"],
                                                                record_data["Email"], record_data["Address"],
                                                                record_data["Birthday"]))
        else:
            # Якщо не знайдено жодного запису, вивести повідомлення
            print("No results found")


class ChangeContactWindow(tk.Toplevel):
    def __init__(self, parent, address_book):
        super().__init__(parent)
        self.title("Change Contact")
        self.iconbitmap('./img/icon.ico')

        # Setting the window position to the center of the screen
        window_width = 400
        window_height = 300
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.address_book = address_book

        # Combo for selecting an existing contact
        self.select_contact_label = tk.Label(self, text="Select Contact:")
        self.select_contact_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)

        existing_contacts = list(self.address_book.data.keys())
        self.selected_contact_var = tk.StringVar()
        self.contact_combobox = ttk.Combobox(self, textvariable=self.selected_contact_var, values=existing_contacts, width=30)
        self.contact_combobox.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        # Text field for entering the new contact name
        self.new_name_label = tk.Label(self, text="New Name:")
        self.new_name_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

        self.new_name_var = tk.StringVar()
        self.new_name_entry = tk.Entry(self, textvariable=self.new_name_var, width=30)
        self.new_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        # Combo for selecting an existing phone number
        self.select_phone_label = tk.Label(self, text="Select Phone:")
        self.select_phone_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)

        self.selected_phone_var = tk.StringVar()
        self.phone_combobox = ttk.Combobox(self, textvariable=self.selected_phone_var, values=[], width=30)
        self.phone_combobox.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        # Text field for entering the new phone number
        self.new_phone_label = tk.Label(self, text="New Phone:")
        self.new_phone_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)

        self.new_phone_var = tk.StringVar()
        self.new_phone_entry = tk.Entry(self, textvariable=self.new_phone_var, width=30)
        self.new_phone_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

        # Combo for selecting an existing email
        self.select_email_label = tk.Label(self, text="Select Email:")
        self.select_email_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)

        self.selected_email_var = tk.StringVar()
        self.email_combobox = ttk.Combobox(self, textvariable=self.selected_email_var, values=[], width=30)
        self.email_combobox.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

        # Text field for entering the new email
        self.new_email_label = tk.Label(self, text="New Email:")
        self.new_email_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)

        self.new_email_var = tk.StringVar()
        self.new_email_entry = tk.Entry(self, textvariable=self.new_email_var, width=30)
        self.new_email_entry.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

        # Text field for entering the new address
        self.new_address_label = tk.Label(self, text="New Address:")
        self.new_address_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.E)

        self.new_address_var = tk.StringVar()
        self.new_address_entry = tk.Entry(self, textvariable=self.new_address_var, width=30)
        self.new_address_entry.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)

        # Text field for entering the new birthday
        self.new_birthday_label = tk.Label(self, text="New Birthday:")
        self.new_birthday_label.grid(row=7, column=0, padx=10, pady=5, sticky=tk.E)

        self.new_birthday_var = tk.StringVar()
        self.new_birthday_entry = tk.Entry(self, textvariable=self.new_birthday_var, width=30)
        self.new_birthday_entry.grid(row=7, column=1, padx=10, pady=5, sticky=tk.W)

        # Buttons to save changes or cancel
        self.save_button = tk.Button(self, text="Save Changes", command=self.save_changes, width=15, height=1)
        self.save_button.grid(row=8, column=0, padx=10, pady=10, sticky=tk.W)

        self.cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=15, height=1)
        self.cancel_button.grid(row=8, column=1, padx=10, pady=10, sticky=tk.E)

        # Bind the event to update phone numbers based on the selected contact
        self.contact_combobox.bind("<<ComboboxSelected>>", self.update_contact_details)

        # Initialize details for the first contact in the list (if available)
        if existing_contacts:
            first_contact = existing_contacts[0]
            self.selected_contact_var.set(first_contact)
            self.update_contact_details()

    def update_contact_details(self, event=None):
        selected_contact = self.selected_contact_var.get()
        if selected_contact:
            contact = self.address_book.find(selected_contact)
            if contact:
                # Update phone numbers
                phone_numbers = [str(phone) for phone in contact.phones]
                self.phone_combobox['values'] = phone_numbers
                if phone_numbers:
                    self.selected_phone_var.set(phone_numbers[0])
                else:
                    self.selected_phone_var.set("")

                # Update emails
                emails = [str(email) for email in contact.emails]
                self.email_combobox['values'] = emails
                if emails:
                    self.selected_email_var.set(emails[0])
                else:
                    self.selected_email_var.set("")

                # Update address
                self.new_address_var.set(contact.address if contact.address else "")

                # Update birthday
                self.new_birthday_var.set(str(contact.birthday) if contact.birthday else "")

    def save_changes(self):
        selected_contact = self.selected_contact_var.get()
        new_name = self.new_name_var.get()
        selected_phone = self.selected_phone_var.get()
        new_phone = self.new_phone_var.get()
        selected_email = self.selected_email_var.get()
        new_email = self.new_email_var.get()
        new_address = self.new_address_var.get()
        new_birthday = self.new_birthday_var.get()

        contact = self.address_book.find(selected_contact)
        if contact:
            # Remove the old contact from the address book
            self.address_book.delete(selected_contact)

            # Update the contact name if a new name is provided
            if new_name:
                contact.name.name = new_name

            # Update the phone number if a new phone number is provided
            if selected_phone and new_phone:
                contact.edit_phone(selected_phone, new_phone)

            # Update the email if a new email is provided
            if selected_email and new_email:
                contact.edit_email(selected_email, new_email)

            # Update the address if a new address is provided
            contact.address = new_address

            # Update the birthday if a new birthday is provided
            if new_birthday:
                contact.add_birthday(new_birthday)

            # Add the updated contact back to the address book
            self.address_book.add_record(contact)

            # Save changes to the address book
            self.address_book.save_to_json("address_book.json")

            # Close the window
            self.destroy()
        else:
            messagebox.showerror("Error", "Selected contact not found")



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



class DeleteWindow(tk.Toplevel):
    def __init__(self, parent, address_book):
        super().__init__(parent)
        self.title("Delete")
        self.iconbitmap('./img/icon.ico')

        # Setting the window position to the center of the screen
        window_width = 400
        window_height = 150
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.address_book = address_book

        # Кнопки
        self.delete_contact_button = tk.Button(self, text="Delete Contact", command=self.delete_contact, width=16, height=2)
        self.delete_contact_button.pack(side=tk.LEFT, padx=10)

        self.delete_phone_button = tk.Button(self, text="Delete Phone", command=self.delete_phone, width=16, height=2)
        self.delete_phone_button.pack(side=tk.LEFT, padx=10)

        self.delete_email_button = tk.Button(self, text="Delete Email", command=self.delete_email, width=16, height=2)
        self.delete_email_button.pack(side=tk.LEFT, padx=10)

    def delete_contact(self):
        messagebox.showinfo("Delete Contact", "Deleting contact functionality will be implemented here.")

    def delete_phone(self):
        delete_phone_window = DeletePhoneWindow(self, address_book)
        # messagebox.showinfo("Delete Phone", "Deleting phone functionality will be implemented here.")

    def delete_email(self):
        delete_email_window = DeleteEmailWindow(self, address_book)
        # messagebox.showinfo("Delete Email", "Deleting email functionality will be implemented here.")




class DeletePhoneWindow(tk.Toplevel):
    def __init__(self, parent, address_book):
        super().__init__(parent)
        self.title("Delete Phone")
        self.iconbitmap('./img/icon.ico')

        # Setting the window position to the center of the screen
        window_width = 280
        window_height = 140
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.address_book = address_book

        # Combo for selecting an existing contact
        self.select_contact_label = tk.Label(self, text="Select Contact:")
        self.select_contact_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)

        existing_contacts = list(self.address_book.data.keys())
        self.selected_contact_var = tk.StringVar()
        self.contact_combobox = ttk.Combobox(self, textvariable=self.selected_contact_var, values=existing_contacts, width=20)
        self.contact_combobox.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        # Combo for selecting an existing phone number
        self.select_phone_label = tk.Label(self, text="Select Phone:")
        self.select_phone_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

        self.selected_phone_var = tk.StringVar()
        self.phone_combobox = ttk.Combobox(self, textvariable=self.selected_phone_var, values=[], width=20)
        self.phone_combobox.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        # Buttons to delete phone or cancel
        self.delete_button = tk.Button(self, text="Delete", command=self.delete_phone, width=10, height=1)
        self.delete_button.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)
        self.cancel_button.grid(row=2, column=1, padx=10, pady=10, sticky=tk.E)

        # Bind the event to update phone numbers based on the selected contact
        self.contact_combobox.bind("<<ComboboxSelected>>", self.update_phone_numbers)

        # Initialize details for the first contact in the list (if available)
        if existing_contacts:
            first_contact = existing_contacts[0]
            self.selected_contact_var.set(first_contact)
            self.update_phone_numbers()

    def update_phone_numbers(self, event=None):
        selected_contact = self.selected_contact_var.get()
        if selected_contact:
            contact = self.address_book.find(selected_contact)
            if contact:
                # Update phone numbers
                phone_numbers = [str(phone) for phone in contact.phones]
                self.phone_combobox['values'] = phone_numbers
                if phone_numbers:
                    self.selected_phone_var.set(phone_numbers[0])
                else:
                    self.selected_phone_var.set("")

    def delete_phone(self):
        selected_contact = self.selected_contact_var.get()
        selected_phone = self.selected_phone_var.get()

        if selected_contact and selected_phone:
            contact = self.address_book.find(selected_contact)
            if contact:
                # Delete the selected phone number from the contact
                contact.remove_phone(selected_phone)

                messagebox.showinfo("Delete Phone", "Phone number deletion successfully completed")

                # Save changes to the address book
                self.address_book.save_to_json("address_book.json")

                # Close the window
                self.destroy()
        else:
            messagebox.showerror("Error", "Selected contact or phone number not found")


class DeleteEmailWindow(tk.Toplevel):
    def __init__(self, parent, address_book):
        super().__init__(parent)
        self.title("Delete Email")
        self.iconbitmap('./img/icon.ico')

        # Setting the window position to the center of the screen
        window_width = 280
        window_height = 140
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.address_book = address_book

        # Combo for selecting an existing contact
        self.select_contact_label = tk.Label(self, text="Select Contact:")
        self.select_contact_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)

        existing_contacts = list(self.address_book.data.keys())
        self.selected_contact_var = tk.StringVar()
        self.contact_combobox = ttk.Combobox(self, textvariable=self.selected_contact_var, values=existing_contacts, width=20)
        self.contact_combobox.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        # Combo for selecting an existing email
        self.select_email_label = tk.Label(self, text="Select Email:")
        self.select_email_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

        self.selected_email_var = tk.StringVar()
        self.email_combobox = ttk.Combobox(self, textvariable=self.selected_email_var, values=[], width=20)
        self.email_combobox.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        # Buttons to delete email or cancel
        self.delete_button = tk.Button(self, text="Delete", command=self.delete_email, width=10, height=1)
        self.delete_button.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)
        self.cancel_button.grid(row=2, column=1, padx=10, pady=10, sticky=tk.E)

        # Bind the event to update emails based on the selected contact
        self.contact_combobox.bind("<<ComboboxSelected>>", self.update_email_addresses)

        # Initialize details for the first contact in the list (if available)
        if existing_contacts:
            first_contact = existing_contacts[0]
            self.selected_contact_var.set(first_contact)
            self.update_email_addresses()

    def update_email_addresses(self, event=None):
        selected_contact = self.selected_contact_var.get()
        if selected_contact:
            contact = self.address_book.find(selected_contact)
            if contact:
                # Update email addresses
                email_addresses = [str(email) for email in contact.emails]
                self.email_combobox['values'] = email_addresses
                if email_addresses:
                    self.selected_email_var.set(email_addresses[0])
                else:
                    self.selected_email_var.set("")

    def delete_email(self):
        selected_contact = self.selected_contact_var.get()
        selected_email = self.selected_email_var.get()

        if selected_contact and selected_email:
            contact = self.address_book.find(selected_contact)
            if contact:
                # Delete the selected email address from the contact
                # contact.edit_email(selected_email, "")
                contact.remove_email(selected_email)

                messagebox.showinfo("Delete Email", "Email address deletion successfully completed.")

                # Save changes to the address book
                self.address_book.save_to_json("address_book.json")

                # Close the window
                self.destroy()
        else:
            messagebox.showerror("Error", "Selected contact or email address not found")





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


# --- For Nones ---

class AddNoteWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Add Note")
        self.iconbitmap('./img/icon.ico')

        self.user_var = tk.StringVar()
        self.note_var = tk.StringVar()
        self.tag_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        note_label = tk.Label(self, text="Note:")
        note_entry = tk.Entry(self, width=30, textvariable=self.note_var)

        tag_label = tk.Label(self, text="Tag:")
        tag_entry = tk.Entry(self, width=30, textvariable=self.tag_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        note_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        note_entry.grid(row=1, column=1, padx=10, pady=5)

        tag_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tag_entry.grid(row=2, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.add_note, width=10, height=1)
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

    def add_note(self):
        user = self.user_var.get()
        note = self.note_var.get()
        tag = self.tag_var.get()

        # <--  Here, the logic for "Add Note"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nNote: {note}\nTag: {tag}")
        self.destroy()


class AddTagWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Add Note")
        self.iconbitmap('./img/icon.ico')

        self.user_var = tk.StringVar()
        self.tag_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        tag_label = tk.Label(self, text="Tag:")
        tag_entry = tk.Entry(self, width=30, textvariable=self.tag_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        tag_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tag_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.add_tag, width=10, height=1)
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

    def add_tag(self):
        user = self.user_var.get()
        tag = self.tag_var.get()

        # <--  Here, the logic for "Add Tag"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nTag: {tag}")
        self.destroy()



class SearchNoteWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Search Note")
        self.iconbitmap('./img/icon.ico')

        self.user_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        # Buttons "Search" and "Cancel"
        save_button = tk.Button(self, text="Search", command=self.show_note_table, width=10, height=1)
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

    def show_note_table(self):
        user = self.user_var.get()

        # <--  Here, the logic for "Search Note"
        
        note_data = {
            "user": user,
            "note": "Lorem ipsum, Lorem ipsum, Lorem ipsum, Lorem ipsum",
            "tags": ["tag1", "tag2"],
        }

        NoteTableWindow(self, note_data)


class SearchTagWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Search Tag")
        self.iconbitmap('./img/icon.ico')

        self.tag_var = tk.StringVar()

        # Text input fields
        tag_label = tk.Label(self, text="Tag:")
        tag_entry = tk.Entry(self, width=30, textvariable=self.tag_var)

        # Placing widgets on a window
        tag_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tag_entry.grid(row=0, column=1, padx=10, pady=5)

        # Buttons "Search" and "Cancel"
        save_button = tk.Button(self, text="Search", command=self.show_tag_table, width=10, height=1)
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

    def show_tag_table(self):
        tag = self.tag_var.get()

        # <--  Here, the logic for "Search Tag"
        
        note_data = {
            "user": "user",
            "note": "Lorem ipsum, Lorem ipsum, Lorem ipsum, Lorem ipsum",
            "tags": [tag, "tag1", "tag2"],
        }

        NoteTableWindow(self, note_data)


class ChangeNoteWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Change Note")
        self.iconbitmap('./img/icon.ico')

        self.user_var = tk.StringVar()
        self.new_note_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        new_note_label = tk.Label(self, text="New Note:")
        new_note_entry = tk.Entry(self, width=30, textvariable=self.new_note_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        new_note_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        new_note_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.change_note, width=10, height=1)
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

    def change_note(self):
        user = self.user_var.get()
        new_note = self.new_note_var.get()

        # <--  Here, the logic for "Change Note"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nNew Note: {new_note}")
        self.destroy()


class ChangeTagWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Change Tag")
        self.iconbitmap('./img/icon.ico')

        self.user_var = tk.StringVar()
        self.tag_var = tk.StringVar()
        self.new_tag_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        tag_label = tk.Label(self, text="Tag:")
        tag_entry = tk.Entry(self, width=30, textvariable=self.tag_var)

        new_tag_label = tk.Label(self, text="New Tag:")
        new_tag_entry = tk.Entry(self, width=30, textvariable=self.new_tag_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        tag_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tag_entry.grid(row=1, column=1, padx=10, pady=5)

        new_tag_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        new_tag_entry.grid(row=2, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.change_tag, width=10, height=1)
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

    def change_tag(self):
        user = self.user_var.get()
        tag = self.tag_var.get()
        new_tag = self.new_tag_var.get()

        # <--  Here, the logic for "Change Tag"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nTag: {tag}\nNew Tag: {new_tag}")
        self.destroy()


class DeleteNoteWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Delete Note")
        self.iconbitmap('./img/icon.ico')

        self.user_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="Delete Note for User:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.delete_note, width=10, height=1)
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

    def delete_note(self):
        user = self.user_var.get()

        # <--  Here, the logic for "Delete Note"
        
        messagebox.showinfo("Information", f"Delete Note for User: {user}")
        self.destroy()


class DeleteTagWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Delete Tag")
        self.iconbitmap('./img/icon.ico')

        self.user_var = tk.StringVar()
        self.tag_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        tag_label = tk.Label(self, text="Delete Tag:")
        tag_entry = tk.Entry(self, width=30, textvariable=self.tag_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        tag_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tag_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.delete_tag, width=10, height=1)
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

    def delete_tag(self):
        user = self.user_var.get()
        tag = self.tag_var.get()

        # <--  Here, the logic for "Delete Tag"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nDelete Tag: {tag}")
        self.destroy()


# --- For Other ---

class SortingFilesWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Sorting Files")
        self.iconbitmap('./img/icon.ico')

        self.path_var = tk.StringVar()

        # Text input fields
        path_label = tk.Label(self, text="Path for Sorting:")
        path_entry = tk.Entry(self, width=30, textvariable=self.path_var)

        # Placing widgets on a window
        path_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        path_entry.grid(row=0, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.sorting_files, width=10, height=1)
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

    def sorting_files(self):
        path_s = self.path_var.get()
        
        # sorter.main(f'sort {path_s}')
        # <--  Here, the logic for "Sorting Files"
        
        messagebox.showinfo("Information", f"Sorting files in a directory: {path_s}")
        self.destroy()



# --- For Show ---
class ContactTableWindow(tk.Toplevel):
    def __init__(self, search_contact_window, contact_data, *args, **kwargs):
        tk.Toplevel.__init__(self, search_contact_window, *args, **kwargs)
        self.title("Contact Information")
        self.iconbitmap('./img/icon.ico')
        self.width = 950
        self.height = 300
        self.geometry(f"{self.width}x{self.height}")
        self.center_window()

        columns_info = {
            "user": {"text": "User", "width": 150},
            "phones": {"text": "Phones", "width": 200},
            "emails": {"text": "Emails", "width": 200},
            "address": {"text": "Address", "width": 200},
            "birthday": {"text": "Birthday", "width": 150}
        }

        tree = ttk.Treeview(self, columns=list(columns_info.keys()), show="headings")

        for col, info in columns_info.items():
            tree.heading(col, text=info["text"])
            tree.column(col, width=info["width"])

        # Adding data to the table
        tree.insert("", "end", values=(contact_data["user"], ", ".join(contact_data["phones"]),
                                       ", ".join(contact_data["emails"]), contact_data["address"],
                                       contact_data["birthday"]))

        tree.pack(padx=10, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')


class NoteTableWindow(tk.Toplevel):
    def __init__(self, search_note_window, note_data, *args, **kwargs):
        tk.Toplevel.__init__(self, search_note_window, *args, **kwargs)
        self.title("Note Information")
        self.iconbitmap('./img/icon.ico')
        self.width = 750
        self.height = 300
        self.geometry(f"{self.width}x{self.height}")
        self.center_window()

        columns_info = {
            "user": {"text": "User", "width": 150},
            "note": {"text": "Notes", "width": 400},
            "tags": {"text": "Tags", "width": 200},
        }

        tree = ttk.Treeview(self, columns=list(columns_info.keys()), show="headings")

        for col, info in columns_info.items():
            tree.heading(col, text=info["text"])
            tree.column(col, width=info["width"])

        # Adding data to the table
        tree.insert("", "end", values=(note_data["user"], note_data["note"],
                                       ", ".join(note_data["tags"])))

        tree.pack(padx=10, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')



address_book = AddressBook()

if __name__ == "__main__":
    # app = MainApplication()
    # app.mainloop()

    # Створення нової адресної книги
    # Якщо файл address_book.json існує, він автоматично буде завантажений
    # book = AddressBook()

    # # Додаємо запис в адресну книгу з рандомними іменем, номером телефону та датою народження
    # user_number = random.randint(100, 999)
    # data_record = Record(f'User-{user_number}')
    # phone_number = ''.join(map(str, [random.randint(0, 9) for _ in range(10)]))
    # data_record.add_phone(phone_number)
    # data_record.add_birthday(generate_random_birthdate())
    # book.add_record(data_record)

    # # # Пошук в адресній книзі по імені користувача
    # # print("Search by username:")
    # # book.find_data_in_book("John")
    # # # Пошук в адресній книзі по номеру телефона
    # # print("Search by phone number:")
    # # book.find_data_in_book("0987654321")

    # # Пошук в адресній книзі по частині імені користувача
    # print("Search by partial username")
    # book.find_data_in_book("Us")
    # # Пошук в адресній книзі по частині номеру телефона
    # print("Search by partial phone number")
    # book.find_data_in_book("4055")

    # # Зберігаємо адресну книгу в файл
    # book.save_to_json("address_book.json")

    print("Good bye!")
