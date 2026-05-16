# Business Email Cutover Checklist

Date: 2026-03-01

## Goal
Make `dan@perrysoftwarellc.com` the production contact inbox while keeping website lead intake fully operational.

## Current state
- Website contact form submits successfully to Formspree endpoint:
  - `https://formspree.io/f/xreadryd`
- Website contact email now displays:
  - `dan@perrysoftwarellc.com`
- Form includes anti-spam honeypot (`_gotcha`) and inline success/error messaging.

## Required user actions
1. Finish business inbox setup and verify mailbox access.
2. In Formspree, set notification destination to that business inbox.
3. Confirm Formspree confirmation email link from the new inbox.

## Post-cutover validation
1. Submit one test lead from website contact form.
2. Confirm Formspree returns success.
3. Confirm notification email arrives in business inbox.
4. Reply from business inbox and verify `reply-to` points to visitor email.

## Optional hardening
1. Add backup recipient (secondary operations inbox).
2. Enable spam filtering/rules in mailbox.
3. Add monthly test reminder to ensure lead capture remains functional.
