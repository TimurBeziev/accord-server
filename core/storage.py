class IStorage:
    @staticmethod
    async def fetch(query):
        print(f'fetched query {query}')
        return query
