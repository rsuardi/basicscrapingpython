class ProductType(object):
    device_type = ""
    product_name = ""

def make_product_type(device_type,product_name):
    product = ProductType()
    product.device_type = device_type
    product.product_name = product_name
    return product