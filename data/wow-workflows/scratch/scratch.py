from enum import StrEnum, auto

from pydantic import BaseModel, Field, HttpUrl


class MyModel(BaseModel):
    url: HttpUrl


m = MyModel(url="https://www.example.com/hi?locale=en_US&namespace=static-us")

print(m.url.query)


def get_url_params(url: HttpUrl) -> dict[str, str]:
    query_string = url.query
    query_params = query_string.split("&")
    print(query_params)

    param_dict = {}
    for p in query_params:
        key_value = p.split("=")
        if len(key_value) > 0:
            param_dict[key_value[0]] = key_value[1]

    return param_dict
