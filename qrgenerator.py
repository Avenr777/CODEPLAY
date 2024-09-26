import qrcode
import os

def generate_qr_code(profile_info, folder_path="output", filename="profile_qr.png"):
    # Ensure the folder exists, create it if it doesn't
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Full path to save the QR code
    file_path = os.path.join(folder_path, filename)

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data (profile info) to the QR code
    qr.add_data(profile_info)
    qr.make(fit=True)

    # Create an image of the QR code
    img = qr.make_image(fill="black", back_color="white")
    
    # Save the QR code as an image file in the specified folder
    img.save(file_path)
    print(f"QR code saved at {file_path}")

# Example usage:
profile_data = {
    "Name": "John Doe",
    "Email": "johndoe@example.com",
    "Phone": "+123456789",
    "Website": "https://johndoe.com"
}

# Convert the dictionary to a formatted string for QR code
profile_info = "\n".join(f"{key}: {value}" for key, value in profile_data.items())

# Specify the folder and filename
generate_qr_code(profile_info, folder_path="C:\\Users\\DELL\\Desktop\\figma codes", filename="john_doe_qr.png")
