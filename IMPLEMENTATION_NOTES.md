# Implementation notes
`bot.py` uses `crm.py`, `database.py`, `settings.py`. Database migration reuses old generic users/topics/staff schema. Aux tables begin with lucky_harbor_. Set OWNER_IDS for administration. All live deployments require PostgreSQL backup.
