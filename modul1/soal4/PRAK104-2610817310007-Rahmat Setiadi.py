shoe_A = 400000
shoe_B = 350000


def calculate_discounted_price(shoe_price, discount_percentage):
    discount_amount = shoe_price * (discount_percentage / 100)
    discounted_price = int(shoe_price - discount_amount)
    return discounted_price


print("Harga Sepatu A: Rp", shoe_A)
print("Harga Sepatu B: Rp", shoe_B)
print(
    "Sepatu A mendapat diskon 13% sehingga harga menjadi Rp",
    calculate_discounted_price(shoe_A, 13),
)
print(
    "Sepatu B mendapat diskon 21% sehingga harga menjadi Rp",
    calculate_discounted_price(shoe_B, 21),
)
