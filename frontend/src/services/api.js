let rawBase = import.meta.env.VITE_API_BASE_URL;
console.log('[API Base Resolution] raw VITE_API_BASE_URL =', rawBase);

if (rawBase) {
  rawBase = rawBase.trim().replace(/\/$/, "");
  if (!rawBase.endsWith("/api")) {
    rawBase = `${rawBase}/api`;
  }
} else {
  rawBase = "/api";
}
const API_BASE = rawBase;
console.log('[API Base Resolution] resolved API_BASE =', API_BASE);

class ApiError extends Error {
  constructor(message, status) {
    super(message);
    this.status = status;
  }
}

async function request(path, options = {}) {
  let token = localStorage.getItem("token");
  if (token === "undefined" || token === "null" || !token || token.trim() === "") {
    token = null;
  }
  console.log('[API Token Loading] path =', path, 'token found =', token ? `Bearer ${token.substring(0, 10)}...` : 'None');

  const headers = {
    "Content-Type": "application/json",
    ...options.headers,
  };

  if (token) {
    headers.Authorization = `Bearer ${token}`;
  }

  const url = `${API_BASE}${path}`;
  console.log('[API Request] Sending request to:', url, 'Method:', options.method ?? 'GET', 'Headers:', headers, 'Body:', options.body);

  try {
    const response = await fetch(url, {
      ...options,
      headers,
    });

    console.log('[API Response Status] URL:', url, 'Status:', response.status, response.statusText);

    const data = await response.json().catch(() => ({}));
    console.log('[API Response Data] URL:', url, 'Data:', data);

    if (!response.ok) {
      console.warn('[API Response Error] URL:', url, 'Status:', response.status, 'Data:', data);
      const detail = data.detail;
      const message = Array.isArray(detail)
        ? detail.map((d) => d.msg).join(", ")
        : detail || "Request failed";
      throw new ApiError(message, response.status);
    }

    return data;
  } catch (error) {
    console.error('[API Network/Request Error] URL:', url, 'Error:', error);
    throw error;
  }
}

export { request, ApiError };
