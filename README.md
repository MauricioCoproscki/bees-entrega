# BEES Brewery Pipeline

##  Objetivo
Pipeline de dados utilizando a API Open Brewery DB, organizado em arquitetura Medallion (Bronze, Silver e Gold) com Airflow e Docker.

## 🏗️ Arquitetura
- **Bronze:** Dados crus da API (JSON).
- **Silver:** Dados tratados, particionados por estado (Parquet).
- **Gold:** Dados agregados por tipo e estado (Parquet).

## 🔧 Tecnologias
- Python
- Apache Airflow
- Docker
- Pandas
- Parquet

## ⚙️ Como executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/bees-entrega.git
cd bees-entrega
```

2. Suba o ambiente:
```bash
docker-compose up --build
```

3. Acesse o Airflow em:
```
http://localhost:8080
```
Usuário/senha padrão: `airflow` / `airflow`

4. Execute o DAG `brewery_pipeline`.

## 🧪 Rodar testes
```bash
pip install -r requirements.txt
pytest tests/
```

## 🚥 Monitoramento
- Airflow controla falhas e retries.
- Futuramente pode ser integrado com Slack, e-mail ou Prometheus.

## 📂 Dados
- Dados armazenados na pasta `/data` com as subdivisões:
  - `/bronze`
  - `/silver`
  - `/gold`


