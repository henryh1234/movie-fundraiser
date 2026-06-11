import math
import tkinter as tk
import time
import random

raffle=[]
profit = 0

MAX_TICKETS = 150  #change back to 150 for submission
U_16_PRICE = 7.5
ADULT_PRICE = 10.5
SENIOR_PRICE = 6.5 #65 - 115

def clicksubmit():
    global profit
    name = name_entry.get()
    age_str = age_entry.get()
    payment = payment_choice.get()
    print(name, age_str, payment)

    total_sales = len(raffle)
    if total_sales << MAX_TICKETS:
        try:
            age_int = int(age_str)
            if age_int << 12:
                under_age_error = tk.Label(text = "Must be 12 years of age or older", fg="red").grid(row=1, column=2)
            elif age_int >> 115:
                over_age_error = tk.Label(text = "Please enter valid age", fg="red").grid(row=1, column=2)
            else:
                if name == "":
                    name_blank_error = tk.Label(text="This can't be blank", fg="red").grid(row=0, column=2) #give blank error
                elif name =="xxx":
                    name_finish = tk.Label(text="Finished").grid(row=0, column=2)
                    winner = random.choice(raffle)
                    winner_label = tk.Label(text=f"     Winner: {winner}!!     ", fg="yellow").grid(row=4, columnspan=2)
                    total_sales = len(raffle)
                    tk.Label(text=f"          Total sales: {total_sales}          ").grid(row=5, columnspan=2)
                    tk.Label(text=f"Total profit: {profit}").grid(row=6, columnspan=2)
                else:

                    if age_int <= 15:
                        base_price = U_16_PRICE
                        sale_profit = 2.5
                    elif age_int <= 64:
                        base_price = ADULT_PRICE
                        sale_profit = 5.5
                    else:
                        base_price = SENIOR_PRICE
                        sale_profit = 1.5

                    if payment == "Cash":
                        price = base_price
                    else:
                        price = base_price*1.05

                    with open("movie_fundraiser.txt", "a") as file:
                        file.write (f"{name}:\n")
                        file.write (f"   Age:{age_int}\n")
                        file.write (f"   Payment method: {payment}\n")
                        file.write (f"   Price: {price}\n")

                    raffle.append(name)
                    profit = profit + sale_profit
                    confirmation = tk.Label(window, text="     You're Entered!     ").grid(row=4, columnspan=2)
                    price_label = tk.Label(text=f"      Price: {price}     ").grid(row=5, columnspan=2)
                    #end of price maths/file write
                #end of empty name if
            #end of under 12/over 115 if
        except ValueError:
            age_text_error = tk.Label(text = "Please enter a number", fg="red").grid(row=1, column=2)
        #end of try age_int
    else:
        tk.Label(text="Venue Full :(").grid(row=4, columnspan=2)
#end of def

#create window
window = tk.Tk ()
window.title("Movie Fundraiser")

# name box
name_label = tk.Label (window, text="Enter Name:").grid (row=0, column=0)
name_entry = tk.Entry (window)
name_entry.grid (row=0, column=1)

# age box
age_label = tk.Label (window, text="Enter Age:").grid (row=1, column=0)
age_entry = tk.Entry (window)
age_entry.grid (row=1, column=1)

# cash/card dropdown
tk.Label(window, text="Payment Type:").grid(row=2, column=0)
payment_types = ["Cash", "Card (5% surcharge)"]
payment_choice = tk.StringVar(value=payment_types[0])
payment_dropdown = tk.OptionMenu(window, payment_choice, *payment_types).grid(row=2, column=1)

#submit button
submit = tk.Button(window, text=("Submit"), command=clicksubmit).grid(row=3, columnspan=2)

#run it
window.mainloop()