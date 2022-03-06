# SpeedDater API

REST API for SpeedDater, powered by Django REST Framework.

## Configuration

Configuration is handled via environment variables.

| Environment variable         | Description                                                                | Default                                      |
| ---------------------------- | -------------------------------------------------------------------------- | -------------------------------------------- |
| `CORS_ALLOWED_ORIGINS`       | List of CORS allowed origins. Format: comma-seperated `scheme://host:port` | *blank* (no CORS header unless configured)   |
| `DATABASE_TYPE`              | Database type. `sqlite3` or `postgresql`                                   | `sqlite3`                                    |
| `DATABASE_NAME`              | Database name. If using SQLite, path to file.                              | `db.sqlite3`                                 |
| `DATABASE_HOST`              | Database hostname.                                                         | *blank*                                      |
| `DATABASE_PORT`              | Database port number.                                                      | *blank*                                      |
| `DATABASE_USERNAME`          | Database server username.                                                  | *blank*                                      |
| `DATABASE_PASSWORD`          | Database server password.                                                  | *blank*                                      |
| `DEBUG`                      | Set to `True` to enable Django debug mode                                  | `False`                                      |
| `GOOGLE_OAUTH_CLIENT_ID`     | Google OAuth2 Client ID.                                                   | *blank* (No Google auth unless configured)   |
| `GOOGLE_OAUTH_CLIENT_SECRET` | Google OAuth2 Client Secret.                                               | *blank* (No Google auth unless configured)   |
| `SECRET_KEY`                 | Django secret key.                                                         | *Randomly generated at launch*               |
| `TRUSTED_ORIGINS`            | List of trusted origins. Format: comma-seperated `scheme://host:port`      | *blank* (must configure unless `DEBUG=True`) |

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
