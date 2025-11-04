from stages import Lead
from repo import LeadRepository

class MiniCRMApp:
    def __init__(self):
        self.repo = LeadRepository()

    def add_leads(self):
        name = input("Nome: ")
        company = input("Empresa: ")
        email = input("E-mail: ")
        if not name or not email or "@" not in email:
            print("Nome e e-mail válido são obrigatórios.")
            return
        lead = Lead(name, company, email)
        self.repo.create_lead(lead)
        print("✔ Lead adicionado!")

    def list_leads(self):
        leads = self.repo.read_leads()
        if not leads:
            print("Nenhum lead ainda.")
            return
        print("\n# | Nome                 | Empresa            | E-mail")
        print("--+----------------------+-------------------+-----------------------")
        for i, l in enumerate(leads):
            print(f"{i:02d}| {l['name']:<20} | {l['company']:<17} | {l['email']:<21}")

    def search_flow(self):
        q = input("Buscar por: ").lower()
        if not q:
            print("Consulta vazia.")
            return
        leads = self.repo.read_leads()
        results = []
        for i, l in enumerate(leads):
            blob = f"{l['name']} {l['company']} {l['email']}".lower()
            if q in blob:
                results.append((i, l))
        if not results:
            print("Nada encontrado.")
            return
        print("\n# | Nome                 | Empresa            | E-mail")
        print("--+----------------------+-------------------+-----------------------")
        for i, l in results:
            print(f"{i:02d}| {l['name']:<20} | {l['company']:<17} | {l['email']:<21}")

    def export_leads(self):
        path = self.repo.export_csv()
        if path is None:
            print("Não consegui escrever o CSV. Feche o arquivo se estiver aberto e tente novamente.")
        else:
            print(f"✔ Exportado para: {path}")

    def print_menu(self):
        print("\nMini CRM de Leads — Aula 2 (Adicionar/Listar/Buscar/CSV)")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Buscar (nome/empresa/e-mail)")
        print("[4] Exportar CSV")
        print("[0] Sair")

    def main(self):
        while True:
            self.print_menu()
            op = input("Escolha: ")
            if op == "1":
                self.add_leads()
            elif op == "2":
                self.list_leads()
            elif op == "3":
                self.search_flow()
            elif op == "4":
                self.export_leads()
            elif op == "0":
                print("Até mais!")
                break
            else:
                print("Opção inválida.")


if __name__ == "__main__":
    app = MiniCRMApp()
    app.main()
