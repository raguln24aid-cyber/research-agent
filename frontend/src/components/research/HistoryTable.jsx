import { Badge } from "@/components/ui/badge";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { useNavigate } from "react-router-dom";

const statusVariant = {
  PENDING: "warning",
  RUNNING: "running",
  COMPLETED: "success",
  FAILED: "destructive",
};

export function HistoryTable({ items, onDelete }) {
  const navigate = useNavigate();

  if (!items.length) {
    return (
      <p className="py-8 text-center text-sm text-muted-foreground">
        No research history yet. Start your first research task!
      </p>
    );
  }

  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>Query</TableHead>
          <TableHead>Title</TableHead>
          <TableHead>Status</TableHead>
          <TableHead>Created</TableHead>
          <TableHead className="text-right">Actions</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {items.map((item) => (
          <TableRow key={item.id}>
            <TableCell className="max-w-[200px] truncate">{item.query}</TableCell>
            <TableCell className="max-w-[200px] truncate">
              {item.title || "—"}
            </TableCell>
            <TableCell>
              <Badge variant={statusVariant[item.status] || "secondary"}>
                {item.status}
              </Badge>
            </TableCell>
            <TableCell>{new Date(item.created_at).toLocaleDateString()}</TableCell>
            <TableCell className="text-right space-x-2">
              <button
                className="text-sm text-primary hover:underline"
                onClick={() => navigate(`/research/${item.id}`)}
              >
                View
              </button>
              <button
                className="text-sm text-destructive hover:underline"
                onClick={() => onDelete(item.id)}
              >
                Delete
              </button>
            </TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}
