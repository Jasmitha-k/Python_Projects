import qrcode

# Data to encode in the QR code
data = "https://github.com/Jasmithakaja"

# Create a QR Code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 is smallest, 40 is largest)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Thickness of the border
)

# Add data to the QR Code
qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("qrcode.png")

print("QR Code has been generated and saved as 'qrcode.png'")
