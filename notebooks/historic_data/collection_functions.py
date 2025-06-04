

# This function is for generating the URL for the Alpha Vantage API request from a dictionary of parameters.
def get_av_request_url(request_params):
    
    url = 'https://www.alphavantage.co/query?'

    for i, (key, value) in enumerate(request_params.items()):
        url += f'{key}={value}'
        if i < len(request_params) - 1:
            url += '&'

    return url