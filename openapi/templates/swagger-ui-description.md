### Authentication Options

All API endpoints require authentication. There are two ways to authenticate.

#### Session authentication

You may authenticate via the login page in your browser.

This is recommended for trying the API on this page.
**[Log in (opens in new tab)]({% url 'account_login' %}?next={% url 'openapi:swagger' %})**

#### Token authentication

You may also authenticate with an API Token.

There are 3 ways to get an API Token:

- If you have a staff account, you may [**get a Token from the Admin Panel**]({% url 'admin:index' %}authtoken/tokenproxy/)
- If you have a username/password, you may use the `{% url 'rest_login' %}` endpoint (see documentation below).
- All others, use the `{% url 'rest_login_google' %}` endpoint (see documentation below).

Once you got the token, provide it with all API requests as a Bearer token, using this header:\n

```
Authorization: Bearer <token>
```

On this page, you may include the API Token by using the **Authorize** button below.

### License
