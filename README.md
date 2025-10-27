
# Sistema Despachante em Django

Este projeto utiliza o Docker para gerenciar e isolar o ambiente de desenvolvimento, incluindo o banco de dados PostgreSQL.

## 🚀 Como Executar o Projeto

Para colocar o projeto no ar, você só precisa ter o **Docker** instalados na sua máquina.

---
### 1. Iniciar o Serviço

Execute o comando a seguir no terminal, a partir do diretório raiz do projeto:

```bash
docker compose up -d
```

Este comando irá:
* Construir (ou baixar) as imagens necessárias.
* Criar e iniciar os contêineres do seu aplicativo e do PostgreSQL.
* A flag -d (detached) faz com que os contêineres rodem em segundo plano.

### 2. Acessar o Sistema

O aplicativo estará disponível imediatamente. Para acessá-lo:
Abra seu navegador e digite o seguinte endereço:

```bash
http://localhost:8000
```
### 3. Parar o Serviço
Para parar e remover os contêineres (mas manter os volumes de dados, como o do banco de dados):

```bash
docker compose stop
```
```bash
docker compose down -v
```
---


### Projeto em Desenvolvimento