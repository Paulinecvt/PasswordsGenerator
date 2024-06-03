from flask import Flask, render_template, request
import random
import string
app = Flask(__name__)


def generate_password(length, use_Digits=True, use_Specials=True, use_Uppercase=True, use_Lowercase=True): # Set default values for the parameters
    # Define the character sets
    length = request.form.get("length")
    digits = string.digits
    specials = string.punctuation
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase

    # Error handling
    if length < 1:
        raise ValueError("The length of the password must be at least 1")
    else:
        length = int(length)

    # Initialize the character set
    charset = ""

    # Error 
    if not use_Digits and not use_Specials and not use_Uppercase and not use_Lowercase:
        raise ValueError("Please select at least one character set")

    # Add the character sets to the charset
    if use_Digits:
        charset += digits

    if use_Specials:
        charset += specials

    if use_Uppercase:
        charset += uppercase

    if use_Lowercase:
        charset += lowercase

    # Generate the password
    password = "".join(random.choice(charset) for i in range(length))
    return password




@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST", "GET"])
def generate():
    if request.method == 'POST':
        length = int(request.form.get("length"))
        use_Digits = request.form.get("Digits").lower() == "on"
        use_Specials = request.form.get("Specials").lower() == "on"
        use_Uppercase = request.form.get("Uppercase").lower() == "on"
        use_Lowercase = request.form.get("Lowercase").lower() == "on"
        password = generate_password(length, use_Digits, use_Specials, use_Uppercase, use_Lowercase)
        return render_template("index.html", password=password)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)