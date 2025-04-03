from flask import Flask, render_template, request, redirect
import sqlite3

# TODO: Importação das bibliotecas de criptografia
# from ... import ...

app = Flask(__name__)


# Página de Cadastro
@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        # TODO: Implementar criptografia da senha
        encrypted_password = password  # Você deve modificar este trecho!

        # TODO: Implementar criptografia de email
        encrypted_email = email  # Você deve modificar este trecho!

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, encrypted_email, encrypted_password),
        )
        conn.commit()
        conn.close()

        return redirect("/users")

    return render_template("register.html")


# Pagina para visualizar os usuarios cadastrados
@app.route("/users")
def users():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row  # Retorna os resultados como dicionarios
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email, password FROM users")
    users_data = cursor.fetchall()
    conn.close()

    return render_template("users.html", users=users_data)


if __name__ == "__main__":
    app.run(debug=True)
