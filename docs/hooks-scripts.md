# Hook Scripts via Files

This guide shows how to run hook commands from scripts mounted into the container.

## 1) Mount a host directory as `/app/hooks`

`docker-compose.yml` defines a volume:

```
- ${HOOKS_DIR_DOCKER_HOST:-./hooks}:/app/hooks:ro
```

Set `HOOKS_DIR_DOCKER_HOST` in `.env` (default is `./hooks`). Files will be readable in the container.

## 2) Create scripts

Examples are provided in `hooks/`:
- `on_start.sh`
- `on_success.sh`
- `on_failure.sh`

Make sure they are Unix LF line endings and executable when running outside Docker; inside Docker they run with `sh`.

## 3) Configure hooks in `.env`

```
ON_DOWNLOAD_START=sh /app/hooks/on_start.sh "{URL}" "{FILENAME}" "{DEST_DIR}" "{TMP_DIR}" "{RUN_SEQ}"
ON_DOWNLOAD_SUCCESS=sh /app/hooks/on_success.sh "{OUTPUT_PATH}" "{URL}" "{FILENAME}" "{DEST_DIR}"
ON_DOWNLOAD_FAILURE=sh /app/hooks/on_failure.sh "{STATUS}" "{URL}" "{FILENAME}" "{DEST_DIR}"
```

## 4) Apply changes

Recreate the container to pick up `.env` changes and ensure the hooks directory is mounted:

```powershell
docker compose up -d --force-recreate
```

## 5) Verify

In the app logs you should see lines like:
- `⚙️ Hook start: sh /app/hooks/on_start.sh ...`
- `[hook:start:out] [HOOK] START ...`

You can also check the consolidated hook log:

```powershell
docker compose exec hometube sh -lc "tail -n +1 /data/tmp/hooks_test.log"
```
