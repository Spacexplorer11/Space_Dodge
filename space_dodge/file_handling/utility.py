import os

file_handling_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(file_handling_dir)


def ref(path):
    path = path.lstrip('/\\')  # remove any leading slashes
    path = path.replace('\\', '/')  # windows backslash to forward slashes, as windows supports both
    return os.path.join(project_dir, path)
