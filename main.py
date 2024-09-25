from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'  # Used for session management and flash messages

# Use either users.db or users_v2.db depending on your preference
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# Database model for Users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    balance = db.Column(db.Float, default=0.0)

# Initialize the database before the first request
@app.before_request
def create_tables():
    app.before_request_funcs[None].remove(create_tables)

    db.create_all()

# Route for homepage to display user balances and forms
@app.route('/')
def index():
    users = User.query.all()  # Retrieve all users from the database
    return render_template('index.html', users=users)

# Route for creating a new user
@app.route('/create_user', methods=['POST'])
def create_user():
    name = request.form['name']
    initial_balance = float(request.form['balance'])

    # Check if user with the same name already exists
    if User.query.filter_by(name=name).first():
        flash(f'User with the name {name} already exists.')
    else:
        # Add a new user to the database with the given initial balance
        new_user = User(name=name, balance=initial_balance)
        db.session.add(new_user)
        db.session.commit()
        flash(f'User {name} created with balance {initial_balance} tokens.')

    return redirect(url_for('index'))

# Route to handle sending tokens between users
@app.route('/send_tokens', methods=['POST'])
def send_tokens():
    sender_name = request.form['sender_name']
    recipient_name = request.form['recipient_name']
    amount = float(request.form['amount'])

    # Retrieve sender and recipient from the database
    sender = User.query.filter_by(name=sender_name).first()
    recipient = User.query.filter_by(name=recipient_name).first()

    # Check if sender and recipient are valid
    if not sender:
        flash(f'Sender {sender_name} does not exist.')
    elif not recipient:
        flash(f'Recipient {recipient_name} does not exist.')
    elif sender.balance < amount:
        flash(f'{sender_name} has insufficient balance to complete the transaction.')
    else:
        # Perform the token transaction
        sender.balance -= amount
        recipient.balance += amount
        db.session.commit()
        flash(f'Transferred {amount} tokens from {sender_name} to {recipient_name}.')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
