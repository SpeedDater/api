from rest_framework.authentication import TokenAuthentication


class BearerAuthentication(TokenAuthentication):
    '''
    A token-based authenticator that uses the standard 'Authorization: Bearer' header
    '''
    keyword = 'Bearer'
