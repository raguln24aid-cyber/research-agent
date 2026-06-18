import api from '../utils/api';

export async function getMe() {
	console.log('[authService] calling GET /api/auth/me');
	return api.get('/api/auth/me');
}