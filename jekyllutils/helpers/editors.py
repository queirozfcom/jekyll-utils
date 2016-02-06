def get_executable_from_name(editor_name):
    name = editor_name.lower().strip()

    if name == "sublime":
        return "subl"
    else:
        return editor_name