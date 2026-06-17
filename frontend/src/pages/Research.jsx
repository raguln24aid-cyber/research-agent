import { useCallback, useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { ReportViewer } from "@/components/research/ReportViewer";
import { LoadingScreen } from "@/components/ui/spinner";
import { researchService } from "@/services/researchService";

export default function Research() {
  const { id } = useParams();
  const [data, setData] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  const loadResearch = useCallback(async () => {
    try {
      const result = await researchService.getById(id);
      setData(result);
      setError("");
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, [id]);

  useEffect(() => {
    loadResearch();
  }, [loadResearch]);

  useEffect(() => {
    if (!data || data.session.status === "COMPLETED" || data.session.status === "FAILED") {
      return;
    }

    const interval = setInterval(loadResearch, 5000);
    return () => clearInterval(interval);
  }, [data, loadResearch]);

  if (loading) {
    return <LoadingScreen message="Loading research..." />;
  }

  if (error) {
    return <p className="text-destructive">{error}</p>;
  }

  return <ReportViewer session={data.session} report={data.report} />;
}
