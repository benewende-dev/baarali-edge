# Demo — the USSD channel

The laptop model serves the office. **USSD** serves everyone else: the delivery driver, the
warehouse keeper, the field agent — on any handset, with no app and no data plan. The reasoning
is in [`../USE_CASE.md`](../USE_CASE.md); this directory is the working code.

```bash
.venv/bin/python demo/ussd.py --telephone    # handset simulator, offline
.venv/bin/python demo/ussd.py --serveur      # HTTP callback, aggregator-compatible
```

Turn the Wi-Fi off before running either. That is the point.

## What is real here, and what is not

**Real — the wire contract.** `repondre()` implements the callback that West African USSD
aggregators publish: four inbound fields (`sessionId`, `serviceCode`, `phoneNumber`, `text`, where
`text` is the whole session history joined by `*`), and a plain-text reply prefixed `CON ` (session
continues) or `END ` (session ends). The same function answers a real aggregator unmodified.

**Real — the screen constraint.** A USSD message is capped at **182 characters**, prefix included.
This is not styling; it dictates the system instruction given to the model and its token budget.
The server *refuses* to emit an over-long screen rather than let the operator truncate it at an
arbitrary byte.

**Real — the data locality.** `commandes.json` is the company's order book, read from the same
disk the model runs on. Nothing leaves the machine, which is the entire argument.

**Not real — the short code.** A live `*123#` requires an agreement with an Ivorian mobile
operator: weeks of paperwork and a commercial contract. **We claim no short code in service.**
`--telephone` replays a session locally so that what we demonstrate is exactly what we can prove.

## Sampling settings, and why

The handler generates with `repeat_penalty = 1.10`, the value chosen in
[`../bench/copies/penalite-repetition.md`](../bench/copies/penalite-repetition.md). It matters
more on this channel than anywhere else: offline, on a handset, with no second opinion available
and airtime being spent, a degenerate loop is not an ugly answer — it is a lost session.
