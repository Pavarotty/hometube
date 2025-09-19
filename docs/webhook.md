# Webhook API (Same Port)

HomeTube exposes an HTTP POST endpoint on the same port as the Streamlit server to receive external data and automatically populate UI fields (e.g. the video URL).

- Endpoint: `POST /webhook`
- Port: the same as the UI (no additional port)
- Enable: `ENABLE_WEBHOOK=1` (default)

## Payload

Accepts JSON (recommended) or form-url-encoded. Recognized fields:
- `url` (or `URL`): video link to populate the UI URL field
- `filename` (or `name`): proposed file name for the "Video name" field

Example JSON:
```json
{
    "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "filename": "My Video"
}
```

## Examples

```bash
curl -sS -X POST http://localhost:8501/webhook \
    -H "Content-Type: application/json" \
    -d '{"url":"https://youtu.be/dQw4w9WgXcQ","filename":"My Video"}'
```

With form-url-encoded:
```bash
curl -sS -X POST http://localhost:8501/webhook \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "url=https://youtu.be/dQw4w9WgXcQ&filename=My+Video"
```

Response:
```json
{"ok": true, "received": {"url": "...", "filename": "..."}}
```

## Security

- The endpoint is left open locally for simplicity. If exposed to the network, protect it with a reverse proxy, trusted network, or custom token.
- To disable completely: `ENABLE_WEBHOOK=0`.

## Notes

- The UI applies webhook data on the next rerun (Streamlit reruns frequently). After the POST, the URL field will be filled automatically.
- In Docker, the endpoint is accessible on the same mapped port (e.g. `http://localhost:8501/webhook`).
