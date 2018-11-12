# Before you can use the jobs API, you need to set up an access token.
# Log in to the IBM Q experience. Under "Account", generate a personal 
# access token. Replace 'PUT_YOUR_API_TOKEN_HERE' below with the quoted
# token string. Uncomment the APItoken variable, and you will be ready to go.

#APItoken = 'PUT_YOUR_API_TOKEN_HERE'
APItoken='55b176a88bb0393b003f268cec4c50f73ce52c094db168337f27656600fcd18c787d17c7d122e3a11a1f1dc0b18253120907364209ce4cc100a3c8c7efe0ad7e'

config = {
    'url': 'https://quantumexperience.ng.bluemix.net/api',

    # If you have access to IBM Q features, you also need to fill the "hub",
    # "group", and "project" details. Replace "None" on the lines below
    # with your details from Quantum Experience, quoting the strings, for
    # example: 'hub': 'my_hub'
    # You will also need to update the 'url' above, pointing it to your custom
    # URL for IBM Q.
    'hub': None,
    'group': None,
    'project': None,
}

if 'APItoken' not in locals():
    raise Exception('Please set up your access token. See Qconfig.py.')
