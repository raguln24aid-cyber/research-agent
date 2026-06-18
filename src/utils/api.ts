import axios from 'axios';

const API_BASE = import.meta.env.VITE_API_BASE_URL ?? '';

console.log('[API] VITE_API_BASE_URL =', API_BASE);

// DEBUG: this file is part of an unused / duplicate axios client in this repo.
// Keeping logs for now, but it should not be used by the deployed frontend (frontend uses frontend/src/services/api.js). 


const api = axios.create({
	baseURL: API_BASE || undefined,
});

// Request interceptor: attach token, log URL/headers/token, prevent /api/auth/me if no token
api.interceptors.request.use((config: any) => {
	const token = localStorage.getItem('token') ?? sessionStorage.getItem('token') ?? null;
	console.log('[API] token from storage =', token);

	// compute and log full request URL
	const requestPath = config.url ?? '';
	const base = API_BASE?.replace(/\/$/, '') ?? '';
	const pathPrefixed = requestPath.startsWith('/') ? requestPath : `/${requestPath}`;
	const fullUrl = base ? `${base}${pathPrefixed}` : requestPath;
	console.log('[API] Full request URL =', fullUrl);

	console.log('[API] Request headers before =', config.headers);

	// If token exists, attach Authorization header
	if (token) {
		config.headers = config.headers || {};
		(config.headers as Record<string, string>)['Authorization'] = `Bearer ${token}`;
		console.log('[API] Authorization header set:', `Bearer ${token}`);
	} else {
		// Prevent call to /api/auth/me if no token and redirect to login
		if (fullUrl.includes('/api/auth/me')) {
			console.warn('[API] No token found; cancelling /api/auth/me request and redirecting to /login');
			// client-side redirect
			try {
				window.location.href = '/login';
			} catch (e) {
				/* ignore */
			}
			// Cancel request
			return Promise.reject(new axios.Cancel('No token; cancelled /api/auth/me'));
		}
	}

	return config;
}, (error) => {
	return Promise.reject(error);
});

// Response interceptor: log responses and handle unauthorized/forbidden/not found
api.interceptors.response.use((response) => {
	console.log('[API] Response', response.status, response.config?.url);
	return response;
}, (error) => {
	if (axios.isCancel(error)) {
		console.warn('[API] Request cancelled:', error.message);
		return Promise.reject(error);
	}
	const resp = error?.response;
	if (resp) {
		console.warn('[API] Response error', resp.status, resp.config?.url);
		if (resp.status === 401) {
			// Optionally redirect to login on 401
			try { window.location.href = '/login'; } catch (e) { /* ignore */ }
		} else if (resp.status === 403) {
			// forbidden handling
		} else if (resp.status === 404) {
			// not found handling
		}
	}
	return Promise.reject(error);
});

export default api;