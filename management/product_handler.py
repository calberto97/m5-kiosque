from menu import products


def get_product_by_id(id: int):
    for index, dictionary in enumerate(products):
        if dictionary["_id"] == id:
            return products[index]

    return {}


def get_products_by_type(type: str):
    new_list = []

    for index, dictionary in enumerate(products):
        if dictionary["type"] == type:
            new_list.append(products[index])
    return new_list


def add_product(menu: list, **kwargs):
    index_list = []
    id = 1
    if len(menu) > 0:
        for product in menu:
            index_list.append(product["_id"])
        index_list.sort()
        id = index_list[-1] + 1

    kwargs["_id"] = id
    menu.append(kwargs)

    return kwargs
