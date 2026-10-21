# Data Models

The frontend bundles did not expose complete reusable TypeScript/OpenAPI schemas. Response and request bodies are represented in `openapi.yaml` as generic objects with `additionalProperties: true`.

Observable model hints:
- Inventory items, sizes, warehouses, variants, suppliers.
- Batches, containers, batch types, stages.
- Orders, fulfillment/TIB orders, invoices.
- Bottling runs, lot codes.
- Barrels, fills, harvests.
- Notes, messages, caches.
- Reports: federal excise return periods, TTB manual adjustments, COGS, spirit bottled.

Field-level schemas remain uncertain and are intentionally not fabricated.
