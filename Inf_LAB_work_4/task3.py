import json

def json_to_yaml(json_string):
    json_obj = json.loads(json_string)
    return convert_to_yaml(json_obj)

def convert_to_yaml(obj, indent=-2):
    yaml_str = ""
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, (dict, list)):
                yaml_str += " " * indent + str(key) + ":\n"
                yaml_str += convert_to_yaml(value, indent+2)
            else:
                yaml_str += " " * indent + str(key) + ": " + str(value) + "\n"
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, (dict, list)):
                yaml_str += "-" + convert_to_yaml(item, indent+2)[1::]
            else:
                yaml_str += " " * indent + str(item) + "\n"
    else:
        yaml_str += " " * indent + str(obj) + "\n"
    return yaml_str


# Example usage:
json_str = open("in.json", "r").read()
yaml_str = json_to_yaml(json_str)
open("out_task3.yaml", "w").write(yaml_str)
