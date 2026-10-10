# Lucky Harbor Deployment
Backup main commit: 79d9105503e9505ade24890475bad76f4061afd0
GitHub backup branch: backup/pre-crm-unification-20261011.

Railway par existing DATABASE_URL/BOT_TOKEN/SUPPORT_GROUP_ID/AUTHORIZED_STAFF_IDS bilkul same rakho. `OWNER_IDS=YOUR_NUMERIC_TELEGRAM_ID` add karo. PostgreSQL snapshot lo.
Existing tables users/topics/staff reuse honge. Extra `lucky_harbor_*` tables additive migrations mein create honge.
GitHub main push se Railway auto deploy ho sakta hai, agar configured hai. Logs check, /start, customer message, staff reply, /profile, /label VIP, /accounts, /setaccount, automatic account detection aur CashMaster selection test karo.
Passwords plain text PostgreSQL mein honge, isliye DB access restrict karo.
Git rollback PostgreSQL data/schema rollback nahin karta; backup alag hai.
