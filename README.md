# JenkinsCLI

Uma ferramenta de linha de comando para interagir com servidores Jenkins, permitindo buscar jobs e exportar histórico de builds para CSV.

## 🚀 Funcionalidades

- **Busca de Jobs**: Encontra jobs Jenkins pelo nome, navegando recursivamente através de folders
- **Exportação de Histórico**: Exporta histórico de builds para arquivo CSV com informações detalhadas
- **Suporte a Folders**: Navega automaticamente através da estrutura hierárquica do Jenkins
- **Autenticação Segura**: Utiliza tokens de API para autenticação segura

## 📋 Pré-requisitos

- Python 3.6+
- Acesso a um servidor Jenkins
- Token de API Jenkins configurado

## 🛠️ Instalação

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd JenkinsCLI
   ```

2. **Configure as variáveis de ambiente:**
   Crie um arquivo `.env` na raiz do projeto:
   ```bash
   JENKINS_URL=https://seu-jenkins.com
   JENKINS_USER=seu-usuario
   JENKINS_TOKEN=seu-token-api
   ```

3. **Instale as dependências:**
   ```bash
   make
   ```
   
   Ou manualmente:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## 📖 Como Usar

### Buscar um Job Específico

```bash
source venv/bin/activate
python jenkins_find_job.py
```

O script solicitará o nome do job e retornará o caminho completo se encontrado.

### Exportar Histórico de Builds

```bash
make run
```

Ou manualmente:
```bash
source venv/bin/activate
python jenkins_history_csv.py
```

O script irá:
1. Buscar todos os jobs recursivamente
2. Coletar os últimos 50 builds de cada job
3. Exportar para `jenkins_builds.csv`

## 📊 Formato do CSV

O arquivo de saída contém as seguintes colunas:

| Coluna | Descrição |
|--------|-----------|
| Path | Caminho hierárquico do job |
| Job | Nome do job |
| Build Number | Número do build |
| Status | Status do build (SUCCESS, FAILURE, etc.) |
| Timestamp | Data e hora do build |
| Duration (s) | Duração em segundos |

## 🔧 Estrutura do Projeto

```
JenkinsCLI/
├── jenkins_find_job.py      # Script para buscar jobs
├── jenkins_history_csv.py   # Script para exportar histórico
├── requirements.txt          # Dependências Python
├── Makefile                 # Comandos de automação
├── .env                     # Configurações (criar manualmente)
└── venv/                    # Ambiente virtual Python
```

## 🔐 Configuração do Token Jenkins

1. Acesse seu Jenkins
2. Vá em **Manage Jenkins** → **Manage Users**
3. Clique no seu usuário
4. Clique em **Configure**
5. Em **API Token**, gere um novo token
6. Use este token no arquivo `.env`

## 📝 Exemplo de Uso

```bash
# Ativar ambiente virtual
source venv/bin/activate

# Buscar um job
python jenkins_find_job.py
# Digite: meu-job-name

# Exportar histórico
python jenkins_history_csv.py
# Resultado: jenkins_builds.csv
```

## 🐛 Solução de Problemas

### Erro de Autenticação
- Verifique se as credenciais no `.env` estão corretas
- Confirme se o token tem permissões adequadas

### Job não encontrado
- Verifique se o nome está correto (case-insensitive)
- Confirme se o job não está em uma pasta aninhada

### Erro de conexão
- Verifique se a URL do Jenkins está acessível
- Confirme se não há firewall bloqueando a conexão

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Suporte

Para dúvidas ou problemas, abra uma issue no repositório do projeto.
