# Magenitc-one-AGENTIC-InsurTech
Mahentic-one AGENTIC InsurTech workflow system

![magentic-one](https://github.com/user-attachments/assets/16295fb5-bb61-4ab8-9192-389f6370f18a) 



# AGENTIC InsurTech Aplikacija

## Opis
AGENTIC InsurTech je napredna zavarovalniška aplikacija, ki uporablja večagentni sistem MagenticOne za avtomatizacijo zavarovalniških procesov. Aplikacija omogoča oceno tveganja na podlagi slik, izračun premij in avtomatsko obdelavo zahtevkov.

## Uporabljene tehnologije

### Glavni agentni sistem
- **MagenticOne**: Microsoftov večagentni sistem za reševanje kompleksnih nalog
  - Dokumentacija: [MagenticOne](https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/)
  - GitHub: [autogen-magentic-one](https://github.com/microsoft/autogen/tree/main/python/packages/autogen-magentic-one)

### Ključne knjižnice
- `autogen-core`: Jedro agentnega sistema
- `autogen-magentic-one`: Implementacija MagenticOne agentov
- `autogen-ext`: Razširitve za AutoGen
- `gradio`: Uporabniški vmesnik
- `streamlit`: Alternativni uporabniški vmesnik
- `playwright`: Spletno brskanje in zajem podatkov

  ![magentic-one struktura map](https://github.com/user-attachments/assets/ae9bff79-3427-451c-bd89-f3612a2ad420)
  


### API integracije
- Together.ai API: LLM model za procesiranje naravnega jezika
- Stripe API: Procesiranje plačil
- Weather API: Vremenska napoved za parametrično zavarovanje

## Struktura projekta 
Magnetic-one/
├── .env # Konfiguracijske spremenljivke
├── requirements.txt # Potrebni paketi
├── README.md # Dokumentacija
└── src/
├── main.py # Glavna aplikacija
├── agents/ # Implementacije agentov
├── utils/ # Pomožne funkcije
└── runtime/ # Orkestrator in runtime

## Agenti v sistemu

### 1. ResearchAgent
- Analiza slik
- Identifikacija objektov
- Ocena tveganja

### 2. UnderwritingAgent
- Izračun premije
- Določanje kritja
- Ocena tveganja

### 3. SalesAgent
- Priprava ponudb
- Komunikacija s strankami
- Generiranje dokumentov

## Namestitev in zagon

1. Kloniranje repozitorija:
```bash
git clone [repository-url]
cd Magnetic-one
```

2. Ustvarjanje virtualnega okolja:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ali
venv\Scripts\activate     # Windows
```

3. Namestitev potrebnih paketov:
```bash
pip install -r requirements.txt
playwright install --with-deps chromium
```

4. Nastavitev okolja:
- Ustvarite `.env` datoteko
- Dodajte potrebne API ključe:
  - TOGETHER_API_KEY
  - STRIPE_API_KEY
  - NOTION_API_KEY

5. Zagon aplikacije:
```bash
python src/run_app.py --interface gradio
# ali
python src/run_app.py --interface streamlit
```

## Funkcionalnosti

### Osnovne funkcije
- Analiza slik za oceno tveganja
- Avtomatski izračun premij
- Generiranje zavarovalnih polic
- Procesiranje zahtevkov

### Napredne funkcije
- Parametrično vremensko zavarovanje
- Avtomatska izplačila
- Preventivni načrti
- Integracija z zunanjimi viri podatkov

## Razvijalci
- Dokumentacija MagenticOne: [Link](https://github.com/microsoft/autogen/tree/main/python/packages/autogen-magentic-one)

- AutoGen dokumentacija: [Link](https://microsoft.github.io/autogen/)

## Licenca
MIT License



