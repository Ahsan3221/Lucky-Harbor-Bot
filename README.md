# Lucky Harbor — Telegram Customer CRM

Updated to Ace Arcade-style CRM while preserving this bot's original **PostgreSQL tables `users`, `topics`, `staff`**, its token/environment variable names, customer IDs, and customer-topic mappings. New CRM tables are namespaced `lucky_harbor_*` to avoid cross-bot collisions.

**Features:** case-insensitive custom labels and game names, saved usernames and plaintext passwords, automatically capture staff account templates, CashMaster selection, pinned customer profiles, account lookup, notes, assignment, audit log, durable queue, privacy/deletion commands, owner-only staff control, opt-in broadcasts.

**Auto account template (staff sends inside customer's forum topic):**
```text
👤 Username: Mike333fk
🔑 Password: 009988
Log in and let me know if you need help ❤️✨
```
Saves Firekirin username/password and forwards original message. Ending with repeated 3 digits plus suffix maps: s=Orionstars, fk=Firekirin, v=Vblink, u=Ultrapanda, r=Riversweeps, j=Juwa, gv=GameVault, mw=Milkyway, cm=CashMaster. Explicit `Game: Custom Game` overrides inference.

**Staff commands:** `/profile`, `/accounts`, `/label My Custom Label`, `/unlabel VIP`, `/setaccount Game Username`, `/findaccount Username`, `/note Text`, `/assign ID`, `/status pending`, `/history`, `/close`.

**Railway:** Keep BOT_TOKEN, SUPPORT_GROUP_ID, DATABASE_URL and AUTHORIZED_STAFF_IDS. Add OWNER_IDS=your numeric Telegram ID to use owner-only actions. Confirm bot has topic-management/pin permissions. No encryption key. Back up PostgreSQL before deployment. Previous source: backup/pre-crm-unification-20261011. Tests are offline; Railway and Telegram integration not verified.
