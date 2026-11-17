# Feature tour

[← Showcase home](../README.md)

SkyCommand brings workflow definition, execution, and inspection into a common interface. This tour introduces the platform's core capabilities; the walkthrough connects them into a demonstration sequence.

## 1. Compose repeatable work

Registered tools are reusable building blocks. Workflows combine those tools with execution steps such as approvals and retries, while scheduling supports recurring operation. The objective is to stop treating every repeatable procedure as a fresh manual exercise.

## 2. Execute durable workflows

Temporal provides the durable execution layer. The operator interface and backend bring that execution into SkyCommand's workflow and run views. Retry and recovery controls belong to that execution model rather than being hidden in one-off scripts.

## 3. Inspect runs and results

Run history, node outcomes, structured outputs, and diagnostics make the execution path visible. A useful demonstration should show both an overall outcome and the individual steps that produced it.

## 4. Use embedded agents selectively

AI agents are optional workflow nodes. They contribute reasoning where useful without replacing deterministic execution. An embedded Agent Run can use its run-bound MCP connection to invoke configured capabilities and return attributable results to the surrounding workflow.

## 5. Let coding agents use SkyCommand through MCP

Configured external coding assistants can invoke SkyCommand's exposed registered operations and published workflows through MCP, then inspect returned results. This makes SkyCommand an operational tool for a coding agent, not only a host that can launch one.

The external assistant and embedded agent use separate MCP connections over shared registrations. Their identities and permissions remain distinct.

## 6. Configure embedded-agent capabilities

Select capabilities for a Project and exact Agent definition version: assigned Tools, assigned published Workflows, and supported direct operations on registered targets. Direct-operation domains include Git, Docker, named SkyCommand Controls and PostgreSQL where the corresponding adapters are available.

Enabled Tools and Workflows retain their normal complete contracts. Direct-access switches govern direct calls; they do not silently restrict operations inside an already enabled Tool or Workflow. Permitted requests execute under standing configuration, while normal executor permissions and explicitly selected approval steps still apply.

Agent integration remains active engineering work. A configured or listed capability is not proof that every operation in that domain has been exercised.

## 7. Support developer operations

Git workflows, scoped delivery, Docker operations, and database-backed services connect the orchestration platform to day-to-day development work. This public tour describes the functions without exposing repository contents, local machine configuration, or account sessions.

## 8. Keep human decisions where intended

Approvals and operator review are available where the owner explicitly configures a decision. Routine enabled Agent-to-Tool and Agent-to-Workflow calls do not require a fresh human approval for every invocation. AI-assisted implementation is paired with testing, validation, and human judgment rather than treated as self-verifying output.

## 9. Coordinate development through work orders

The current development method uses structured instructions and work-order families to coordinate multiple scoped work streams. Manifests define scope and assignments; execution state records attempts and results; family state tracks related orders and progress. Dependencies, focused verification and one accountable writer per shared checkout help preserve unrelated work.

This is an existing development practice. **Native work-order coordination inside SkyCommand is planned for Phase 20**, not advertised as an already delivered screen or automatic agent-to-agent delegation feature.

## Where to go next

[Architecture](./architecture.md) · [Walkthrough](./walkthrough.md) · [Screenshot gallery](./gallery.md)
