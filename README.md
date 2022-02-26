# SpeedDater407 API

REST API for SpeedDater407, powered by Django REST Framework.

## Configuration

Configuration is handled via environment variables.

| Environment variable | Description                                                           | Required?                        |
| -------------------- | --------------------------------------------------------------------- | -------------------------------- |
| `DEBUG`              | Set to `True` to enable Django debug mode                             | **No**                           |
| `SECRET_KEY`         | Django secret key. Leave blank to use a randomly-generated one.       | **No**                           |
| `TRUSTED_ORIGINS`    | List of trusted origins. Format: comma-seperated `scheme://host:port` | **Yes**, unless DEBUG is enabled |

## License

Licensed under [GNU Affero General Public License, version 3 (AGPLv3)](LICENSE).
