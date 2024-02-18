import tkinter
from Email_Manager import EmailManager
from Product_Info_Manager import ProductInfoManager
from tkinter import messagebox

# -FONT-#
FONT = ("helvetica", 15, "normal")
# -COLORS-#
BROWN = "#3E3232"
LIGHT_BROWN = "#7E6363"
ORANGE = "#FF9843"
LIGHT_ORANGE = "#FDE767"
BLACK = "#181a1b"
BEIGE = "#BBAB8C"


# -BUTTON FUNCTIONALITY-#


def register():
    url = url_entry.get()
    email_address = email_entry.get()
    set_price = price_entry.get()
    if url == "" or email_address == "" or set_price == "":
        messagebox.showerror(title="Error", message="Please don't leave any fields empty")
    else:
        with open(file="registration_details.txt", mode="a") as register_file:
            details = f"{url} | {email_address} | {set_price}\n"
            register_file.write(details)
            url_entry.delete(0, len(url))
            price_entry.delete(0, len(set_price))


def check_prices():
    with open(file="registration_details.txt", mode="r") as registration_file:
        registration_details = registration_file.readlines()
        if not registration_details:
            messagebox.showinfo(title="Oops", message="It seems you have not registered yourself.\n"
                                                      "Try filling the details again and then press the register "
                                                      "button")
        else:
            for detail in registration_details:
                user_data = [item.strip() for item in detail.split("|")]
                url = user_data[0]
                email_address = user_data[1]
                set_price = user_data[2]
                print(user_data)
                product_info_manager = ProductInfoManager(product_url=url)
                product_details = product_info_manager.get_product_info()
                cont_or_not = messagebox.askyesno(title="Confirmation Message",
                                                  message=f"Product Name:\n "
                                                          f"{product_details['Product Name'].strip()}\n\n"
                                                          f"Registered E-mail Address: {email_address}\n\n"
                                                          f"Set Price: {set_price}\n\n"
                                                          f"Shall we continue with the following details?")
                if cont_or_not:
                    if product_details["Net Price"] <= float(set_price):
                        email_manager = EmailManager(to_address=email_address,
                                                     product_name=product_details['Product Name'].strip(),
                                                     product_price=product_details["Net Price"])
                        email_manager.send_mail()


# -------#
window = tkinter.Tk()
window.title("Amazon Price Alert")
window.minsize(width=600, height=325)
window.config(bg=BLACK)

logo_canvas = tkinter.Canvas(window, width=110, height=110, highlightthickness=0, background=BLACK)
logo_img = tkinter.PhotoImage(file="amazon-logo.png")
logo_canvas.create_image(55, 55, image=logo_img)
logo_canvas.place(x=20, y=20)

product_url_label = tkinter.Label(window, text="Amazon product URL", background=BLACK, foreground=BEIGE, font=FONT)
product_url_label.place(x=150, y=20)
url_entry = tkinter.Entry(window, background=BEIGE, width=60)
url_entry.place(x=150, y=50)

email_address_label = tkinter.Label(window, text="Enter your e-mail address", background=BLACK, foreground=BEIGE,
                                    font=FONT)
email_address_label.place(x=150, y=90)
email_entry = tkinter.Entry(window, background=BEIGE, width=60)
email_entry.place(x=150, y=120)

price_label = tkinter.Label(window, text="Enter the price ($) below which\nyou are willing to buy the product",
                            background=BLACK, foreground=BEIGE, font=FONT)
price_label.place(x=150, y=160)
price_entry = tkinter.Entry(window, background=BEIGE, width=60)
price_entry.place(x=150, y=210)

register_button = tkinter.Button(window, font=FONT, background=ORANGE, text="Register",
                                 highlightthickness=0, borderwidth=0, width=12, command=register)
register_button.place(x=380, y=260)

check_prices_button = tkinter.Button(window, font=FONT, background=ORANGE, text="Check Prices",
                                     highlightthickness=0, borderwidth=0, command=check_prices)
check_prices_button.place(x=150, y=260)

window.mainloop()
