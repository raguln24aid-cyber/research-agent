import { useCallback, useEffect, useState } from "react";
import { useNavigate, useSearchParams } from "react-router-dom";
import { Search } from "lucide-react";
import { HistoryTable } from "@/components/research/HistoryTable";
import { ResearchInput } from "@/components/research/ResearchInput";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { LoadingScreen } from "@/components/ui/spinner";
import { researchService } from "@/services/researchService";

export default function Dashboard() {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const [history, setHistory] = useState([]);
  const [recent, setRecent] = useState([]);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);
  const [starting, setStarting] = useState(false);
  const [error, setError] = useState("");

  const showHistory = searchParams.get("tab") === "history";

  const loadData = useCallback(async (searchTerm = "") => {
    setLoading(true);
    try {
      const [historyData, recentData] = await Promise.all([
        researchService.history(searchTerm || undefined),
        researchService.recent(),
      ]);
      setHistory(historyData);
      setRecent(recentData);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    const timer = setTimeout(() => loadData(search), 300);
    return () => clearTimeout(timer);
  }, [search, loadData]);

  const handleStartResearch = async (query) => {
    setStarting(true);
    setError("");
    try {
      const result = await researchService.start(query);
      navigate(`/research/${result.session.id}`);
    } catch (err) {
      setError(err.message);
    } finally {
      setStarting(false);
    }
  };

  const handleDelete = async (id) => {
    if (!confirm("Delete this research session and report?")) return;
    try {
      await researchService.delete(id);
      loadData(search);
    } catch (err) {
      setError(err.message);
    }
  };

  if (loading && !history.length) {
    return <LoadingScreen message="Loading dashboard..." />;
  }

  return (
    <div className="mx-auto max-w-6xl space-y-6">
      <div>
        <h1 className="text-3xl font-bold">Dashboard</h1>
        <p className="text-muted-foreground">Start new research or browse your history</p>
      </div>

      {error && <p className="text-sm text-destructive">{error}</p>}

      {!showHistory && (
        <>
          <Card>
            <CardHeader>
              <CardTitle>New Research</CardTitle>
              <CardDescription>
                Enter a topic and our multi-agent system will research and generate a report
              </CardDescription>
            </CardHeader>
            <CardContent>
              <ResearchInput onSubmit={handleStartResearch} loading={starting} />
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Recent Reports</CardTitle>
            </CardHeader>
            <CardContent>
              {recent.length === 0 ? (
                <p className="text-sm text-muted-foreground">No reports yet.</p>
              ) : (
                <div className="grid gap-3 md:grid-cols-2">
                  {recent.map((report) => (
                    <button
                      key={report.id}
                      onClick={() => navigate(`/research/${report.session_id}`)}
                      className="rounded-lg border p-4 text-left transition-colors hover:bg-muted/50"
                    >
                      <h3 className="font-medium truncate">{report.title}</h3>
                      <p className="mt-1 text-xs text-muted-foreground">
                        {new Date(report.created_at).toLocaleString()}
                      </p>
                    </button>
                  ))}
                </div>
              )}
            </CardContent>
          </Card>
        </>
      )}

      <Card>
        <CardHeader>
          <div className="flex items-center justify-between">
            <CardTitle>{showHistory ? "Research History" : "Recent History"}</CardTitle>
            <div className="relative w-64">
              <Search className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
              <Input
                placeholder="Search reports..."
                className="pl-9"
                value={search}
                onChange={(e) => setSearch(e.target.value)}
              />
            </div>
          </div>
        </CardHeader>
        <CardContent>
          <HistoryTable items={history} onDelete={handleDelete} />
        </CardContent>
      </Card>
    </div>
  );
}
