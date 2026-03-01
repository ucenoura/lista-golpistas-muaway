from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

banidos = [
    {"numero": 1, "nome": "MAGOPEIXE - 81 9603-2026"},
]

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Lista de GOLPISTAS - MuAway</title>
    <style>
        body {
            background: linear-gradient(to bottom, #000000, #1a0000);
            font-family: Arial;
            color: white;
            text-align: center;
        }

        h1 {
            color: gold;
            text-shadow: 0 0 10px red;
        }

        .container {
            width: 400px;
            margin: auto;
        }

        .card {
            background-color: #111;
            border: 1px solid gold;
            padding: 10px;
            margin: 10px 0;
            border-radius: 8px;
        }

        input {
            padding: 8px;
            width: 70%;
            margin: 5px;
            border-radius: 5px;
            border: none;
        }

        button {
            padding: 8px 15px;
            background-color: gold;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
        }

        button:hover {
            background-color: orange;
        }
    </style>
</head>
<body>
    <h1>🔥 LISTA DE BANIDOS - MU 🔥</h1>

    <div class="container">

        <form method="POST">
            <input type="text" name="nome" placeholder="Nome do pilantra" required>
            <button type="submit">Adicionar</button>
        </form>

        {% for pessoa in banidos %}
            <div class="card">
                {{ pessoa.numero }} - {{ pessoa.nome }}
            </div>
        {% endfor %}

    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        nome = request.form["nome"]
        numero = len(banidos) + 1
        banidos.append({"numero": numero, "nome": nome})
        return redirect("/")

    return render_template_string(html, banidos=banidos)

if __name__ == "__main__":
    app.run(debug=True)