"""Quick API smoke test for all endpoints."""
import json
import sys
import urllib.error
import urllib.request
from uuid import uuid4

BASE = "http://127.0.0.1:8000/api"
email = f"langgraph_test_{uuid4().hex[:8]}@example.com"
password = "testpass123"
token = None
session_id = None
passed = 0
failed = 0


def call(method, path, body=None, auth=False):
    url = f"{BASE}{path}"
    headers = {"Content-Type": "application/json"}
    if auth and token:
        headers["Authorization"] = f"Bearer {token}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body_text = e.read().decode()
        try:
            detail = json.loads(body_text)
        except json.JSONDecodeError:
            detail = body_text
        return e.code, detail


def check(name, ok, detail=""):
    global passed, failed
    if ok:
        passed += 1
        print(f"  PASS  {name}")
    else:
        failed += 1
        print(f"  FAIL  {name} -> {detail}")


print("\n=== API Smoke Tests ===\n")

status, data = call("GET", "/health")
check("GET /api/health", status == 200 and data.get("status") == "ok", data)

status, data = call("POST", "/auth/signup", {"name": "LangGraph Tester", "email": email, "password": password})
check("POST /api/auth/signup", status == 200 and "access_token" in data, data)
if status == 200:
    token = data["access_token"]

status, data = call("GET", "/auth/me", auth=True)
check("GET /api/auth/me", status == 200 and data.get("email") == email, data)

status, data = call("POST", "/auth/login", {"email": email, "password": password})
check("POST /api/auth/login", status == 200 and "access_token" in data, data)
if status == 200:
    token = data["access_token"]

status, data = call("POST", "/research/start", {"query": "Brief overview of LangGraph for AI agents"}, auth=True)
check("POST /api/research/start", status == 200 and data.get("session", {}).get("id"), data)
if status == 200:
    session_id = data["session"]["id"]

status, data = call("GET", "/research/history", auth=True)
check("GET /api/research/history", status == 200 and isinstance(data, list), data)

status, data = call("GET", "/research/recent", auth=True)
check("GET /api/research/recent", status == 200 and isinstance(data, list), data)

if session_id:
    status, data = call("GET", f"/research/{session_id}", auth=True)
    check(
        f"GET /api/research/{{id}}",
        status == 200 and data.get("session", {}).get("id") == session_id,
        data,
    )

print(f"\n=== Results: {passed} passed, {failed} failed ===\n")
sys.exit(0 if failed == 0 else 1)
