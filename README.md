<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 650px)" srcset="./assets/brand/hero-mobile-static.svg" />
  <source media="(prefers-reduced-motion: reduce)" srcset="./assets/brand/hero-static.svg" />
  <source media="(max-width: 650px)" srcset="./assets/brand/hero-mobile.svg" />
  <img src="./assets/brand/hero.svg" width="100%" alt="SkyCommand — workflow automation and orchestration. Deterministic by default, with reusable tools, optional AI agents, and observable execution. An independent platform by Paul Sattaur." />
</picture>

<p align="center">
  <a href="./docs/features.md">Feature tour</a> ·
  <a href="./docs/architecture.md">Architecture</a> ·
  <a href="./docs/walkthrough.md">Walkthrough</a> ·
  <a href="./docs/gallery.md">Screenshots</a> ·
  <a href="mailto:paulsattaur@hotmail.com?subject=SkyCommand%20walkthrough">Get in touch</a>
</p>

# SkyCommand

**Build workflows. See what ran. Understand what happened.**

SkyCommand is an independent workflow automation and orchestration platform built by **Paul Sattaur**. It brings reusable tools, durable workflows, optional AI agents, and operational visibility into one developer-focused interface.

The guiding principle is simple: **deterministic workflows by default; AI agents where adaptive reasoning is useful.**

> **Public showcase, private implementation.** This repository contains product documentation and presentation assets. It is not the application source, an installable distribution, or a hosted interactive demo.

## What it does

| Capability | What it brings to the workflow |
|---|---|
| **Durable orchestration** | Temporal-backed execution with retries, approvals, recovery controls, and scheduling. |
| **Reusable tools** | Tools composed into workflows rather than repeated as disconnected manual steps. |
| **Optional AI-agent nodes** | Adaptive work within the workflow when it is useful—not a requirement for every operation. |
| **Execution visibility** | Run history, node results, structured outputs, and operational diagnostics. |
| **Developer workflows** | Git and Docker operations alongside database-backed services and operational tooling. |
| **Human control** | Review and approval steps where a workflow calls for an operator's decision. |

[Explore the feature tour →](./docs/features.md)

## How it fits together

```text
React operator interface
           │
           ▼
     Node.js Core API
           │
           ▼
 Temporal workflow execution
      ├── Registered tools
      └── Optional AI-agent nodes

PostgreSQL: workflow definitions, run metadata, and results
Docker: containerized development and service operations
```

This is a simplified conceptual view, not a deployment specification. [Read the architecture overview →](./docs/architecture.md)

**Core stack:** React · Node.js / TypeScript · PostgreSQL · Temporal · Docker · REST APIs

## See the platform

The [walkthrough](./docs/walkthrough.md) outlines a representative demonstration: choose a workflow, follow its execution, inspect the results, and explain recovery.

**UI screenshots have not been published in this initial documentation package.** The [gallery](./docs/gallery.md) will contain reviewed captures from the actual application. The header is decorative concept artwork—not an application screenshot.

## Engineering approach

- Keep repeatable execution deterministic; introduce agents deliberately.
- Make execution observable through run history and structured results.
- Design for retries, recovery, and operator review.
- Keep implementation, validation, and release decisions accountable to a human.

## Project scope

SkyCommand is an independently developed platform. This repository focuses on its design, capabilities, and operator experience. The application implementation and development environment remain private.

## About the builder

I'm **Paul Sattaur**, a software engineer based in the Greater Toronto Area. My work combines enterprise backend and database experience with hands-on workflow orchestration, full-stack development, and AI-assisted engineering.

[GitHub profile](https://github.com/PStar80) · [LinkedIn](https://www.linkedin.com/in/paulsattaur/) · [Request a walkthrough](mailto:paulsattaur@hotmail.com?subject=SkyCommand%20walkthrough)

**Build systems that explain themselves.**
