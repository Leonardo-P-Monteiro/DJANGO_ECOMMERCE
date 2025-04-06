# DJANGO_ECOMMERCE 

Uma plataforma de e-commerce desenvolvida utilizando o framework web Python Django.

Link para acesso no [pythonanywhere].(https://ecommercedjango.pythonanywhere.com/)

![image](https://github.com/user-attachments/assets/c3543efe-c0fc-4660-a866-6bf47a678a06)
![image](https://github.com/user-attachments/assets/c5da64ee-2b71-4eed-a8b6-3a51c0fe723b)
![image](https://github.com/user-attachments/assets/40d190f7-c241-4814-83b4-a399054ade8a)
![image](https://github.com/user-attachments/assets/f6525f79-641e-40f8-aba1-c22576462278)
![image](https://github.com/user-attachments/assets/9d838d9f-4ed7-4920-8f87-ee1aee41b56c)
![image](https://github.com/user-attachments/assets/3c736b09-024d-4151-89ef-52e5b32081cf)
![image](https://github.com/user-attachments/assets/9dc01f05-1647-4174-9d7c-680c82ad6b93)








## 📖 Descrição

Este projeto tem como objetivo criar uma aplicação web de e-commerce funcional, permitindo aos usuários navegar por produtos, adicioná-los ao carrinho e (potencialmente) finalizar compras. Ele serve como um exemplo prático da aplicação dos conceitos do Django na construção de sites dinâmicos e interativos.

## ✨ Funcionalidades Principais (Exemplo)

* Listagem de produtos com paginação.
* Página de detalhes para cada produto.
* Sistema de carrinho de compras.
* Autenticação de usuários (Registro e Login).
* Interface administrativa do Django para gerenciamento de produtos, categorias, pedidos (se implementado), etc.

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python, Django
* **Frontend:** HTML5, CSS, Bootstrap.
* **Banco de Dados:** SQLite (padrão do Django para desenvolvimento).
* **Gerenciamento de Pacotes:** pip

## ⚙️ Pré-requisitos

Antes de começar, garanta que você tenha instalado:

* [Python 3.8+](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installation/) (geralmente vem com o Python)
* [Git](https://git-scm.com/downloads/) (para clonar o repositório)

## 🚀 Instalação e Execução

Siga os passos abaixo para configurar e rodar o projeto localmente:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Leonardo-P-Monteiro/DJANGO_ECOMMERCE.git](https://www.google.com/search?q=https://github.com/Leonardo-P-Monteiro/DJANGO_ECOMMERCE.git)
    cd DJANGO_ECOMMERCE
    ```

2.  **Crie e ative um ambiente virtual:**
    * **Linux/macOS:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * **Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Instale as dependências:**
    *(Certifique-se de que você tem um arquivo `requirements.txt` no seu projeto)*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

5.  **Crie um superusuário (para acesso ao Admin):**
    ```bash
    python manage.py createsuperuser
    ```
    *Siga as instruções para definir nome de usuário, email e senha.*

6.  **Execute o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

7.  **Acesse a aplicação:**
    Abra seu navegador e vá para `http://127.0.0.1:8000/`
    Para acessar a interface administrativa, vá para `http://127.0.0.1:8000/admin/` e use as credenciais do superusuário criado.


## 🤝 Contribuições

Contribuições são bem-vindas! Se você deseja contribuir:

1.  Faça um Fork do projeto.
2.  Crie uma branch para sua feature (`git checkout -b feature/NomeDaFeature`).
3.  Faça commit das suas alterações (`git commit -m 'Adiciona nova feature'`).
4.  Faça push para a sua branch (`git push origin feature/NomeDaFeature`).
5.  Abra um Pull Request.


## 👤 Autor

* **Leonardo P. Monteiro** - [Linkedin](https://www.linkedin.com/in/leonardopmonteiro/)

---
