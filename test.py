from models.utils import convert, unit_per

result = convert('USD', 'NGN', 100)
print(type(result))


unit = unit_per('USD', 'NGN', 100, 119800)
print(type(unit))