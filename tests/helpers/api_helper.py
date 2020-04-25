import requests


class ApiHelper:
    def __init__(self, url: str):
        self.graphql_url = '{}/graphql'.format(url)

    def send_query_request(self, schema: str, values: list, **kwargs):
        resp = requests.post(url=self.graphql_url, json={'query': self.__query_builder(schema, values)})
        if 'code' in kwargs:
            assert resp.status_code == kwargs['code']
            return resp.json()
        return resp

    def send_mutation_request(self):
        raise NotImplementedError

    @classmethod
    def __query_builder(cls, schema: str, values: list):
        return "query {\n" + schema + " {\n" + '\n'.join(values) + "}}"
