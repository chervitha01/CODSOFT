import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        
        self.contacts = {}
        
        # Labels and Entry widgets
        self.name_label = tk.Label(root, text="Name:")
        self.name_entry = tk.Entry(root)
        
        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_entry = tk.Entry(root)
        
        # Listbox to display contacts
        self.contact_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        
        # Buttons
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        
        # Grid layout
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.contact_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
        
        self.add_button.grid(row=3, column=0, pady=10)
        self.delete_button.grid(row=3, column=1, pady=10)
        
        # Binding listbox selection to a function
        self.contact_listbox.bind('<<ListboxSelect>>', self.display_selected_contact)
        
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        
        if name and phone:
            self.contacts[name] = phone
            self.update_contact_listbox()
            self.clear_entry_fields()
        else:
            messagebox.showwarning("Warning", "Please enter both name and phone number.")
    
    def delete_contact(self):
        selected_contact_index = self.contact_listbox.curselection()
        if selected_contact_index:
            selected_contact = self.contact_listbox.get(selected_contact_index)
            del self.contacts[selected_contact]
            self.update_contact_listbox()
            self.clear_entry_fields()
        else:
            messagebox.showwarning("Warning", "Please select a contact to delete.")
    
    def update_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, contact)
    
    def display_selected_contact(self, event):
        selected_contact_index = self.contact_listbox.curselection()
        if selected_contact_index:
            selected_contact = self.contact_listbox.get(selected_contact_index)
            phone_number = self.contacts[selected_contact]
            
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, selected_contact)
            
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, phone_number)
    
    def clear_entry_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
