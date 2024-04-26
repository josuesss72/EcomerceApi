

def upload_Entity(item):
    return {
        "id": str(item.get("_id")),
        "productId": item.get("productId"),
        "pathImg": item.get("pathImg")
    }