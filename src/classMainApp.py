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
        # label = tk.Label(self, text="NOTES MANAGEMENT:", font=("Calibri", 13))
        # label.grid(row=6, column=0, columnspan=4, pady=10)
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

        # For "Add". Button 1:
        btn_add_contact = tk.Button(self, text="Add", command=lambda: AddContactWindow(self, address_book), width=WIDTH, height=HEIGHT)
        btn_add_contact.grid(row=1, column=0, sticky="w", padx=PADX, pady=PADY)

        # For "Search". Button 2:
        btn_search_contact = tk.Button(self, text="Search", command=lambda: SearchContactWindow(self, address_book), width=WIDTH, height=HEIGHT)
        btn_search_contact.grid(row=1, column=1, sticky="e", padx=PADX, pady=PADY)

        # For "Change". Button 3:
        btn_change_contact = tk.Button(self, text="Change", command=lambda: ChangeContactWindow(self, address_book), width=WIDTH, height=HEIGHT)
        btn_change_contact.grid(row=1, column=2, sticky="e", padx=PADX, pady=PADY)

        # For "Delete". Button 4:
        btn_delete_contact = tk.Button(self, text="Delete", command=lambda: DeleteWindow(self, address_book), width=WIDTH, height=HEIGHT)
        btn_delete_contact.grid(row=1, column=3, sticky="e", padx=PADX, pady=PADY)

        # For Other. "Sorting Files":
        btn_sorting_files = tk.Button(self, text="Sorting files", command=self.show_sorting_files_window, width=WIDTH, height=HEIGHT)

        btn_sorting_files.grid(row=10, column=0, sticky="w", padx=PADX, pady=PADY)


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
        window_height = 300
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

        # Text field for entering notes
        self.notes_label = tk.Label(self, text="Notes:")
        self.notes_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)

        self.notes_text = tk.Text(self, width=30, height=5)
        self.notes_text.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)


        self.add_button = tk.Button(self, text="Save", command=self.add_contact, width=10, height=1)
        self.add_button.grid(row=6, column=0, padx=30, pady=10, sticky=tk.W)
        self.cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)
        self.cancel_button.grid(row=6, column=1, padx=30, pady=10, sticky=tk.E)
        # To horizontally align the buttons
        self.add_button.grid(row=6, column=0, padx=30, pady=10, sticky=tk.W, columnspan=2)
    
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

            # Get notes from the Text widget
            notes = self.notes_text.get("1.0", tk.END).strip()

            # Додаємо поле нотаток до об'єкту контакту
            # new_record.add_notes(notes)

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
                if notes:
                    existing_record.notes = notes
            else:
                # If the name does not exist, create a new contact
                new_record = Record(name, birthday)
                if phone:
                    new_record.add_phone(phone)
                if email:
                    new_record.add_email(email)
                if address:
                    new_record.address = address
                if notes:
                    new_record.notes = notes

                self.address_book.add_record(new_record)

            # Save the changes and close the window
            self.address_book.save_to_json("address_book.json")
            messagebox.showinfo("Contact added", f"Contact name: {name}\nPhone number: {phone}\nEmail: {email}\nAddress: {address}\nBirthday: {birthday}")
            self.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))



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
        window_height = 400
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
        self.new_name_entry = tk.Entry(self, textvariable=self.new_name_var, width=33)
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
        self.new_phone_entry = tk.Entry(self, textvariable=self.new_phone_var, width=33)
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
        self.new_email_entry = tk.Entry(self, textvariable=self.new_email_var, width=33)
        self.new_email_entry.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

        # Text field for entering the new address
        self.new_address_label = tk.Label(self, text="New Address:")
        self.new_address_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.E)

        self.new_address_var = tk.StringVar()
        self.new_address_entry = tk.Entry(self, textvariable=self.new_address_var, width=33)
        self.new_address_entry.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)

        # Text field for entering the new birthday
        self.new_birthday_label = tk.Label(self, text="New Birthday:")
        self.new_birthday_label.grid(row=7, column=0, padx=10, pady=5, sticky=tk.E)

        self.new_birthday_var = tk.StringVar()
        self.new_birthday_entry = tk.Entry(self, textvariable=self.new_birthday_var, width=33)
        self.new_birthday_entry.grid(row=7, column=1, padx=10, pady=5, sticky=tk.W)

        # Text field for entering notes
        self.notes_label = tk.Label(self, text="Notes:")
        self.notes_label.grid(row=8, column=0, padx=10, pady=5, sticky=tk.E)

        self.notes_text = tk.Text(self, wrap=tk.WORD, width=25, height=5)
        self.notes_text.grid(row=8, column=1, padx=10, pady=5, sticky=tk.W)



        # Buttons to save changes or cancel
        self.save_button = tk.Button(self, text="Save Changes", command=self.save_changes, width=15, height=1)
        self.save_button.grid(row=9, column=0, padx=10, pady=10, sticky=tk.W)

        self.cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=15, height=1)
        self.cancel_button.grid(row=9, column=1, padx=10, pady=10, sticky=tk.E)

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

                # Update notes
                self.notes_text.delete("1.0", tk.END)
                self.notes_text.insert(tk.END, contact.notes if contact.notes else "")

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

            # Update notes
            notes = self.notes_text.get("1.0", tk.END).strip()
            contact.notes = notes

            # Add the updated contact back to the address book
            self.address_book.add_record(contact)

            # Save changes to the address book
            self.address_book.save_to_json("address_book.json")

            # Close the window
            self.destroy()
        else:
            messagebox.showerror("Error", "Selected contact not found")



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
        delete_contact_window = DeleteContactWindow(self, address_book)

    def delete_phone(self):
        delete_phone_window = DeletePhoneWindow(self, address_book)

    def delete_email(self):
        delete_email_window = DeleteEmailWindow(self, address_book)



class DeleteContactWindow(tk.Toplevel):
    def __init__(self, parent, address_book):
        super().__init__(parent)
        self.title("Delete Contact")
        self.iconbitmap('./img/icon.ico')

        # Setting the window position to the center of the screen
        window_width = 280
        window_height = 100
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

        # Button to delete contact or cancel
        self.delete_button = tk.Button(self, text="Delete", command=self.delete_contact, width=10, height=1)
        self.delete_button.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)
        self.cancel_button.grid(row=1, column=1, padx=10, pady=10, sticky=tk.E)

    def delete_contact(self):
        selected_contact = self.selected_contact_var.get()

        if selected_contact:
            # Delete the selected contact from the address book
            self.address_book.delete(selected_contact)

            messagebox.showinfo("Delete Contact", "Contact deletion successfully completed.")

            # Save changes to the address book
            self.address_book.save_to_json("address_book.json")

            # Close the window
            self.destroy()
        else:
            messagebox.showerror("Error", "Selected contact not found")



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
