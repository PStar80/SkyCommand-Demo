# Feature tour

[← Showcase home](../README.md)

SkyCommand brings workflow definition, execution, and inspection into a common interface. This tour introduces the platform's core capabilities; the walkthrough connects them into a demonstration sequence.

## 1. Compose repeatable work

Registered tools are reusable building blocks. Workflows combine those tools with execution steps such as approvals and retries, while scheduling supports recurring operation. The objective is to stop treating every repeatable procedure as a fresh manual exercise.

## 2. Execute durable workflows

Temporal provides the durable execution layer. The operator interface and backend bring that execution into SkyCommand's workflow and run views. Retry and recovery controls belong to that execution model rather than being hidden in one-off scripts.

## 3. Inspect runs and results

Run history, node outcomes, structured outputs, and diagnostics make the execution path visible. A useful demonstration should show both an overall outcome and the individual steps that produced it.

## 4. Use agents selectively

AI agents are optional workflow nodes. They are used for work that benefits from adaptive reasoning; they do not replace the deterministic workflow path. The surrounding workflow retains the context for execution, review, and results.

Agent integration remains active engineering work. Testing, validation, and human review remain part of the development approach.

## 5. Support developer operations

Git workflows, scoped delivery, Docker operations, and database-backed services connect the orchestration platform to day-to-day development work. This public tour describes the functions without exposing repository contents, local machine configuration, or account sessions.

## 6. Keep a human in the loop

Approvals and operator review are available where the workflow requires a decision. AI-assisted implementation is paired with testing, validation, and human judgment rather than treated as self-verifying output.

## Where to go next

[Architecture](./architecture.md) · [Walkthrough](./walkthrough.md) · [Screenshot gallery](./gallery.md)
