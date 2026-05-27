
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Servicios de Maquinaria Pesada</title>

    <style>

        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
        }

        body{
            font-family:Arial, sans-serif;
            background:#f4f4f4;
            color:#333;
        }

        /* ================= HEADER ================= */

        header{
            background:#111;
            color:white;
            padding:20px;
            display:flex;
            justify-content:space-between;
            align-items:center;
        }

        header h1{
            color:orange;
        }

        nav a{
            color:white;
            text-decoration:none;
            margin-left:20px;
            font-weight:bold;
        }

        /* ================= HERO ================= */

        .hero{
            height:90vh;
            background-image:url('/static/images/excavadora.jpg');
            background-size:cover;
            background-position:center;
            display:flex;
            justify-content:center;
            align-items:center;
            text-align:center;
            color:white;
        }

        .hero-content{
            background:rgba(0,0,0,0.6);
            padding:40px;
            border-radius:10px;
        }

        .hero h2{
            font-size:55px;
            margin-bottom:20px;
        }

        .hero p{
            font-size:22px;
            margin-bottom:30px;
        }

        .btn{
            background:orange;
            color:black;
            padding:15px 30px;
            text-decoration:none;
            border-radius:5px;
            font-weight:bold;
            margin:10px;
            display:inline-block;
        }

        /* ================= SERVICIOS ================= */

        .servicios{
            padding:60px 20px;
            text-align:center;
        }

        .servicios h2{
            font-size:40px;
            margin-bottom:40px;
            color:#222;
        }

        .cards{
            display:grid;
            grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
            gap:25px;
        }

        .card{
            background:white;
            border-radius:10px;
            overflow:hidden;
            box-shadow:0px 5px 15px rgba(0,0,0,0.2);
            transition:0.3s;
        }

        .card:hover{
            transform:translateY(-10px);
        }

        .card img{
            width:100%;
            height:220px;
            object-fit:cover;
        }

        .card h3{
            margin:20px 0;
            color:#ff6600;
        }

        .card p{
            padding:0 20px 20px;
            line-height:1.6;
        }

        /* ================= SECCION EXTRA ================= */

        .extra{
            background:#222;
            color:white;
            padding:60px 20px;
            text-align:center;
        }

        .extra h2{
            font-size:40px;
            margin-bottom:20px;
            color:orange;
        }

        .extra p{
            max-width:900px;
            margin:auto;
            line-height:1.8;
            font-size:20px;
        }

        /* ================= FOOTER ================= */

        footer{
            background:#111;
            color:white;
            text-align:center;
            padding:20px;
        }

        /* ================= RESPONSIVE ================= */

        @media(max-width:768px){

            .hero h2{
                font-size:35px;
            }

            .hero p{
                font-size:18px;
            }

        }

    </style>

</head>

<body>

    <!-- ================= HEADER ================= -->

    <header>

        <h1>🚜 MAQUINARIA PESADA</h1>

        <nav>
            <a href="#">Inicio</a>
            <a href="#">Servicios</a>
            <a href="#">Proyectos</a>
            <a href="#">Contacto</a>
        </nav>

    </header>

    <!-- ================= HERO ================= -->

    <section class="hero">

        <div class="hero-content">

            <h2>ALQUILER DE MAQUINARIA PESADA</h2>

            <p>
                Retroexcavadora, Excavadora, Volquete,
                Minicargador y Movimiento de Tierra.
            </p>

            <a href="#" class="btn">📞 Cotizar</a>

            <a href="#" class="btn">🚧 Ver Servicios</a>

        </div>

    </section>

    <!-- ================= SERVICIOS ================= -->

    <section class="servicios">

        <h2>NUESTROS SERVICIOS</h2>

        <div class="cards">

            <!-- CARD 1 -->

            <div class="card">

                <img src="/static/images/retro.jpg">

                <h3>Retroexcavadora</h3>

                <p>
                    Servicio profesional de excavación,
                    zanjas, nivelación y movimientos de tierra.
                </p>

            </div>

            <!-- CARD 2 -->

            <div class="card">

                <img src="/static/images/volquete.jpg">

                <h3>Volquete</h3>

                <p>
                    Transporte de materiales,
                    eliminación de desmonte,
                    tierra y piedra.
                </p>

            </div>

            <!-- CARD 3 -->

            <div class="card">

                <img src="/static/images/minicargador.jpg">

                <h3>Minicargador</h3>

                <p>
                    Limpieza de terrenos,
                    trabajos rápidos y compactos
                    para construcción.
                </p>

            </div>

            <!-- CARD 4 -->

            <div class="card">

                <img src="/static/images/excavadora.jpg">

                <h3>Excavadora</h3>

                <p>
                    Demoliciones, excavaciones profundas,
                    movimiento de grandes volúmenes de tierra.
                </p>

            </div>

        </div>

    </section>

    <!-- ================= EXTRA ================= -->

    <section class="extra">

        <h2>TRABAJOS DE CONSTRUCCIÓN Y MOVIMIENTO DE TIERRA</h2>

        <p>
            Realizamos trabajos de excavación,
            demoliciones, zanjas, transporte de materiales,
            hormigón, afirmado, piedra, nivelación de terrenos
            y alquiler de maquinaria pesada para obras civiles
            y proyectos de construcción.
        </p>

    </section>

    <!-- ================= FOOTER ================= -->

    <footer>

        <p>
            © 2026 Servicios de Maquinaria Pesada |
            Todos los derechos reservados
        </p>

    </footer>

</body>
</html>
