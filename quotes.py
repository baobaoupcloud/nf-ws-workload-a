from flask import Flask, render_template
import random

app = Flask(__name__)

# List of motivational quotes
QUOTES = [
    "Believe in yourself! 💪",
    "Good things are coming your way. 🌈",
    "Luck is on your side today! 🍀",
    "You are capable of amazing things. 🚀",
    "Dream big, work hard, stay focused! ⭐",
    "Embrace the journey, not just the destination. 🛤️"
]

# Route for displaying the UI and fetching a new quote
@app.route('/workload-a', methods=['GET'])
def quotes():
    quote = random.choice(QUOTES)  # Get a random quote
    return render_template('quote.html', quote=quote)  # Pass quote to the template

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
