# SkyCommand Visual Walkthrough

[← Showcase Home](../README.md) · [Screenshot Gallery](./gallery.md)

This is a **guided reading of real UI captures**, not a transcript of a single continuous execution. Images are from a development environment on November 17, 2026; account information and internal paths were redacted.

## 1. Enter the operator interface

[View the Login Screen](../assets/screenshots/01-login.jpg). SkyCommand uses a branded sign-in screen with a star-field background. Entered account fields are hidden in the public copy.

## 2. Inspect the Command Center

[View Command Center](../assets/screenshots/02-command-center.jpg). The overview presents tool and workflow activity, scheduled execution, utilization and workflow duration across the displayed period.

[View SkyCommand Controls](../assets/screenshots/03-skycommand-controls.jpg). The controls popover provides operational entry points and point-in-time runtime status. The screenshot does not imply that every displayed service is healthy or currently running.

## 3. Examine the infrastructure

[View Infrastructure](../assets/screenshots/04-infrastructure.jpg). Resource trends, containers and lifecycle events connect the automation interface to underlying operational services.

## 4. Configure a workflow

[View Start Workflow](../assets/screenshots/05-start-workflow.jpg). The Repo Files Generator interface shows selected inputs and a read-only runtime map. It is captured **before execution**; the screenshot itself is not proof that the displayed launch was performed.

## 5. Follow execution in progress

[View the Running Workflow](../assets/screenshots/06-workflow-running.jpg). The Workflow Operations overlay shows earlier nodes completed while the Generate Repository Map node is **RUNNING**, with later nodes not yet run. This is an actual point-in-time in-progress graph, **not** a completed workflow.

## 6. Inspect structured evidence

[View a Structured Tool Result](../assets/screenshots/07-tool-structured-result.jpg). A separate tool execution exposes a versioned ToolResult with an artifact summary, performance telemetry and packaging policy. Its internal archive path has been redacted. **Do not interpret this as the final result of the workflow in step 5.**

## 7. Explore AI agents

[View Run Agents](../assets/screenshots/08-run-agents.jpg). This is the conversation/workspace surface; its pictured state is idle. The real session history was hidden from the public version.

[View Agent Capabilities](../assets/screenshots/09-agent-capabilities.jpg). The example shows capability discovery, assignments and an inspector. Its selected historical test item is marked **NOT_VERIFIED_AT_DISPATCH**; an assigned checkbox does not prove a callable operation has been authorized or executed.

## 8. Understand MCP and the development process

Configured external coding assistants can access SkyCommand's published tools and workflows through MCP, while embedded agents use a separate run-bound capability path. Read the [architecture and capability overview](./architecture.md) for the model. **No external MCP invocation screenshot was supplied in this set**, so this page does not claim to demonstrate one visually.

Work-order families and the Cloud Agent / Operator / Local Agent relay are an established development method. Native work-order integration in SkyCommand is **planned for Phase 20**, not shown as a shipped UI feature.

## 9. Inspect browser-test configuration

[View Playwright Tests](../assets/screenshots/10-playwright-tests.jpg). The supplied capture shows the Playwright Tests → Run Tests page and a configured Workflow Initialization E2E test. Its Chromium execution profile, inputs and launch control are visible. It is not a test-results capture and does not demonstrate a completed test.

## What future captures could add

A completed workflow run with its own structured node results; a demonstrated agent result; and a verified external MCP invocation matched to SkyCommand's execution history.

[Back to Gallery](./gallery.md) · [Request a Walkthrough](mailto:paulsattaur@hotmail.com?subject=SkyCommand%20walkthrough)
