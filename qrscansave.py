import sqlite3

def init_db():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('qr_scanner.db')
    cursor = conn.cursor()

    # Create a table to store scanned QR data (if it doesn't already exist)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS qr_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        qr_content TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Commit and close the connection
    conn.commit()
    conn.close()


import cv2
from pyzbar import pyzbar
import sqlite3

# Function to initialize the SQLite database
def init_db():
    conn = sqlite3.connect('qr_scanner.db')
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS qr_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        qr_content TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    conn.commit()
    conn.close()

# Function to save scanned data to the database
def save_to_db(qr_data):
    conn = sqlite3.connect('qr_scanner.db')
    cursor = conn.cursor()

    # Insert the QR code data into the table
    cursor.execute('INSERT INTO qr_data (qr_content) VALUES (?)', (qr_data,))

    conn.commit()
    conn.close()

# Function to decode the QR code from the frame
def decode_qr(frame):
    qr_codes = pyzbar.decode(frame)
    
    for qr_code in qr_codes:
        x, y, w, h = qr_code.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        qr_data = qr_code.data.decode('utf-8')
        qr_type = qr_code.type

        # Display the decoded QR code data
        text = f'{qr_data} ({qr_type})'
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Save the scanned QR data to the database
        save_to_db(qr_data)
        print(f'Decoded and saved QR code: {qr_data}')

    return frame

# Function to start the QR scanner
def start_qr_scanner():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video source.")
        return

    print("QR Code Scanner started. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture image.")
            break

        # Decode the QR codes in the frame and save to the database
        frame = decode_qr(frame)

        # Display the frame
        cv2.imshow('QR Code Scanner', frame)

        # Exit the scanner by pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture when done
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # Initialize the database and start the QR code scanner
    init_db()
    start_qr_scanner()

import sqlite3

def fetch_data():
    conn = sqlite3.connect('qr_scanner.db')
    cursor = conn.cursor()

    # Fetch all rows from the qr_data table
    cursor.execute('SELECT * FROM qr_data')
    rows = cursor.fetchall()

    for row in rows:
        print(f'ID: {row[0]}, QR Content: {row[1]}, Timestamp: {row[2]}')

    conn.close()

# Call this function to see the stored data
fetch_data()
