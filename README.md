
# Sistema Despachante em Django

Este projeto utiliza o **Docker** e o **Docker Compose** para gerenciar e isolar o ambiente de desenvolvimento, incluindo o banco de dados PostgreSQL.

## ⚙️ Configuração Automatizada

O serviço principal da aplicação está configurado com um script de *entrypoint* que garante a prontidão do ambiente:

* **Migrações Automáticas:** Antes de iniciar o servidor, o sistema **aplica automaticamente** todas as migrações pendentes do Django (`python manage.py migrate`), garantindo que a estrutura do banco de dados (PostgreSQL) esteja sempre atualizada.


## 🚀 Como Executar o Projeto
Para colocar o projeto no ar, você só precisa ter o **Docker** instalado na sua máquina.

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
Para parar os contêineres:

```bash
docker compose stop
```

---


### 📝 Projeto em Desenvolvimento   