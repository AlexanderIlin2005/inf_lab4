def from_json_to_yaml_by_replacing(json_text):
    json_text = json_text.replace('{', '')
    json_text = json_text.replace('}', '\n')
    json_text = json_text.replace(':', ': ')
    json_text = json_text.replace(',', '\n')
    json_text = json_text.replace('[', '')
    json_text = json_text.replace(']', '')
    yaml_text = json_text

    return yaml_text

json_data = open("in.json", "r", encoding="utf-8").read()
print(from_json_to_yaml_by_replacing(json_data))
