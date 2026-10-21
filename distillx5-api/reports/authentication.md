# Authentication

- Login is a server-rendered form POST to the application base with `_csrf_token`.
- Session is maintained via HTTP cookies.
- CSRF token is stored in `<meta name="csrf-token">` and sent as `X-CSRF-Token` on same-origin POST/PUT/PATCH/DELETE requests.
- The frontend refreshes the CSRF token from `X-CSRF-Token` response headers or JSON `csrf_token` fields after 419 responses.
- No bearer tokens or API keys were observed in frontend assets.

This documentation does not include credentials or session secrets.
