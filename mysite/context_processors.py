import os


def export_vars(requests):
    data={}
    data["DEBUG"] = os.environ["DEBUG"]
    return data