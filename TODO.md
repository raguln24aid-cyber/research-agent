- [x] Scan full workspace for hardcoded API URLs and localhost/127.0.0.1
- [x] Fix frontend API base URL usage to rely on import.meta.env.VITE_API_BASE_URL
- [x] Ensure auth.me requests use correct base URL (/api/auth/me)
- [x] Remove/replace duplicate api clients (frontend/src/services/api.js vs src/utils/api.ts)

- [x] Add temporary debugging logs for request/response + token loading + base URL resolution
- [x] Verify JWT Authorization header is attached on every protected request
- [x] Ensure FastAPI router prefixes match frontend paths
- [ ] Re-run scan to confirm no remaining bad occurrences


