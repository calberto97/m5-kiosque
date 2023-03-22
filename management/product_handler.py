from menu import products


def get_product_by_id(id: int):
    for index, dictionary in enumerate(products):
        if (dictionary["_id"] == id):
            return products[index]

    return {}


def get_products_by_type(type: str):
    new_list = []

    for index, dictionary in enumerate(products):
        if (dictionary["type"] == type):
            new_list.append(products[index])
    return new_list
