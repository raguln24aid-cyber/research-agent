import { createContext, useContext, useEffect, useState } from "react";
import { authService } from "@/services/authService";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem("token") ?? sessionStorage.getItem("token");
    console.log('[Auth Hook] token loaded from storage =', token);

    if (!token) {
      console.log('[Auth Hook] No token found; user is unauthenticated');
      setLoading(false);
      return;
    }

    console.log('[Auth Hook] token found; calling authService.me()');

    authService
      .me()
      .then((userData) => {
        console.log('[Auth Hook] me() response user data =', userData);
        setUser(userData);
      })
      .catch((error) => {
        console.error('[Auth Hook] me() call failed; clearing token from storage. Error:', error);
        localStorage.removeItem("token");
        setUser(null);
      })
      .finally(() => {
        console.log('[Auth Hook] me() request completed; setting loading to false');
        setLoading(false);
      });
  }, []);

  const login = async (credentials) => {
    const data = await authService.login(credentials);
    localStorage.setItem("token", data.access_token);
    setUser(data.user);
    return data;
  };

  const signup = async (data) => {
    const result = await authService.signup(data);
    localStorage.setItem("token", result.access_token);
    setUser(result.user);
    return result;
  };

  const logout = () => {
    localStorage.removeItem("token");
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, loading, login, signup, logout, isAuthenticated: !!user }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within AuthProvider");
  }
  return context;
}
