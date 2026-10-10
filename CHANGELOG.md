# Lucky Harbor CRM upgrade — 2026-10-11
- Preserved generic PostgreSQL users/topics/staff and existing topic IDs.
- Added namespaced `lucky_harbor_*` CRM tables, case-insensitive labels, saved accounts/passwords, and staff account-template auto-capture.
- Added CashMaster to game keyboard; hardened delivery reliability using database outbox and retry handling.
- Owner/admin permissions, opt-in broadcast, privacy/deletion, notes and audit.
- Original SHA 79d9105503e9505ade24890475bad76f4061afd0. Offline tests pass locally for equivalent transformed code; live environment not yet verified.
