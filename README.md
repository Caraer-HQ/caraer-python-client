# caraer-client

Generated Python client for the [Caraer API](https://v2.api.caraer.com).

This repository is regenerated automatically from the production OpenAPI spec after each Caraer backend production deploy. Hand-written serverless payload helpers in `caraer_client/apps.py` are preserved across regenerations.

## Install

```bash
pip install caraer-client
```

## Docs

- API reference: https://developer.caraer.com
- OpenAPI: https://v2.api.caraer.com/api-docs.yaml

## Auth

Configure the generated API client with a Bearer token (see generated docs after the first codegen publish).

## Serverless app payload types

Import TypedDict helpers for lifecycle / webhook / schedule / inbound / job bodies
(instead of running `caraer apps typegen`):

```python
from caraer_client import LifecyclePayload, WebhookPayload, SchedulePayload
# or: from caraer_client.apps import LifecyclePayload

def handler(request):
    body: LifecyclePayload = request.get("body") or {}
    ...
```

## License

See [LICENSE](LICENSE).
