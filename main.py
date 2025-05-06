from flask import Flask
import json

with open('candidate.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


app = Flask(__name__)

@app.route("/")
def page_main() :
    result_main = []
    for candidate in data:
        for title, name in candidate.items():
            result_main.append(f"{title}: {name}")
    return f"<pre>{"\n".join(result_main)}</pre>"


@app.route("/candidate/<int:x>")
def  page_candidate(x):
    candidate_result = []
    new_data = data[x]
    for title, name in new_data.items():
        candidate_result.append(f"{title}: {name}")
    return f"<pre>{"\n".join(candidate_result)}</pre>"


@app.route("/skill/<x>")
def page_skill(x):
    skill_result = []
    for candidate in data:
        if x in candidate['Навыки']:
            for title, name in candidate.items():
                skill_result.append(f"{title}: {name}")
    return f"<pre>{"\n".join(skill_result)}</pre>"

app.run()

