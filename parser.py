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

# For testing
parse_file("test.txt")