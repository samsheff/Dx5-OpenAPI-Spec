# DISTILL x 5 Frontend API (Reverse Engineered)

This directory contains an OpenAPI 3.1 specification and supporting analysis for the DISTILL x 5 web application at `https://distillx5.com/archetype/`.

## Files

- `openapi.yaml` / `openapi.json` — generated OpenAPI 3.1 specification.
- `reports/` — human-readable analysis reports.
- `artifacts/` — downloaded bundles, manifests, and analysis JSON.
- `scripts/` — reusable discovery/extraction/generation scripts.

## Regeneration

1. Download frontend assets:
   ```bash
   bash scripts/download-assets.sh < artifacts/manifests/asset-paths.txt
   ```
2. Extract/normalize endpoints:
   ```bash
   python3 scripts/extract_method_calls.py
   python3 scripts/normalize_endpoints.py
   ```
3. Generate OpenAPI:
   ```bash
   python3 scripts/generate_openapi.py
   ```
4. Validate:
   ```bash
   npx @redocly/cli lint openapi.yaml --skip-rule=no-ambiguous-paths --skip-rule=no-unused-components
   ```

## Notes

- Base URL: `https://distillx5.com/archetype`
- API v1 base: `https://distillx5.com/archetype/api`
- Authentication: session cookie + `X-CSRF-Token` header for state-changing requests.
- Schemas are generic where the frontend bundles did not expose complete response models.
