import requests


def get_load():
    file = requests.get("https://www.jsonkeeper.com/b/AD8L").json()
    return file


def get_all():
    return get_load()


def get_by_pk(pk):
    for x in get_load():
        if pk == x["pk"]:
            return x


def get_by_skill(skill_name):
    result = "<pre>"
    for x in get_all():
        if skill_name.lower() in x["skills"].lower().split(", "):
            result += f'Имя кандидата - {x["name"]}' + "<br>"
            result += f'Позиция кандидата {x["position"]}' + "<br>"
            result += f'Навыки кандидата {x["skills"]}' + "<br>"
            result += "<br>"
    result += "</pre>"
    return result
