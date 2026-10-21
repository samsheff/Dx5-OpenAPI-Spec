# Unresolved Endpoints

- Endpoints whose base URL is a runtime variable (`s.uri`, dynamic action URIs) are not represented as concrete paths.
- Legacy form submission endpoints discovered only as base64-encoded `data-uri` values are not fully enumerated.
- Ambiguous path pairs flagged by validators (e.g. `/api/item/sizes/{id}` vs `/api/item/{id}/suppliers`) are retained as distinct routes.
