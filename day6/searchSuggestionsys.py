# LC 1268


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        list_ = []
        products.sort()
        for i, c in enumerate(searchWord):
            products = list(filter(lambda x=x[i] == c if len(x) > i else False, products))
            list_.append(products[:3])
        return list_
