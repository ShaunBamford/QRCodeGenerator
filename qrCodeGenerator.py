# A simple QR code generator made in python

# Importing libaries for future use
import qrcode
import image
import os
import validators

# Setting up the QR code template
qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)

link = ""

# Creating a function that asks the user to enter the URL they wish to create a QR code for
def grabUserLink():
    # Putting the user into a loop until they have entered a valid URL to meet the condition
    while True:
        link = input("Enter a valid URL\n> ") 
        # Validators libary will check if the URL is valid and will either return a TRUE or FALSE value
        validation = validators.url(link)
        # If the link is valid then leave the while loop
        if validation:
            break
        # Otherwise keep asking user for URL
        else:
            print("That URL is not valid, please try again")

# Creating a function that will add data to the QR code and save it as an image in the current directory of the running program
def createQRCode():
    qr.add_data(link)
    qr.make(fit = True)
    img = qr.make_image(fill="black", back_color = "white")
    # Save the QR code as a .PNG file
    img.save("QrCode.png")
    # Using the OS libary, output the current directory to user
    print(f"Image has been saved to {os.getcwd()}")

grabUserLink()
createQRCode()
