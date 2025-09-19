# Webhook API (Same Port)

HomeTube espone un endpoint HTTP POST sulla stessa porta del server Streamlit per ricevere dati esterni e popolare automaticamente i campi della UI (es. l'URL del video).

- Endpoint: `POST /webhook`
- Porta: la stessa della UI (nessuna porta aggiuntiva)
- Abilitazione: `ENABLE_WEBHOOK=1` (default)

## Payload

Accetta JSON (consigliato) o form-url-encoded. Campi riconosciuti:
- `url` (o `URL`): link del video da inserire nel campo URL della UI
- `filename` (o `name`): nome file proposto nel campo "Video name"

Esempio JSON:
```json
{
  "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  "filename": "My Video"
}
```

## Esempi

```bash
curl -sS -X POST http://localhost:8501/webhook \
  -H "Content-Type: application/json" \
  -d '{"url":"https://youtu.be/dQw4w9WgXcQ","filename":"My Video"}'
```

Con form-url-encoded:
```bash
curl -sS -X POST http://localhost:8501/webhook \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "url=https://youtu.be/dQw4w9WgXcQ&filename=My+Video"
```

Risposta:
```json
{"ok": true, "received": {"url": "...", "filename": "..."}}
```

## Sicurezza

- L'endpoint è aperto in locale per semplicità. Se esposto in rete, proteggilo con un reverse proxy, rete fidata o token custom.
- Per disabilitare completamente: `ENABLE_WEBHOOK=0`.

## Note

- L'UI applica i dati del webhook al prossimo rerun (Streamlit ricalcola spesso). Dopo la POST, la barra URL si riempirà automaticamente.
- In Docker, l'endpoint è accessibile sulla stessa porta mappata (es. `http://localhost:8501/webhook`).
