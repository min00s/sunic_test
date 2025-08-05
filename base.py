modified_code2 = """
    def checkout(user_id, product_id, quantity):
        cart = db.get_cart(user_id)
        cart.remove(product_id, quantity)
        db.update_cart(cart)

        product = db.get_product(product_id)
        if product.stock >= quantity:
            product.stock -= quantity
            db.update_product(product)
            return "구매 완료"
        else:
            return "재고 부족"
"""
