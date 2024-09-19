def discount_price(price,discount_percent):
    discount_decimal=discount_percent/100;
    if(discount_percent<20):
        return price * 1
    else:
        discount=price * discount_decimal
        final_price=price-discount
        return final_price

price=float(input('Enter price here:\n'));
discount_percent=float(input('Enter discount here:\n'));

print(discount_price(price,discount_percent));
