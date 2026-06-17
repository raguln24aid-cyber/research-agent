import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Spinner } from "@/components/ui/spinner";

export function ResearchInput({ onSubmit, loading }) {
  const [query, setQuery] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (query.trim()) {
      onSubmit(query.trim());
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <Textarea
        placeholder="Enter your research topic or question..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        rows={4}
        disabled={loading}
      />
      <Button type="submit" disabled={loading || !query.trim()}>
        {loading ? (
          <>
            <Spinner className="mr-2" />
            Starting Research...
          </>
        ) : (
          "Start Research"
        )}
      </Button>
    </form>
  );
}
