import ReactMarkdown from "react-markdown";
import { Download } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

const statusVariant = {
  PENDING: "warning",
  RUNNING: "running",
  COMPLETED: "success",
  FAILED: "destructive",
};

export function ReportViewer({ session, report }) {
  const handleDownload = () => {
    if (!report) return;
    const blob = new Blob([report.report], { type: "text/markdown" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `${report.title.replace(/[^a-z0-9]/gi, "_")}.md`;
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="space-y-6">
      <div className="flex items-start justify-between gap-4">
        <div>
          <h2 className="text-2xl font-bold">{report?.title || "Research in Progress"}</h2>
          <p className="mt-1 text-muted-foreground">{session.query}</p>
        </div>
        <div className="flex items-center gap-2">
          <Badge variant={statusVariant[session.status] || "secondary"}>
            {session.status}
          </Badge>
          {report && (
            <Button variant="outline" size="sm" onClick={handleDownload}>
              <Download className="mr-2 h-4 w-4" />
              Download Markdown
            </Button>
          )}
        </div>
      </div>

      {session.status === "RUNNING" || session.status === "PENDING" ? (
        <Card>
          <CardContent className="py-12 text-center">
            <p className="text-muted-foreground">
              Research agents are working on your query. This may take a minute...
            </p>
            <p className="mt-2 text-sm text-muted-foreground">
              Planner → Research → Review → Report
            </p>
          </CardContent>
        </Card>
      ) : session.status === "FAILED" ? (
        <Card>
          <CardContent className="py-12 text-center text-destructive">
            Research failed. Please try again with a different query.
          </CardContent>
        </Card>
      ) : report ? (
        <>
          <Card>
            <CardHeader>
              <CardTitle>Generated Report</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="markdown-body prose max-w-none">
                <ReactMarkdown>{report.report}</ReactMarkdown>
              </div>
            </CardContent>
          </Card>

          {report.sources?.length > 0 && (
            <Card>
              <CardHeader>
                <CardTitle>Sources</CardTitle>
              </CardHeader>
              <CardContent>
                <ul className="space-y-3">
                  {report.sources.map((source, i) => (
                    <li key={i} className="text-sm">
                      <a
                        href={source.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="font-medium text-primary hover:underline"
                      >
                        {source.title || source.url}
                      </a>
                      {source.snippet && (
                        <p className="mt-1 text-muted-foreground">{source.snippet}</p>
                      )}
                    </li>
                  ))}
                </ul>
              </CardContent>
            </Card>
          )}
        </>
      ) : null}
    </div>
  );
}
