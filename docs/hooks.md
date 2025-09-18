# Download Hooks

HomeTube supports running custom commands when a download starts, completes successfully, or fails. Hooks are configured via environment variables in your `.env` file.

## Environment variables

- `ON_DOWNLOAD_START`: executed when a download begins
- `ON_DOWNLOAD_SUCCESS`: executed when the final file is ready in the destination folder
- `ON_DOWNLOAD_FAILURE`: executed for failures and cancellations

Each hook receives a context that can be interpolated in the command using placeholders like `{FILENAME}`. Quoted variants `*_Q` are also available and already include double-quotes.

Available placeholders:
- `{URL}`, `{FILENAME}`, `{DEST_DIR}`, `{TMP_DIR}`, `{OUTPUT_PATH}`, `{STATUS}`
- `{RUN_SEQ}`, `{TS}` (unix epoch), `{START_SEC}`, `{END_SEC}`
- Quoted variants: `{URL_Q}`, `{DEST_DIR_Q}`, `{OUTPUT_PATH_Q}`, ...

## Notes
- On Windows, hooks run via the system shell. If you want PowerShell syntax, prefix with `powershell -NoProfile -Command` or `-File`.
- Escape literal braces in JSON payloads by doubling them: `{{` and `}}`.
- Hooks have a 30s timeout; output is logged in the UI logs.

## Examples

### PowerShell examples (Windows)
```powershell
# .env
ON_DOWNLOAD_START=powershell -NoProfile -Command "Write-Host 'Start {URL} -> {DEST_DIR_Q}'"
ON_DOWNLOAD_SUCCESS=powershell -NoProfile -Command "Write-Host 'OK {OUTPUT_PATH_Q}'"
ON_DOWNLOAD_FAILURE=powershell -NoProfile -Command "Write-Host 'FAIL {URL} status={STATUS}'"
```

### Call a PowerShell script with parameters
```powershell
# .env
ON_DOWNLOAD_SUCCESS=powershell -NoProfile -File .\scripts\on_success.ps1 -Path {OUTPUT_PATH_Q} -Url {URL_Q}
```

### Send a JSON webhook
```powershell
# .env
ON_DOWNLOAD_SUCCESS=curl -X POST -H "Content-Type: application/json" -d "{{\"path\":\"{OUTPUT_PATH}\",\"url\":\"{URL}\",\"status\":\"{STATUS}\"}}" http://localhost:9000/webhook
```

## Troubleshooting
- If you don’t see hook output, check the Logs panel at the bottom of the UI
- Ensure paths containing spaces use the quoted placeholders, e.g., `{OUTPUT_PATH_Q}`
- Increase logging in your scripts to diagnose issues
