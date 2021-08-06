import json

from requests import get, put, post, delete, Response


BEAR_URI = "/bear"


class ExpectedStatusCodeError(Exception):
    def __init__(self, response: Response, status_code: int) -> None:
        self.response: Response = response
        self.status_code: int = status_code

    def __str__(self):
        return f'Status code should be `{self.status_code}`. Now is `{self.response.status_code}`'


class Bears:
    def __init__(self, host: str, port: int, bear_uri: str = BEAR_URI) -> None:
        self.resource_url: str = f"http://{host}:{port}"
        self.bears_url: str = f"{self.resource_url}{bear_uri}"

    def get_all_bears(self) -> Response:
        return get(url=self.bears_url)

    def get_bear(self, id_: int) -> Response:
        return get(url=f"{self.bears_url}/{id_}")

    def update_bear(self, id_: int, data: dict) -> Response:
        return put(url=f"{self.bears_url}/{id_}", data=json.dumps(data))

    def delete_all_bears(self) -> Response:
        return delete(url=self.bears_url)

    def delete_bear(self, id_: int) -> Response:
        return get(url=f"{self.bears_url}/{id_}")

    def create_bear(self, data: dict) -> Response:
        return post(url=self.bears_url, data=json.dumps(data))
