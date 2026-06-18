const API_BASE = import.meta.env.VITE_API_BASE_URL ?? "/api";



class ApiError extends Error {
  constructor(message, status) {
    super(message);
    this.status = status;
  }
}

async function request(path, options = {}) {
  const token = localStorage.getItem("token");
  const headers = {
    "Content-Type": "application/json",
    ...options.headers,
  };

  if (token) {
    headers.Authorization = `Bearer ${token}`;
  }

console.log('[frontend fetch] API_BASE=', API_BASE, 'path=', path);

  const response = await fetch(`${API_BASE}${path}`, {

    ...options,
    headers,
  });

  const data = await response.json().catch(() => ({}));

if (!response.ok) {
    console.warn('[frontend fetch] non-OK', response.status);

    const detail = data.detail;
    const message = Array.isArray(detail)
      ? detail.map((d) => d.msg).join(", ")
      : detail || "Request failed";
    throw new ApiError(message, response.status);
  }

  return data;
}

export { request, ApiError };
