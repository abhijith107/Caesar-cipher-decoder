import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from caesar_cipher import caesar_cipher, auto_decrypt

class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher")
        self.root.geometry("600x700")
        self.root.configure(bg="black")
        self.style = ttk.Style()
        self.style.configure("TLabel", background="black", foreground="green", font=("Helvetica", 12))
        self.style.configure("TButton", background="black", foreground="green", font=("Helvetica", 12), borderwidth=1)
        self.style.map("TButton", background=[('active', 'green')])
        self.style.configure("TEntry", fieldbackground="black", foreground="green", font=("Helvetica", 12))
        self.style.configure("TText", background="black", foreground="green", font=("Helvetica", 12))
        self.create_widgets()
        
    def create_widgets(self):
        self.label = ttk.Label(self.root, text="Enter text or upload a file to encrypt/decrypt:")
        self.label.pack(pady=10)
        
        self.text_input = tk.Text(self.root, height=10, width=70, bg="black", fg="green", insertbackground="green", font=("Helvetica", 12))
        self.text_input.pack(pady=10)
        
        self.shift_label = ttk.Label(self.root, text="Enter shift value:")
        self.shift_label.pack(pady=5)
        
        self.shift_entry = ttk.Entry(self.root, width=10)
        self.shift_entry.pack(pady=5)
        
        self.encrypt_button = ttk.Button(self.root, text="Encrypt", command=self.encrypt_text)
        self.encrypt_button.pack(pady=5)
        
        self.decrypt_button = ttk.Button(self.root, text="Decrypt", command=self.decrypt_text)
        self.decrypt_button.pack(pady=5)
        
        self.auto_decrypt_button = ttk.Button(self.root, text="Auto Decrypt", command=self.auto_decrypt_text)
        self.auto_decrypt_button.pack(pady=5)
        
        self.upload_button = ttk.Button(self.root, text="Upload File", command=self.upload_file)
        self.upload_button.pack(pady=5)
        
        self.output_label = ttk.Label(self.root, text="Output:")
        self.output_label.pack(pady=5)
        
        self.text_output = tk.Text(self.root, height=10, width=70, bg="black", fg="green", insertbackground="green", font=("Helvetica", 12))
        self.text_output.pack(pady=10)
        
    def encrypt_text(self):
        text = self.text_input.get("1.0", tk.END).strip()
        shift = self.get_shift_value()
        if text and shift is not None:
            encrypted_text = caesar_cipher(text, shift)
            self.text_output.delete("1.0", tk.END)
            self.text_output.insert(tk.END, encrypted_text)
        else:
            messagebox.showwarning("Input Error", "Please enter text and a valid shift value.")
    
    def decrypt_text(self):
        text = self.text_input.get("1.0", tk.END).strip()
        shift = self.get_shift_value()
        if text and shift is not None:
            decrypted_text = caesar_cipher(text, shift, decrypt=True)
            self.text_output.delete("1.0", tk.END)
            self.text_output.insert(tk.END, decrypted_text)
        else:
            messagebox.showwarning("Input Error", "Please enter text and a valid shift value.")
    
    def auto_decrypt_text(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if text:
            decrypted_text, shift = auto_decrypt(text)
            self.text_output.delete("1.0", tk.END)
            self.text_output.insert(tk.END, f"Decrypted Text: {decrypted_text}\nDetected Shift: {shift}")
        else:
            messagebox.showwarning("Input Error", "Please enter text for auto decryption.")
    
    def upload_file(self):
        file_path = filedialog.askopenfilename(title="Select a text file", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                text = file.read()
            self.text_input.delete("1.0", tk.END)
            self.text_input.insert(tk.END, text)
    
    def get_shift_value(self):
        try:
            return int(self.shift_entry.get().strip())
        except ValueError:
            messagebox.showwarning("Input Error", "Shift value must be an integer.")
            return None

def main():
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
