from interfaces.product_interface import IProduct


def product_Entity(item) -> IProduct:
    return {
        "id": str(item.get("_id")),
        "name": item.get("name"),
        "stock": item.get("stock"),
        "price": item.get("price"),
        "unit_cost": item.get("unit_cost"),
        "category_id": item.get("category_id"),
    }


def products_Entities(entity):
    return [product_Entity(item) for item in entity]
