import attr
import data
import json
from typing import List, Union
from functools import partial
from runner import Size, Runner


@attr.s(auto_attribs=True)
class Small:
    i: int
    s: str
    f: float
    b: bool


@attr.s(auto_attribs=True)
class Medium:
    inner: List[Small] = attr.Factory(list)


SMALL = Small(**data.args_sm)

MEDIUM = Medium([Small(**d) for d in data.args_md])


def new(size: Size) -> Runner:
    name = 'attrs'
    if size == Size.Small:
        unp = SMALL
    elif size == Size.Medium:
        unp = MEDIUM
    return Runner(name, unp, partial(se, unp), None, partial(astuple, unp), partial(asdict, unp))


def se(obj: Union[Small, Medium]):
    return json.dumps(attr.asdict(obj))


def astuple(obj: Union[Small, Medium]):
    return attr.astuple(obj)


def asdict(obj: Union[Small, Medium]):
    return attr.asdict(obj)
