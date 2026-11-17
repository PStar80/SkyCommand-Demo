# Architecture overview

[← Showcase home](../README.md)

This is a high-level explanation of SkyCommand's public architecture. It deliberately omits private deployment details, host addresses, credentials, internal file paths, and provider-account configuration.

## Main components

| Component | Responsibility |
|---|---|
| **React operator interface** | Present workflow operations, run history, structured results, and operational views. |
| **Node.js Core API** | Connect operator requests to workflow execution and database-backed platform services. |
| **Temporal** | Coordinate durable workflow execution, including the retry and recovery model. |
| **Registered tools** | Supply reusable operations that workflows can compose. |
| **Optional AI-agent nodes** | Handle bounded workflow tasks where adaptive reasoning is useful. |
| **PostgreSQL** | Store workflow definitions, execution metadata, and structured results. |
| **Docker** | Support containerized development and service operations. |

## Simplified execution path

```text
Operator
   │
   ▼
React interface → Node.js Core API → Temporal workflow
                                        ├── Tool execution
                                        ├── Optional AI-agent work
                                        └── Approval / recovery steps

Workflow and run metadata → PostgreSQL → operator-facing history and results
```

This diagram groups responsibilities for explanation. It is not a complete service topology, database schema, or indication of every internal dependency.

## Why deterministic-first?

Repeatable work benefits from an explicit execution path that can be inspected and recovered. SkyCommand keeps that path central. Agents complement it when a task benefits from reasoning or adaptation, rather than adding a model call to every routine operation.

## Visibility is part of the workflow

Execution should be understandable at both the run and node level. The platform's history, structured outputs, and diagnostics are intended to help the operator answer what ran, what happened, and which next action is appropriate.

## What this repository does not contain

It contains no runtime services, database dumps, executable application source, account connections, environment files, or private repository history. A demonstration can explain architecture without granting access to the underlying environment.

[Feature tour](./features.md) · [Walkthrough](./walkthrough.md)
