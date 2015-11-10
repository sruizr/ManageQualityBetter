import os


def get_template_path():
    templates_path = os.getcwd()
    templates_path = os.path.join(templates_path, "mqb",
                                  "test", "templates")
    return templates_path
