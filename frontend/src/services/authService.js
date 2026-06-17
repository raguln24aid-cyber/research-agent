import { request } from "./api";

export const authService = {
  signup: (data) =>
    request("/auth/signup", { method: "POST", body: JSON.stringify(data) }),

  login: (data) =>
    request("/auth/login", { method: "POST", body: JSON.stringify(data) }),

  me: () => request("/auth/me"),
};
