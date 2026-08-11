"""Hand-written serverless / installation payload helpers for Caraer apps.

Preserved across OpenAPI regeneration (see `.openapi-generator-ignore` and
``scripts/client-overlays/`` in the Caraer backend). Prefer these over
per-app ``caraer apps typegen`` output.
"""

from __future__ import annotations

from typing import Any, NotRequired, TypedDict


class SettingFieldValue(TypedDict, total=False):
    name: str
    label: str
    type: str
    value: Any
    defaultValue: Any
    hasValue: bool


class LifecyclePayload(TypedDict, total=False):
    event: str
    timestamp: int | float
    appUuid: str
    appName: str
    appLabel: str
    privateApp: bool
    authMethod: str
    userUuid: str
    companyUuid: str
    installationToken: str
    caraerApiBase: str
    oauthConnected: bool
    settingsSchema: list[SettingFieldValue]
    scopes: list[str]
    settingsChanged: bool
    scopesChanged: bool
    filtersChanged: bool


class WebhookPayload(TypedDict, total=False):
    topic: str
    event: str
    timestamp: int | float
    appUuid: str
    companyUuid: str
    installationToken: str
    caraerApiBase: str
    record: dict[str, Any]
    objectName: str
    settingsSchema: list[SettingFieldValue]


class SchedulePayload(TypedDict, total=False):
    scheduleName: str
    name: str
    appUuid: str
    companyUuid: str
    installationToken: str
    caraerApiBase: str
    scheduledAt: str | int | float
    settingsSchema: list[SettingFieldValue]


class InboundPayload(TypedDict, total=False):
    appUuid: str
    companyUuid: str
    installationToken: str
    caraerApiBase: str
    routeName: str
    body: Any
    headers: dict[str, str]


class JobPayload(TypedDict, total=False):
    jobId: str
    functionName: str
    appUuid: str
    companyUuid: str
    installationToken: str
    caraerApiBase: str


InstallationState = dict[str, Any]
InstallationSecrets = dict[str, str]


class EnqueueJobRequest(TypedDict):
    functionName: str
    payload: NotRequired[dict[str, Any]]
    delaySeconds: NotRequired[float]


class InstallationJob(TypedDict, total=False):
    jobId: str
    status: str
    functionName: str
    payload: dict[str, Any]
    result: Any
    error: str
    createdAt: str | int | float
    updatedAt: str | int | float


class ApiSuccess(TypedDict, total=False):
    message: str
    data: Any
