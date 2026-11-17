# Walkthrough guide

[← Showcase home](../README.md)

This is a proposed sequence for a live or recorded demonstration. It is **not a transcript of a captured run**, and it contains no invented timings, results, screenshots, or performance claims.

## 1. Orient the viewer

Introduce the workflow and the problem it addresses. Explain which work is deterministic and whether any part benefits from an optional agent. Use demonstration-safe names and inputs.

## 2. Inspect the workflow

Show the ordered steps, reusable tools, and any relevant approval or retry behaviour. Explain the expected outcome before starting execution.

## 3. Run and observe

Start the selected workflow and show progress through its steps. Keep the explanation centred on the operator's view rather than private infrastructure or account configuration.

## 4. Inspect the outcome

Open the run history and a representative node result. Explain the difference between the overall workflow status and the evidence recorded for each step.

## 5. Explain recovery

Where a suitable demonstration is available, show how the operator inspects a failure and uses the available recovery or retry control. Label any deliberately introduced failure as a test scenario. Do not imply that every action is safe to repeat without examining its effect.

## 6. Show an optional agent

When appropriate, first show the selected Project + Agent-version capability assignments, then demonstrate an agent task within the workflow and its structured result. Explain why that task benefits from reasoning, while routine operations stay deterministic.

Distinguish assigned Tools and Workflows from direct-operation controls. Do not present a disabled direct operation as proof that an enabled Tool cannot perform the same action within its normal contract.

## 7. Show external coding-agent access through MCP

Use an already configured coding assistant to request a suitable exposed SkyCommand operation, such as a read-only inspection or an approved demonstration workflow. Show the genuine returned result or Run ID and the corresponding platform history where available.

Explain that the external MCP connection is distinct from the embedded Agent Run's connection. Do not display credentials, private connection configuration or unrestricted local-access claims.

## 8. Explain the work-order development method

Describe how an outcome becomes a scoped work order, how related work streams carry dependencies and assigned roles, and how results and review evidence are handed back. Use a sanitized illustrative outline rather than publishing private work-order payloads.

Clearly label this as the **current development method**. Native work-order coordination inside SkyCommand is **planned for Phase 20**; do not present an illustration as a shipped product screen.

## 9. Close with the engineering choices

Summarize durable execution, reusable tools, visible results, and human review. Distinguish the capability shown from work still in progress.

## Demonstration status

No video, recording, or application screenshots are included in this first documentation package. Reviewed media will be linked from the [gallery](./gallery.md) once available.

[Request a walkthrough](mailto:paulsattaur@hotmail.com?subject=SkyCommand%20walkthrough)
