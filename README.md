# SpeedDater407 API

REST API for SpeedDater407, powered by Django REST Framework.

## Configuration

Configuration is handled via environment variables.

| Environment variable         | Description                                                                | Required?                        |
| ---------------------------- | -------------------------------------------------------------------------- | -------------------------------- |
| `CORS_ALLOWED_ORIGINS`       | List of CORS allowed origins. Format: comma-seperated `scheme://host:port` | **No**                           |
| `DEBUG`                      | Set to `True` to enable Django debug mode                                  | **No**                           |
| `GOOGLE_OAUTH_CLIENT_ID`     | Google OAuth2 Client ID                                                    | **Yes**, if using Google sign-in |
| `GOOGLE_OAUTH_CLIENT_SECRET` | Google OAuth2 Client Secret                                                | **Yes**, if using Google sign-in |
| `SECRET_KEY`                 | Django secret key. Leave blank to use a randomly-generated one.            | **No**                           |
| `TRUSTED_ORIGINS`            | List of trusted origins. Format: comma-seperated `scheme://host:port`      | **Yes**, unless DEBUG is enabled |

## Authentication

### Django built-in authentication (username/password)

- Create a superuser
  ```bash
  python3 manage.py createsuperuser
  ```
- Log in to the Admin Panel (`/admin`) as the superuser, and configure other user accounts.

### Sign in with Google

- Create a Django superuser first
- [Get OAuth 2.0 client credentials from Google](https://developers.google.com/identity/protocols/oauth2)
- Configure `GOOGLE_OAUTH_CLIENT_ID` and `GOOGLE_OAUTH_CLIENT_SECRET` (see [Configuration](#configuration))

## License

Licensed under [GNU Affero General Public License, version 3 (AGPLv3)](LICENSE).
