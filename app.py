from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://media.giphy.com/media/5Vy3WpDbXXMze/giphy.gif",
    "https://media.giphy.com/media/1HKaikaFqDt7i/giphy.gif",
    "https://media.giphy.com/media/33OrjzUFwkwEg/giphy.gif",
    "https://media.giphy.com/media/jTnGaiuxvvDNK/giphy.gif",
    "https://media.giphy.com/media/WPWrU2AeK3aV2/giphy.gif",
    "https://media.giphy.com/media/FatZQeOFWW8E0/giphy.gif",
    "https://media.giphy.com/media/11bnQmUcjLzy00/giphy.gif",
    "https://media.giphy.com/media/lXCQNy6VTwmk0/giphy.gif"
    "https://media.giphy.com/media/oqWTRKzfFkgsE/giphy.gif"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")