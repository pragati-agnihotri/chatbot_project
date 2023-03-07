from flask import Flask , render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer

app = Flask(__name__,static_url_path='/static')
english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)


# now training the bot with the help of trainer

trainer.train(
    "chatterbot.corpus.english"
)

@app.route("/")
def home():
    return render_template("chatbottemplate.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact", methods=['GET', 'POST','DELETE', 'PATCH'])
def contact():
    return render_template("contact.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))

if __name__== '__main__':
    app.run(debug=True)
