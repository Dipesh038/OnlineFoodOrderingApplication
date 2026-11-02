def total(price, discount):
    if price < 0 or discount < 0 or discount > 100:
        raise ValueError("Use a positive price and a discount from 0 to 100")
    money_off = price * discount / 100
    new_price = price - money_off
    return new_price

if __name__ == "__main__":
    print("Price after 10% discount:", total(100, 10))
