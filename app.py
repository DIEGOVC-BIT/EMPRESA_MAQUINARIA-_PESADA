from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
from flask import Flask, render_template_string
 
app = Flask(__name__)
 
pagina_html = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Maquinaria Pesada - Alquiler</title>
 
  <!-- Bootstrap -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
 
  <style>
    body {
      background-color: #f5f5f5;
    }
 
    .navbar {
      background: #d97706;
    }
 
    .navbar-brand {
      color: white !important;
      font-weight: bold;
      font-size: 24px;
    }
 
    .nav-link {
      color: white !important;
    }
 
    .banner {
      background-image: url("https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1200&q=80");
      background-size: cover;
      background-position: center;
      height: 400px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      text-align: center;
    }
 
    .banner-box {
      background: rgba(0,0,0,0.55);
      padding: 36px 48px;
      border-radius: 10px;
    }
 
    .card img {
      height: 210px;
      object-fit: cover;
    }
 
    footer {
      background: #d97706;
      color: white;
      text-align: center;
      padding: 20px;
      margin-top: 40px;
    }
  </style>
</head>
 
<body>
 
<!-- Navbar -->
<nav class="navbar navbar-expand-lg">
  <div class="container">
    <a class="navbar-brand" href="#">🚜 Maquinaria Pesada</a>
    <div class="collapse navbar-collapse">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item"><a class="nav-link" href="#servicios">Servicios</a></li>
        <li class="nav-item"><a class="nav-link" href="#maquinas">Maquinaria</a></li>
        <li class="nav-item"><a class="nav-link" href="#precios">Precios</a></li>
        <li class="nav-item"><a class="nav-link" href="#contacto">Contacto</a></li>
      </ul>
    </div>
  </div>
</nav>
 
<!-- Banner -->
<section class="banner">
  <div class="banner-box">
    <h1>Alquiler de Maquinaria Pesada</h1>
    <p>Retroexcavadoras, Volquetes, Excavadoras, Minicargadores y más</p>
    <button class="btn btn-warning btn-lg mt-2">Ver servicios</button>
  </div>
</section>
 
<!-- Maquinaria -->
<div class="container mt-5" id="maquinas">
  <h2 class="mb-4">Nuestra Maquinaria</h2>
  <div class="row g-4">
 
    <div class="col-md-3">
      <div class="card shadow">
        <img src="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600&q=80" alt="Retroexcavadora">
        <div class="card-body">
          <h5>Retroexcavadora</h5>
          <p>Zanjas, cimentaciones y movimiento de tierra.</p>
          <button class="btn btn-warning">Consultar</button>
        </div>
      </div>
    </div>
 
    <div class="col-md-3">
      <div class="card shadow">
        <img src="https://images.unsplash.com/photo-1580674684081-7617fbf3d745?w=600&q=80" alt="Volquete">
        <div class="card-body">
          <h5>Volquete</h5>
          <p>Transporte de tierra, piedra, afirmado y desmonte.</p>
          <button class="btn btn-warning">Consultar</button>
        </div>
      </div>
    </div>
 
    <div class="col-md-3">
      <div class="card shadow">
        <img src="https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122?w=600&q=80" alt="Minicargador">
        <div class="card-body">
          <h5>Minicargador</h5>
          <p>Espacios reducidos, carga y descarga de materiales.</p>
          <button class="btn btn-warning">Consultar</button>
        </div>
      </div>
    </div>
 
    <div class="col-md-3">
      <div class="card shadow">
        <img src="https://images.unsplash.com/photo-1541888946425-d81bb19240f5?w=600&q=80" alt="Excavadora">
        <div class="card-body">
          <h5>Excavadora</h5>
          <p>Excavaciones profundas y nivelación de terrenos.</p>
          <button class="btn btn-warning">Consultar</button>
        </div>
      </div>
    </div>
 
  </div>
</div>
 
<!-- Servicios -->
<div class="container mt-5" id="servicios">
  <h2 class="mb-4">Servicios que ofrecemos</h2>
  <div class="row g-3">
    <div class="col-md-4">
      <div class="card shadow text-center p-3">
        <div style="font-size:40px">⛏️</div>
        <h5 class="mt-2">Movimiento de Tierra</h5>
        <p class="text-muted">Corte, relleno, compactación y nivelación de terrenos.</p>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card shadow text-center p-3">
        <div style="font-size:40px">🏗️</div>
        <h5 class="mt-2">Demolición</h5>
        <p class="text-muted">Demolición de estructuras con equipos especializados.</p>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card shadow text-center p-3">
        <div style="font-size:40px">📐</div>
        <h5 class="mt-2">Zanjado</h5>
        <p class="text-muted">Zanjas para tuberías, drenaje y sistemas de cable.</p>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card shadow text-center p-3">
        <div style="font-size:40px">🪨</div>
        <h5 class="mt-2">Suministro de Piedra</h5>
        <p class="text-muted">Piedra chancada, base y sub-base para obras.</p>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card shadow text-center p-3">
        <div style="font-size:40px">🛤️</div>
        <h5 class="mt-2">Afirmado</h5>
        <p class="text-muted">Material granular para caminos y plataformas.</p>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card shadow text-center p-3">
        <div style="font-size:40px">🏗️</div>
        <h5 class="mt-2">Hormigón</h5>
        <p class="text-muted">Suministro y vaciado de hormigón para cimentaciones.</p>
      </div>
    </div>
  </div>
</div>
 
<!-- Tabla de precios -->
<div class="container mt-5" id="precios">
  <h2 class="mb-4">Tarifas Referenciales</h2>
  <table class="table table-striped table-bordered shadow">
    <thead style="background:#d97706; color:white;">
      <tr>
        <th>Maquinaria / Servicio</th>
        <th>Precio por hora</th>
        <th>Disponibilidad</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Retroexcavadora</td>
        <td>Consultar</td>
        <td>✅ Disponible</td>
      </tr>
      <tr>
        <td>Volquete</td>
        <td>Consultar</td>
        <td>✅ Disponible</td>
      </tr>
      <tr>
        <td>Minicargador</td>
        <td>Consultar</td>
        <td>✅ Disponible</td>
      </tr>
      <tr>
        <td>Excavadora</td>
        <td>Consultar</td>
        <td>✅ Disponible</td>
      </tr>
      <tr>
        <td>Demolición (servicio)</td>
        <td>Consultar</td>
        <td>✅ Disponible</td>
      </tr>
      <tr>
        <td>Zanjado (servicio)</td>
        <td>Consultar</td>
        <td>✅ Disponible</td>
      </tr>
    </tbody>
  </table>
</div>
 
<!-- Contacto -->
<div class="container mt-5 mb-5" id="contacto">
  <h2>Contacto</h2>
  <p>📍 Lima - Perú</p>
  <p>📞 999 000 000</p>
  <p>🕒 Lunes a sábado: 7:00 am - 6:00 pm</p>
  <p>💬 Cotizaciones sin compromiso</p>
</div>
 
<footer>
  © 2026 Maquinaria Pesada - Lima, Perú | Hecho con Python + Flask
</footer>
 
</body>
</html>
"""
 
@app.route("/")
def inicio():
    return render_template_string(pagina_html)
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
