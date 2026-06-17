import { cn } from "@/lib/utils";

export function Spinner({ className }) {
  return (
    <div
      className={cn(
        "h-5 w-5 animate-spin rounded-full border-2 border-primary border-t-transparent",
        className
      )}
    />
  );
}

export function LoadingScreen({ message = "Loading..." }) {
  return (
    <div className="flex min-h-[200px] flex-col items-center justify-center gap-3">
      <Spinner className="h-8 w-8" />
      <p className="text-sm text-muted-foreground">{message}</p>
    </div>
  );
}
