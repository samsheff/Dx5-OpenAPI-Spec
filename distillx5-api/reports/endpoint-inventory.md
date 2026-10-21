# Endpoint Inventory

| Method | Path | Feature/Tag | Description | Auth | Source | Confidence |
|---|---|---|---|---|---|---|
| GET | `//batches/allowed-batch-types` | batches | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//batches/available-vessels` | batches | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `//batches/metrics` | batches | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `//containers/overview-settings` | containers | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//containers/overview/1` | containers | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//containers/tib-in-bond` | containers | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//crm/suppliers` | crm | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//inventory/accounting-inventory` | inventory | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `//inventory/add` | inventory | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `//inventory/details` | inventory | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//inventory/items` | inventory | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//inventory/items-with-costs` | inventory | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//inventory/overview` | inventory | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//inventory/overview/alcoholic-flavoring-materials-check` | inventory | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//inventory/overview/client-categories` | inventory | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//inventory/overview/effective-tax-rate-check` | inventory | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//inventory/overview/finished-products` | inventory | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//inventory/reporting-types` | inventory | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `//inventory/transactions/create-revaluation` | inventory | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `//inventory/warehouses` | inventory | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//item` | item | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//item/categories` | item | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `//notes/delete` | notes | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `//operations/barrel-receipts-ib` | operations | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//operations/barrel-receipts-ib-count` | operations | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//operations/batches/details` | operations | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//operations/bulk-receipts-ib` | operations | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//operations/bulk-receipts-ib-count` | operations | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//operations/longterm/bulkbarrelheadcards` | operations | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//operations/lookback-display` | operations | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//operations/packaging` | operations | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//orders/tib` | orders | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `//orders/tib/can-approve` | orders | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `//orders/tib/cancel` | orders | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `//orders/tib/csv-template-barrels` | orders | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//orders/tib/orders-outstanding-containers` | orders | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//orders/tib/return-monitoring` | orders | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `//orders/tib/ship` | orders | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `//orders/tib/status` | orders | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `//orders/tib/undo-shipment` | orders | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `//raw-material-tanks` | raw-material-tanks | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//system/super-user` | system | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//user/all` | user | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `//user/reset-password` | user | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/batches/note/{id}` | batches | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/cache-buster` | api | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `/api/inventory/adjustment-info/{id}` | inventory | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `/api/inventory/sizes/{id}/item-notes-summary` | inventory | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/inventory/sizes/{id}/item-overview-summary` | inventory | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/inventory/sizes/{id}/warehouses/{id}/bonded-summary` | inventory | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/inventory/sizes/{id}/warehouses/{id}/variant-summary` | inventory | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/item/sizes/{id}` | item | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/item/{id}` | api | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/item/{id}/suppliers` | item | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/orders/{id}/info` | orders | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `/api/raw-material-tanks/deactivate/{id}` | raw-material-tanks | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `/api/v1/rest/containers` | rest | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rest/feature-flags` | rest | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rest/inventory-item-info-storage` | rest | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rest/inventory-lots` | rest | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rest/inventory-totals` | rest | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rpc/batches/details` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rpc/batches/details-settings` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rpc/batches/history` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rpc/batches/readings` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rpc/batches/readings/{id}` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rpc/bottling/details` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `/api/v1/rpc/bottling/generate-lot-code` | rpc | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/api/v1/rpc/bottling/run` | rpc | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/api/v1/rpc/bottling/run-settings` | rpc | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/api/v1/rpc/bottling/undo` | rpc | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/api/v1/rpc/bottling/undo-details` | rpc | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `/api/v1/rpc/containers/history` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rpc/containers/source-vessels` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rpc/historical/purchase-orders` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rpc/inventory-ledger/available-lots` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rpc/inventory-ledger/fifo-lots` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rpc/inventory-ledger/recipe-fifo-lots` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rpc/inventory-lots/initialize` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rpc/inventory-reports/barrel-csv-export` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rpc/inventory-reports/barrel-list-view` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rpc/inventory-reports/barrel-overview-filters` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rpc/inventory/available-supplies` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rpc/inventory/finished-product-sizes` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `/api/v1/rpc/inventory/generate-lot-code` | rpc | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/api/v1/rpc/inventory/receive-po` | rpc | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/api/v1/rpc/inventory/receive-settings` | rpc | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/api/v1/rpc/inventory/warehouse-transfer` | rpc | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `/api/v1/rpc/notes` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `/api/v1/rpc/operations/add-ingredient` | rpc | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `/api/v1/rpc/operations/ingredient-list` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rpc/operations/ingredient/{id}` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `/api/v1/rpc/operations/longterm-fill` | rpc | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `/api/v1/rpc/operations/recipe-ingredients/{id}` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rpc/operations/recipe-list` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `/api/v1/rpc/operations/run-recipe` | rpc | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `/api/v1/rpc/orders/details` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `/api/v1/rpc/orders/generate-number` | rpc | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `/api/v1/rpc/orders/product-catalog` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rpc/reports/federal-excise-return/pdf-data` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/api/v1/rpc/reports/federal-excise-return/periods` | rpc | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `/contacts/contactdetails/edit` | contacts | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `/contacts/customerdetails` | contacts | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/contacts/duplicate` | contacts | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/contacts/remove` | contacts | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `/fulfillment/orders` | fulfillment | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/fulfillment/orders/approve-tib-order` | fulfillment | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/fulfillment/orders/cancel-tib-order` | fulfillment | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/fulfillment/orders/changestatus` | fulfillment | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/fulfillment/orders/edit-tib-order` | fulfillment | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/fulfillment/orders/editInvoice` | fulfillment | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/fulfillment/orders/invoice` | fulfillment | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/fulfillment/orders/pullsheet` | fulfillment | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/fulfillment/orders/send-tib-order` | fulfillment | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/fulfillment/orders/ship-tib-order` | fulfillment | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/fulfillment/orders/tib-overview` | fulfillment | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/fulfillment/orders/tibdocument` | fulfillment | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/fulfillment/orders/undo-tib-order` | fulfillment | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/fulfillment/orders/{id}` | fulfillment | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/generic/notes/add` | generic | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/generic/notes/delete` | generic | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/generic/notes/edit` | generic | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `/generic/operations/listactivelongtermbytype` | generic | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/generic/toptabs/calcs` | generic | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/generic/toptabs/calcs/indexedttb4` | generic | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/generic/toptabs/calcs/indexedttb4can` | generic | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/generic/toptabs/favorites/get` | generic | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/generic/toptabs/favorites/reorder` | generic | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `/inventory/add` | inventory | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/inventory/addreporttype` | inventory | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/inventory/bulkcontainer/add` | inventory | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/inventory/categories/add` | inventory | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/inventory/categories/deactivate` | inventory | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `/inventory/details` | inventory | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `/inventory/details/addsize` | inventory | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/inventory/details/addstorage` | inventory | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/inventory/details/addsupplier` | inventory | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `/inventory/details/attach` | inventory | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `/inventory/details/deactivate` | inventory | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/inventory/details/editsize` | inventory | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `/inventory/details/quan` | inventory | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `/inventory/details/reorderedit` | inventory | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/inventory/edit` | inventory | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `/inventory/finishedproducts/details` | inventory | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/inventory/purchaseorders/details` | inventory | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/inventory/reconciliation` | inventory | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `/inventory/valueaddedproducts/package` | inventory | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/inventory/warehouses/transferinventory` | inventory | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `/messages` | messages | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `/operations/barrel-withdrawn-ib` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/operations/barrel-withdrawn-ib-count` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/operations/batches/add` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/operations/batches/addSpirit` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/operations/batches/addrecipe` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/operations/batches/addwater` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/operations/batches/charge` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `/operations/batches/collections` | operations | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/operations/batches/details` | operations | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/operations/batches/distillationcomplete` | operations | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `/operations/batches/dump` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/operations/batches/edit` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/operations/batches/end` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/operations/batches/firestill` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `/operations/batches/listharvestbatchtypes` | operations | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `/operations/batches/metrics` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/operations/batches/recal` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/operations/batches/switchstage` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/operations/batches/transfer` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/operations/batches/unfirestill` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/operations/batches/withdraw` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `/operations/longterm/bulkbarrelheadcards` | operations | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `/operations/longterm/bulkeditbarrels` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/operations/longterm/bulkeditemptybarrels` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/operations/longterm/bulkeditrackhouse` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `/operations/longterm/bulkremovebarrels` | operations | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/operations/packaging` | operations | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/operations/packaging/caselabel` | operations | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/operations/packaging/controlcaselabel` | operations | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/operations/packaging/details` | operations | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `/operations/packaging/edit` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/operations/packaging/filltest` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/operations/packaging/run` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `/operations/pastbatches/advsearch` | operations | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/operations/setup/containers/details` | operations | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| POST | `/operations/spirit-withdrawn-ib` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/operations/spirit-withdrawn-ib-count` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| POST | `/operations/valueaddedproducts/details` | operations | Discovered frontend endpoint | Session cookie + CSRF (POST/PUT/PATCH/DELETE) | bundle-extracted | medium |
| GET | `/sess/cache/get` | sess | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
| GET | `/sess/cache/set` | sess | Discovered frontend endpoint | Session cookie | bundle-extracted | medium |
