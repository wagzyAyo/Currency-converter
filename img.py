currency_map = {
    'USD': '/static/images/us.png',
    'AED': '/static/images/uae.pngs'
}

def get_img_url(currency_code):
    '''Get currency img url base on currency code'''
    return currency_map.get(currency_code)