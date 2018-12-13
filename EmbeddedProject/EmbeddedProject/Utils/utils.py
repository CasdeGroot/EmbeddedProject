def get_attribute(name, json):
    if name not in json:
        print("Attribute not found error" + name)
        return None

    return json[name]