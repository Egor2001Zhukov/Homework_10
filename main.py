from utils import *
from flask import Flask


app = Flask(__name__)


@app.route("/")
def page_home():
    result = ""
    for x in get_all():
        result += f'Имя кандидата - {x["name"]}' + "<br>"
        result += f'Позиция кандидата {x["position"]}' + "<br>"
        result += f'Навыки кандидата {x["skills"]}' + "<br>"
        result += "<br>"
    return f'<pre>{result}</pre>'


@app.route("/candidate/<int:x>")
def page_condidate(x):
    result = '<br>'
    condidate = get_by_pk(x)
    result += condidate["name"] + "<br>"
    result += condidate["position"] + "<br>"
    result += condidate["skills"] + "<br>"
    result += "<br>"
    return f'''
        <img src = "{condidate["picture"]}">
        <pre> {result} </pre>
            '''


@app.route("/skills/<x>")
def page_skills(x):
    return get_by_skill(x)


app.run(debug=True)
