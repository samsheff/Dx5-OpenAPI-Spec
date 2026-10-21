# API Architecture

## Base URLs

- Application base: `https://distillx5.com/archetype/`
- API v1 base: `https://distillx5.com/archetype/api`
- Legacy AJAX endpoints are relative to the application base and use `G_URI_BASE=/archetype/`.

## HTTP Client Layers

1. Legacy jQuery/Knockout layer:
   - `Ajax` wrapper (`assets/js/ajax.js`) uses `XMLHttpRequest`.
   - URLs are relative (`messages`, `inventory/details?id=...`).
   - Responses are HTML or JSON; `AJAX=GET/POST` query flag is appended.
   - CSRF token sent via `X-CSRF-Token` for same-origin state-changing requests.

2. Vue/axios layer:
   - Base `D = ${location.origin}${G_URI_BASE}api`.
   - Endpoints under `api/v1/rest/*` and `api/v1/rpc/*`.
   - Additional non-versioned `/api/*` endpoints for notes, batches, raw materials, orders, etc.

## Authentication

Session-cookie based. State-changing requests require CSRF token. See `authentication.md`.
