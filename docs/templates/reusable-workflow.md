# Reusable workflow template

Use after reviewed chapters support the pattern. Clearly distinguish a proposed
practice, a narrated practice, and a successfully demonstrated practice.

## Problem and applicability

Describe the recurring coordination problem, prerequisites, and situations
where the approach does not apply. Identify human decision owners.

## Evidence

Link reviewed chapters and intervals. Describe what was observed, what was only
reported, and what remains unverified. Do not generalize from a bot success
message into external operational reliability.

## Participants and handoffs

Describe human roles, bot roles, inputs, outputs, shared context, and approval
boundaries. Use stable instance IDs in examples, not names assumed globally unique.

## Procedure

Write a bounded sequence with explicit request, acknowledgement, delegation,
verification, and human escalation steps. Commands require real implementations;
example prompts must be labeled examples, not historical quotations.

## Failure modes and recovery

Record demonstrated failures and plausible risks separately. Include how to
recognize missing context, silent failure, incorrect assumptions, and conflicting
instructions. Specify stop conditions and who resolves them.

## Verification and portability

Define observable success criteria, evidence needed to claim completion, and
limitations when transferring the practice to another team or toolset.
