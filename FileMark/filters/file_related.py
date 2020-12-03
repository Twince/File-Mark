from datetime import datetime

from dateutil.relativedelta import relativedelta

from FileMark.model import FileOrDirectory, Directory


def contains_name(query: str, f: FileOrDirectory, case_sensitive=False):
    return not query \
           or (query and (
            (case_sensitive and query in f.name)
            or (not case_sensitive and query.lower() in f.name.lower())
    ))


def find_ext(query: str, f: FileOrDirectory, case_sensitive=False, match_full=True):
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


def in_duration(query: str, f: FileOrDirectory, field="mtime"):
    if not query:
        return True

    assert field in ("mtime", "ctime", "atime")

    delta = relativedelta(seconds=0)
    for x in query.split(" "):
        if x[-1] == "d":
            delta += relativedelta(days=int(x[:-1]))
        elif x[-1] == "w":
            delta += relativedelta(weeks=int(x[:-1]))
        elif x[-1] == "m":
            delta += relativedelta(months=int(x[:-1]))

    val = datetime.utcfromtimestamp(0)
    if field == "ctime":
        val = f.ctime
    elif isinstance(f, Directory):
        return True
    elif field == "mtime":
        val = f.mtime
    elif field == "atime":
        val = f.atime

    return not query or (query and val >= datetime.now() - delta)


def under_size(query: str, f: FileOrDirectory):
    units = ("TB", "GB", "MB", "KB", "B")

    query = query.replace(" ", "").lower()

    val = 0.0
    for i, u in enumerate(units):
        if not val and query.endswith(u.lower()):
            val = float(query[:-len(u)])

        if i != len(units) - 1:
            val *= 1024

    print(val)
    return not query or (query and f.size <= val)
