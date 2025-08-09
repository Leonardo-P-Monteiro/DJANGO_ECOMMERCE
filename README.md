# [DJANGO_ECOMMERCE](https://ecommercedjango.pythonanywhere.com/)

Uma plataforma de e-commerce desenvolvida utilizando o framework web Python Django.

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
