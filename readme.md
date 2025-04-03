# Segurança de Senhas em Aplicações Web  

Este projeto apresenta um sistema simples de cadastro de usuários utilizando **Flask** e **SQLite**. No entanto, a implementação inicial não protege corretamente os dados armazenados.

O objetivo desta atividade é corrigir essa vulnerabilidade, implementando a criptografia correta para armazenar dados de forma segura.

## Estrutura do Projeto  

```
/Criptografia
│── /templates
│   │── register.html  # Página de cadastro de usuários
│   │── users.html     # Página para visualizar usuários cadastrados
│   │── login.html     # TODO: Formulário para login de usuário (atividade extra).
│── app.py             # Aplicação Flask principal
│── database.py        # Inicializa o banco de dados SQLite
│── database.db        # Arquivo do banco de dados SQLite (gerado após rodar database.py)
│── requirements.txt   # Lista de dependências do projeto
│── README.md          # Documentação do projeto
```

---

## Enunciado da Atividade  

O sistema atual permite que usuários cadastrem seu nome, e-mail e senha. No entanto, os dados **não estão protegidos adequadamente**. Seu desafio é modificar o código para garantir que as senhas e e-mail sejam armazenadas de maneira segura.  

### **Tarefa 1**  

1. Implementar **forma de armazenamento de dados** para senha:  
   - **Senha com criptografia adequada** → Protege as senhas de maneira irreversível.  

2. Modificar o código do arquivo **`app.py`**, na função de cadastro, substituindo a variável de senha pelo método adequado de criptografia.

3. Testar o comportamento do sistema apresentado os dados em **`users.html`**.


### **Tarefa 2**  
1. Implementar **criptografia** de campo reversível
   - **E-mail com criptografia adequada** → Protege os e-mails de maneira reversível.

2. Modificar o código do arquivo **`app.py`**, na função de cadastro, substituindo a variável de e-mail pelo método adequado de criptografia.

3. O e-mail deve ser apresentado descriptografado em **`users.html`**.

### **Tarefa 3**  
1. Todas as bibliotecas novas usadadas devem ser inseridas em   **`requirements.txt`**.

### **Atividade extra**  
1. Crie uma nova página **`login.html`** com campos para email/senha, juntamente com um botão **enviar**, **simulando** o login do usuário.

2. O botão **enviar** deve fazer o processamento **adequado** para o e-mail e senha para verificar se os valores batem com os valores do banco de dados.

3. Apresentar mensagem de **sucesso** ou **inválido** ao realizar a operação. Caso sucesso, **apresentar dados do usuário**.


---

## Arquivos Relevantes  

### **1. `app.py`**  
- Contém a lógica da aplicação Flask.  
- A função `register()` deve ser modificada para aplicar a criptografia correta.  
- O trecho a ser alterado está na variável `encrypted_password` e no campo `encrypted_email`. 

### **2. `database.py`**  
- Cria o banco de dados SQLite.  
- Deve ser executado ao menos uma vez antes de iniciar o servidor Flask.
- Se executado novamente, irá re-criar o banco de dados.

### **3. `templates/register.html`**  
- Formulário de cadastro de usuários.  

### **4. `templates/users.html`**  
- Exibe a lista de usuários cadastrados.  

### **4. `templates/login.html`**  
- **TODO**: Formulário para login de usuário.

---

## Como Configurar e Executar o Projeto  

### **1. Criar e ativar enviroment**
```bash
conda create -n criptografia python=3.6.0
conda activate criptografia
```

### **1. Instalar Dependências**  

```bash
pip install -r requirements.txt
```

### **2. Criar o Banco de Dados**  

```bash
python database.py
```

### **3. Iniciar o Servidor Flask**  

```bash
python app.py
```

### **4. Acessar no Navegador**  
Abra o navegador e acesse:  

```
http://127.0.0.1:5000/
```

---

## Dicas e Diretrizes  

- Utilize alguma biblioteca para o armazenamento seguro das senhas.
- Evite armazenar senhas utilizando criptografia reversível, pois isso compromete a segurança do sistema.  
- Faça testes cadastrando usuários e verificando como as senhas são armazenadas no banco.  
- Compare os resultados obtidos com hashing e criptografia reversível para entender os riscos de cada abordagem. 
- Para instalar bibliotecas você pode utilizar o comando ``bash pip install <biblioteca>``.

- Recomendações: **werkzeug**, **bcrypt**, **hashlib**, **cryptography**
---

## Referências  

- [Werkzeug Security - Password Hashing](https://werkzeug.palletsprojects.com/en/latest/utils/#module-werkzeug.security)
- [bcrypt](https://pypi.org/project/bcrypt/)
- [Hashlib](https://docs.python.org/3/library/hashlib.html)
- [Python Cryptography Library](https://cryptography.io/)
- [Flask Documentation](https://flask.palletsprojects.com/)

---

Este repositório foi desenvolvido para fins educacionais e visa demonstrar boas práticas de segurança na implementação de sistemas web.  