from flask import Flask, send_from_directory
app = Flask(__name__)

def lista_htmliksi(lista):return "<UL>" + "".join("<LI>" + x for x in sorted(lista)) + "</UL>"

@app.route("/")
def oletussivu():
    return send_from_directory('templates', "haku.html")

@app.route("/style.css")
def tyyli():
    return send_from_directory('.', "style.css")

if __name__ == "__main__":
    app.run()
