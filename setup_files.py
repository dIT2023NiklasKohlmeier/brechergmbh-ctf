#!/usr/bin/env python3
"""
Setup-Skript für P3 - Directory Traversal Challenge
Erstellt Fake-Rechnungen und versteckte Secrets für das CTF
"""
import os
import random
from datetime import datetime, timedelta

def create_directories():
    """Erstellt die benötigten Verzeichnisse"""
    directories = [
        'static/invoices/2023',
        'static/invoices/2024',
        'secrets'
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✓ Verzeichnis erstellt: {directory}")

def generate_fake_invoices():
    """Generiert Fake-PDF-Rechnungen mit realistischem Dummy-Inhalt"""

    # Firmen für realistische Rechnungen
    companies = [
        "TechCorp Solutions GmbH",
        "Müller & Partner AG",
        "Digitale Welten Ltd.",
        "Schneider Maschinenbau",
        "Global Trade Systems",
        "Schmidt Consulting",
        "Weber Industries",
        "Fischer Electronics",
        "Meyer Logistics",
        "Becker Software"
    ]

    # Services für Rechnungen
    services = [
        "Softwarelizenz Enterprise Edition",
        "IT-Beratung und Support",
        "Hosting-Service Premium",
        "Wartungsvertrag Maschinen",
        "Cloud-Storage Professional",
        "Logistik-Dienstleistung",
        "Consulting-Paket Business",
        "Hardware-Lieferung Server",
        "Marketing-Kampagne Digital",
        "Security-Audit Premium"
    ]

    # Generiere Rechnungen für 2023 und 2024
    for year in [2023, 2024]:
        for i in range(1, 21):  # 20 Rechnungen pro Jahr
            invoice_number = f"RE-{year}-{i:03d}"
            filename = f"static/invoices/{year}/{invoice_number}.pdf"

            # Zufälliges Datum im Jahr
            start_date = datetime(year, 1, 1)
            end_date = datetime(year, 12, 31)
            days_between = (end_date - start_date).days
            random_date = start_date + timedelta(days=random.randint(0, days_between))

            # Zufällige Firma und Service
            company = random.choice(companies)
            service = random.choice(services)
            amount = random.randint(500, 50000)

            # Fake-PDF-Inhalt (als Text, sieht aus wie PDF-Struktur)
            content = f"""%PDF-1.4
1 0 obj
<<
/Type /Catalog
/Pages 2 0 R
>>
endobj

2 0 obj
<<
/Type /Pages
/Kids [3 0 R]
/Count 1
>>
endobj

3 0 obj
<<
/Type /Page
/Parent 2 0 R
/Contents 4 0 R
>>
endobj

4 0 obj
<<
/Length 500
>>
stream
========================================
    BRECHER LOGISTICS GMBH
    Rechnungsnummer: {invoice_number}
========================================

Datum: {random_date.strftime('%d.%m.%Y')}
Kunde: {company}

Position:
- {service}

Nettobetrag:     {amount:>10,.2f} EUR
MwSt. (19%):     {amount*0.19:>10,.2f} EUR
----------------------------------------
Gesamtbetrag:    {amount*1.19:>10,.2f} EUR

Zahlbar bis: {(random_date + timedelta(days=14)).strftime('%d.%m.%Y')}

Mit freundlichen Grüßen
Brecher Logistics GmbH
endstream
endobj

xref
0 5
trailer
<<
/Size 5
/Root 1 0 R
>>
startxref
{random.randint(1000, 9999)}
%%EOF
"""

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"✓ Rechnung erstellt: {filename}")

def create_secret_flag():
    """Erstellt die versteckte Flag-Datei"""
    secret_content = """# Brecher Logistics - Internal Configuration
# STRENG VERTRAULICH - NUR FÜR SYSTEMADMINISTRATOREN

DATABASE_URL = "postgresql://admin:SecureP@ss2024@db.internal:5432/logistics"
API_KEY = "BL-INTERNAL-a7f3d9c2e1b4f6a8"
ADMIN_PASSWORD = "Br3ch3r!Admin#2024"

# CTF Flag - Gefunden via Directory Traversal
FLAG = 'CTF{PATH_TRAVERSAL_MASTER_CLASS}'

# Weitere interne Secrets
JWT_SECRET = "super-secret-jwt-key-do-not-share"
ENCRYPTION_KEY = "AES256-brecher-logistics-key"
"""

    filename = 'secrets/config.py'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(secret_content)

    print(f"✓ Secret-Flag erstellt: {filename}")
    print(f"  → Flag: CTF{{PATH_TRAVERSAL_MASTER_CLASS}}")

def main():
    """Hauptfunktion - Setup durchführen"""
    print("\n" + "="*60)
    print("  P3 - Directory Traversal Setup")
    print("  Brecher Logistics CTF Challenge")
    print("="*60 + "\n")

    print("[1/3] Erstelle Verzeichnisse...")
    create_directories()

    print("\n[2/3] Generiere Fake-Rechnungen...")
    generate_fake_invoices()

    print("\n[3/3] Erstelle Secret-Flag...")
    create_secret_flag()

    print("\n" + "="*60)
    print("  ✓ Setup abgeschlossen!")
    print("="*60)
    print("\nDas System ist bereit für die Challenge.")
    print("Starte die Anwendung mit: python app.py")
    print("\nHinweis für CTF-Teilnehmer:")
    print("Die Flag befindet sich in secrets/config.py")
    print("Exploit: ....//....//secrets/config.py umgeht den Filter!\n")

if __name__ == "__main__":
    main()
