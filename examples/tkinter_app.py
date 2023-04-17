import tkinter as tk

class BankApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Bank App")

        # create user selection frame
        user_frame = tk.Frame(self.master)
        user_frame.pack(side=tk.TOP, padx=10, pady=10)

        user_label = tk.Label(user_frame, text="Select user:")
        user_label.pack(side=tk.LEFT)

        self.user_var = tk.StringVar()
        user_select = tk.OptionMenu(user_frame, self.user_var, "User 1", "User 2", "User 3")
        user_select.pack(side=tk.LEFT)

        # create transaction list frame
        transaction_frame = tk.Frame(self.master)
        transaction_frame.pack(side=tk.TOP, padx=10, pady=10)

        transaction_label = tk.Label(transaction_frame, text="Transaction history:")
        transaction_label.pack(side=tk.LEFT)

        self.transaction_text = tk.Text(transaction_frame, width=30, height=10)
        self.transaction_text.pack(side=tk.LEFT)

        # create account actions frame
        account_frame = tk.Frame(self.master)
        account_frame.pack(side=tk.TOP, padx=10, pady=10)

        deposit_button = tk.Button(account_frame, text="Deposit", command=self.deposit_account)
        deposit_button.pack(side=tk.LEFT)

        withdraw_button = tk.Button(account_frame, text="Withdraw", command=self.withdraw_account)
        withdraw_button.pack(side=tk.LEFT)

        modify_button = tk.Button(account_frame, text="Modify", command=self.modify_account)
        modify_button.pack(side=tk.LEFT)

    def deposit_account(self):
        user = self.user_var.get()
        amount = tk.simpledialog.askinteger("Deposit Account", f"Enter deposit amount for {user}:")
        if amount is not None:
            # TODO: deposit to account and update transaction history
            self.transaction_text.insert(tk.END, f"{user}: deposited {amount}\n")

    def withdraw_account(self):
        user = self.user_var.get()
        amount = tk.simpledialog.askinteger("Withdraw Account", f"Enter withdraw amount for {user}:")
        if amount is not None:
            # TODO: withdraw from account and update transaction history
            self.transaction_text.insert(tk.END, f"{user}: withdrew {amount}\n")

    def modify_account(self):
        user = self.user_var.get()
        # TODO: modify account details for selected user
        tk.messagebox.showinfo("Modify Account", f"Modify account details for {user}")

if __name__ == '__main__':
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()