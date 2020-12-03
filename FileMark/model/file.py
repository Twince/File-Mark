import os
import traceback

import typing
from datetime import datetime
from os import PathLike

pathLike = typing.Union[str, PathLike]


class AbstractFile:
    name: str
    base: pathLike
    _parent: typing.Any

    def __init__(self, name: str, base: pathLike) -> None:
        self.name = name
        self.base = base

        self._parent = None

    def __repr__(self) -> str:
        return "<{} named `{}` at base `{}`>".format(self.__class__.__name__, self.name, self.base)

    def __hash__(self):
        return hash(self.path)

    @property
    def is_valid(self) -> bool:
        return os.path.exists(self.path)

    @property
    def path(self) -> pathLike:
        return os.path.join(self.base, self.name)

    @property
    def size(self) -> int:
        raise NotImplementedError

    @property
    def parent(self):
        return self._parent or self.assume_parent()

    @property
    def ext(self) -> str:
        return os.path.splitext(self.path)[-1][1:]

    @property
    def ctime(self) -> datetime:
        return datetime.fromtimestamp(os.path.getctime(self.path))

    @classmethod
    def from_path(cls, path: pathLike):
        if path.endswith("/") or path.endswith("\\"):
            path = path[:-1]

        if not os.path.exists(path):
            raise FileNotFoundError("경로 `{}`에서 파일을 찾을 수 없음".format(path))

        return cls(name=os.path.basename(path), base=os.path.dirname(path))

    def set_parent(self, *args, **kwargs):
        raise NotImplementedError

    def assume_parent(self):
        try:
            self._parent = Directory.from_path(os.path.dirname(self.path))
            return self._parent
        except FileNotFoundError:
            return


class Directory(AbstractFile):
    _computed: bool

    def __init__(self, name: str, base: pathLike) -> None:
        super().__init__(name, base)

        self.parent: Directory
        self._children = []
        self._computed = False

    def __iter__(self):
        for ch in self.children:
            yield ch

        raise StopIteration

    @property
    def size(self) -> int:
        return sum(map(lambda x: x.size, self._children))

    @property
    def is_valid(self) -> bool:
        return super(Directory, self).is_valid and os.path.isdir(self.path)

    @property
    def accessible(self) -> bool:
        return os.access(self.path, os.R_OK)

    @property
    def safe_listing(self) -> typing.List[str]:
        if not (self.is_valid and self.accessible):
            return []

        try:
            return os.listdir(self.path)
        except PermissionError:
            return []

    @property
    def children(self) -> typing.List[AbstractFile]:
        if not self._computed or not self._children:
            self._children = self.fetch_children()
        return self._children

    def set_parent(self, directory):
        if not isinstance(directory, Directory) or not directory.is_valid:
            raise NotADirectoryError("상위폴더 `{}`는 폴더가 아닙니다.".format(directory))

        self._parent = directory

    def _fetch_children(self, filter_func=None):
        for path in map(lambda x: os.path.join(self.path, x), self.safe_listing):
            try:
                path = os.path.join(self.path, path)
                obj = Directory.from_path(path) if os.path.isdir(path) else File.from_path(path)
                obj.set_parent(self)

                if not filter_func or (filter_func and filter_func(obj)):
                    yield obj
            except:
                traceback.print_exc()
                pass

    def fetch_children(self, filter_func=None):
        if not self._computed:
            self._children = list(self._fetch_children(filter_func))
            self._computed = True
        return self._children


class File(AbstractFile):
    parent: Directory

    @property
    def size(self) -> int:
        return os.path.getsize(self.path)

    @property
    def mtime(self) -> datetime:
        return datetime.fromtimestamp(os.path.getmtime(self.path))

    @property
    def atime(self) -> datetime:
        return datetime.fromtimestamp(os.path.getatime(self.path))

    def __init__(self, name: str, base: pathLike) -> None:
        super().__init__(name, base)

    @property
    def is_valid(self) -> bool:
        return super(File, self).is_valid and os.path.isfile(self.path)

    def set_parent(self, directory: Directory):
        if not isinstance(directory, Directory) or not directory.is_valid:
            raise NotADirectoryError("상위폴더 `{}`는 폴더가 아닙니다.".format(directory))

        self._parent = directory
        return self


def finder(path: pathLike):
    return (Directory if os.path.isdir(path) else File).from_path(path)
