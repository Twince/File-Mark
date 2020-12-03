from FileMark.model import FileOrDirectory


def contains_name(query: str, f: FileOrDirectory, case_sensitive=False):
    return (case_sensitive and query in f.name) or (not case_sensitive and query.lower() in f.name.lower())
