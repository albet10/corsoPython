def apply_discount(price, discount):
    # Source - https://stackoverflow.com/a/4187220
# Posted by Matt, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-08, License - CC BY-SA 4.0
#isinstance(price, (int, float)) and not isinstance(x, bool)

    if isinstance (price, (int,float)) or price <= 0.0:
        print('The price should be greater than 0')
    else:
        print('The price should be a number')
    if isinstance (discount, (int,float)) or (discount <= 0.0 and discount > 100.0):
        print('The discount should be between 0 and 100')
    else:
        print('The discount should be a number')

apply_discount(2,25)