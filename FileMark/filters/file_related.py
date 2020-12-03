from FileMark.model import FileOrDirectory


def contains_name(query: str, f: FileOrDirectory, case_sensitive=False):
    return not query \
           or (query and (
            (case_sensitive and query in f.name)
            or (not case_sensitive and query.lower() in f.name.lower())
    ))


def find_ext(query: str, f: FileOrDirectory, case_sensitive=False, match_full=True):
    print(f.ext)
    return \
        not query or (query and (
                match_full and (
                (case_sensitive and f.ext == query)
                or (not case_sensitive and f.ext.lower() == query.lower())
        )
        ) or (
                              not match_full and (
                              (case_sensitive and query in f.ext)
                              or (not case_sensitive and query.lower() in f.ext.lower())
                      )
                      ))
