import tkinter as tk
from tkinter import ttk, messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Email App")

        self.sender_label = ttk.Label(root, text="Sender Email:")
        self.sender_entry = ttk.Entry(root)
        self.sender_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.sender_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        self.password_label = ttk.Label(root, text="Password:")
        self.password_entry = ttk.Entry(root, show="*")
        self.password_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.recipient_label = ttk.Label(root, text="Recipient Email:")
        self.recipient_entry = ttk.Entry(root)
        self.recipient_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.recipient_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        self.subject_label = ttk.Label(root, text="Subject:")
        self.subject_entry = ttk.Entry(root)
        self.subject_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.subject_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        self.message_label = ttk.Label(root, text="Message:")
        self.message_text = tk.Text(root, wrap="word", height=10)
        self.message_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.message_text.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

        self.send_button = ttk.Button(root, text="Send Email", command=self.send_email)
        self.send_button.grid(row=5, column=1, pady=10)

    def send_email(self):
        sender_email = self.sender_entry.get()
        password = self.password_entry.get()
        recipient_email = self.recipient_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", tk.END)

        if not (sender_email and password and recipient_email and subject and message):
            messagebox.showerror("Error", "All fields must be filled.")
            return

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, password)

            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = recipient_email
            msg["Subject"] = subject
            msg.attach(MIMEText(message, "plain"))

            server.sendmail(sender_email, recipient_email, msg.as_string())
            server.quit()

            messagebox.showinfo("Success", "Email sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    app = EmailApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
