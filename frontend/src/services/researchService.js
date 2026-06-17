import { request } from "./api";

export const researchService = {
  start: (query) =>
    request("/research/start", {
      method: "POST",
      body: JSON.stringify({ query }),
    }),

  history: (search) => {
    const params = search ? `?search=${encodeURIComponent(search)}` : "";
    return request(`/research/history${params}`);
  },

  recent: () => request("/research/recent"),

  getById: (id) => request(`/research/${id}`),

  delete: (id) => request(`/research/${id}`, { method: "DELETE" }),
};
