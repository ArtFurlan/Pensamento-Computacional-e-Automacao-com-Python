from pathlib import Path
import json, csv

class LeadRepository:
    def __init__(self):
        self.data_dir = Path(__file__).resolve().parent / "data"
        self.data_dir.mkdir(exist_ok=True)
        self.db_path = self.data_dir / "leads.json"

    def _load(self):
        if not self.db_path.exists():
            return []
        try:
            return json.loads(self.db_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []

    def _save(self, leads):
        self.db_path.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

    def read_leads(self):
        return self._load()

    def create_lead(self, lead):
        leads = self._load()
        leads.append(lead.to_dict())
        self._save(leads)

    def export_csv(self, path=None):
        path = Path(path) if path else (self.data_dir / "leads.csv")
        leads = self._load()
        try:
            with path.open("w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=["name", "company", "email", "stage", "created"])
                w.writeheader()
                for row in leads:
                    w.writerow(row)
            return path
        except PermissionError:
            return None
