import json


def parse_file(filename):
    """Read a recipe file and return the data as a dict{name, body}. 
    Return None on failure.
    """

    try:
        recipe_dict = {}
        with open(filename, "r") as file:
            contents = file.read()
            recipes = contents.split("\n\n\n")
            for recipe in recipes:
                rows = recipe.split("\n")
                name = rows[0]
                recipe_body = "\n".join(rows[1:])
                if not name in recipe_dict.keys():
                    recipe_dict[name] = recipe_body
                else:
                    raise Exception("Recipe with given name already exists.")
        return recipe_dict
    except Exception as e:
        print(e)
        return None


def load_json_file(filename):
    """Read a JSON file and return the data as a dict. 
    Return None on failure.
    """

    try:
        with open(filename, "r") as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(e)
        return None


def write_json_file(filename, data):
    """Write data to the file in JSON format. 
    Return True on success and False on failure.
    """

    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=2)
        return True
    except Exception as e:
        print(e)
        return False


def update_json_file(filename, update, overwrite=False):
    """Update the JSON file with data in update. 
    If overwrite is set, allows overwriting recipes with the same name, 
    else will raise an exception.
    Return True on success and False on failure.
    """

    try:
        data = load_json_file(filename)
        if overwrite:
            data |= update
        else:
            for recipe_name, recipe_body in update.items():
                if recipe_name in data:
                    raise Exception("Duplicate recipe names with overwrite not set.")
                else:
                    data[recipe_name] = recipe_body
        return True
    except Exception as e:
        print(e)
        return False

# Alternative, more in-depth, way to parse recipes. Work in progress.
"""
def parse_file(filename):
    try:
        file = open(filename)
    except:
        return None
    
    try:
        contents = file.read()
        recipes = contents.split("\n\n\n")
        for recipe in recipes:
            categories = {}
            instructions = ""

            parts = recipe.split("\n\n")
            name_amount = parts[0]
            try:
                name, amount = name_amount.split("\n")
            except ValueError:
                name = name_amount
                amount = None
            
            for part in parts[1:]:
                if "\t" in part:  # Only categories have tabs (on ingredients)
                    # Category
                    pass # TODO: handle categories and ingredients
                else:
                    # Instructions
                    instructions += part + "\n\n"
            instructions = instructions[:-2]
    finally:
        file.close()
"""
