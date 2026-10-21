# Coverage Report

Analyzed:
- HTML entry document and all script tags.
- 44 frontend JavaScript assets under `/assets/js` and `/bundled`.
- Legacy AJAX layer and Vue/axios API calls extracted from bundles.

Not fully analyzed:
- Server-rendered form actions passed as base64 URIs in HTML (not all enumerated).
- Dynamically constructed endpoints where the base path is a runtime value.
- Response/request body schemas (generic only).
- Authenticated runtime traffic (no credentials supplied).

Uncertainty:
- Some method assignments for legacy form endpoints are inferred.
- Some endpoints may be unused or admin-only.
