# 🚀 Microsserviços Docker - Toshiro Shibakita

**Desafio DIO: Docker com Microsserviços**  
Implementação completa de arquitetura de microsserviços utilizando Docker Compose, Nginx Load Balancer e múltiplas linguagens.

[![Docker Compose](https://img.shields.io/badge/Docker-Compose-2496ED.svg)](https://docs.docker.com/compose/)
[![Nginx](https://img.shields.io/badge/Nginx-009639.svg)](https://nginx.org/)
[![Node.js](https://img.shields.io/badge/Node.js-43853D.svg)](https://nodejs.org/)
[![Python](https://img.shields.io/badge/Python-3776AB.svg)](https://python.org/)
[![PHP](https://img.shields.io/badge/PHP-777BB4.svg)](https://php.net/)

## 🏗️ Arquitetura da Solução
Internet → [Nginx:80 (Load Balancer)]
↓ (Round Robin)
┌─────────────────────────────┐
│ Node.js (App1:3001) │
│ Python Flask (App2:3002) │
│ PHP Apache (App3:3003) │
└─────────────────────────────┘
             ↓
        Banco Persistente

## ✨ Funcionalidades Implementadas

- ✅ **Load Balancing** com Nginx (3 microsserviços)
- ✅ **4 Microsserviços** em linguagens diferentes (Node.js, Python, PHP, MySQL)
- ✅ **Rede Docker isolada** (`microsservicos-net`)
- ✅ **Persistência MySQL** com volume e script de inicialização
- ✅ **Health Check** no Nginx (`/health`)
- ✅ **Restart automático** dos containers
- ✅ **Configuração Zero** (basta `docker compose up -d`)

## 🚀 Como Executar

### Pré-requisitos
Docker 20+
Docker Compose v2+
4GB RAM disponível


### 1. Clonar repositório
git clone https://github.com/gkaahara/microsservicos-docker.git
cd microsservicos-docker


### 2. Subir ambiente completo
docker compose up -d --build


### 3. Verificar status
docker compose ps


### 4. Testar APIs

**Nginx Gateway (Load Balancer):**
curl http://localhost
Retorna JSON aleatório de um dos 3 microsserviços


**Health Check:**
curl http://localhost/health
"Nginx Gateway OK - Microsservicos Docker"


**Status Nginx:**
curl http://localhost/status


**MySQL direto:**
docker compose exec mysql mysql -uroot -proot123 -Dmicrosservicos -e "SELECT * FROM logs;"


## 📋 Endpoints Disponíveis

| Serviço | Endpoint | Porta | Descrição |
|---------|----------|-------|-----------|
| **Nginx Gateway** | `http://localhost` | 80 | Load Balance para microsserviços |
| **Health Check** | `http://localhost/health` | 80 | Status do Gateway |
| **MySQL** | `mysql://root:root123@localhost:3306/microsservicos` | 3306 | Banco persistente |

## 🔧 Comandos Úteis
Logs em tempo real
docker compose logs -f nginx

Verificar recursos
docker stats

Reiniciar um serviço
docker compose restart app1

Parar tudo
docker compose down

Limpar tudo (inclui volumes)
docker compose down -v


## 📊 Estrutura do Projeto
microsservicos-docker/
├── apps/
│ ├── app1/ # Node.js API (porta 3001)
│ ├── app2/ # Python Flask (porta 3002)
│ └── app3/ # PHP Apache (porta 3003)
├── mysql/
│ └── init.sql # Inicialização automática
├── nginx/
│ └── nginx.conf # Load Balancer config
├── docker-compose.yml # Orquestração completa
└── README.md # 📄 Você está aqui!


## 🎯 Melhorias Implementadas

1. **Load Balancing Round Robin** entre 3 microsserviços
2. **Rede Docker personalizada** para isolamento
3. **MySQL persistente** com dados em volume
4. **Script init.sql** executado automaticamente
5. **Health endpoints** para monitoramento
6. **Restart policy** para alta disponibilidade
7. **Configuração zero-downtime** pronta para produção

## 🛠️ Tecnologias Utilizadas

| Componente | Tecnologia | Versão |
|------------|------------|--------|
| Orquestrador | Docker Compose | v2+ |
| Gateway | Nginx | Alpine |
| App1 | Node.js + Express | 18 |
| App2 | Python + Flask | 3.11 |
| App3 | PHP + Apache | 8.2 |
| Banco | MySQL | 8.0 |

## 📈 Monitoramento
Containers ativos
docker compose ps

Uso de CPU/RAM
docker stats

Logs detalhados
docker compose logs -f

Rede interna
docker network inspect microsservicos-docker_microsservicos-net


## 📝 Autoria

**Desenvolvido por:** Gabriel Kaahara  
**Desafio:** DIO - Docker Microsservicos Toshiro Shibakita  
**Data:** Dezembro 2025  

---
<p align="center">
  <img src="https://img.shields.io/badge/Status-✅%20Produção-green.svg" alt="Status">
  <img src="https://img.shields.io/badge/Docker-Ready-0db7ed.svg" alt="Docker Ready">
</p>
