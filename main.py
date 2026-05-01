import pandas as pd
from jinja2 import Environment, DictLoader
import os
os.add_dll_directory(r"C:\msys64\ucrt64\bin")
from weasyprint import HTML, CSS

# 1. TEMPLATE HTML/CSS
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Feedback 360°</title>
    <style>
        /* Importação de fontes */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Poppins:wght@500;600;700&display=swap');

        /* Regras de Página e Arte de Fundo */
        @page {
            size: A4 portrait;
            margin: 0;
            
            /* Fundo Laranja para todas as páginas (exceto a primeira) */
            background-image: url('file:///C:/Feedback360Porte/imagem_fundo_laranja.png');
            background-position: center;
            background-size: 100% 100%;
            background-repeat: no-repeat;
        }

        /* Regra específica para a primeira página */
        @page :first {
            background-image: url('file:///C:/Feedback360Porte/imagem_fundo_capa.png');
        }

        /* Variáveis de Cor */
        :root {
            --primary: #F26522;
            --secondary: #4A5568;
            --bg-light: #F7FAFC;
            --border-color: #E2E8F0;
            --text-dark: #1A202C;
        }

        /* Estilos Globais */
        body {
            font-family: 'Inter', sans-serif;
            color: var(--text-dark);
            margin: 0;
            padding: 2cm 2cm 2.5cm 2cm;
            box-sizing: border-box;
            line-height: 1.6;
            font-size: 10pt;
            background-color: transparent;
        }

        /* Capa */
        .cover {
            text-align: center;
            page-break-after: always;
            padding-top: 25%;
        }
        .cover h1 {
            font-family: 'Poppins', sans-serif;
            color: var(--primary);
            font-size: 40pt;
            margin-bottom: 0px;
            text-transform: uppercase;
            letter-spacing: 2px;
            line-height: 1.1;
        }
        .cover h2 {
            font-family: 'Poppins', sans-serif;
            font-size: 22pt;
            color: var(--bg-light);
            font-weight: 500;
            margin-top: 15px;
        }
        .intro-box {
            margin-top: 60px;
            background-color: var(--bg-light);
            border-left: 4px solid var(--primary);
            padding: 25px 35px;
            border-radius: 0 8px 8px 0;
            text-align: justify;
            box-shadow: 0 2px 4px rgba(0,0,0,0.03);
        }
        .intro-box p {
            margin: 0;
            font-size: 11pt;
            color: var(--secondary);
        }

        /* Seções Gerais */
        .section {
            page-break-before: always;
            padding-top: 10px;
        }
        .section-title {
            font-family: 'Poppins', sans-serif;
            color: var(--bg-light);
            font-size: 18pt;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 8px;
            margin-bottom: 25px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        /* Tabelas Quantitativas */
        .avaliador-nome {
            font-family: 'Poppins', sans-serif;
            font-size: 12pt;
            color: var(--text-dark);
            margin-top: 30px;
            margin-bottom: 10px;
        }
        .avaliador-nome span {
            color: var(--bg-light);
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 30px;
            background-color: #ffffff;
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid var(--border-color);
            page-break-inside: avoid; /* Evita que a tabela se quebre no meio */
        }
        /* Cabeçalho */
        th {
            background-color: var(--bg-light);
            color: var(--secondary);
            font-family: 'Poppins', sans-serif;
            text-transform: uppercase;
            font-size: 9pt;
            letter-spacing: 0.5px;
            padding: 12px 15px;
            text-align: left;
            border-bottom: 2px solid var(--border-color);
        }
        /* Texto */
        td {
            padding: 12px 15px;
            font-size: 8pt;
            color: var(--secondary);
            border-bottom: 1px solid var(--border-color);
        }
        tr:last-child td {
            border-bottom: none;
        }
        tr:nth-child(even) td {
            background-color: #FAFCFF;
        }
        .score-cell {
            text-align: center;
            width: 80px;
        }
        /* Design em "Badge" para as notas */
        .score-badge {
            display: inline-block;
            background-color: var(--primary);
            color: white;
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
            font-size: 10pt;
            padding: 4px 12px;
            border-radius: 12px;
        }

        /* Cards de Feedback Qualitativo */
        .feedback-grid {
            display: block;
        }
        .feedback-card {
            background-color: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 25px;
            margin-bottom: 25px;
            page-break-inside: avoid;
            position: relative;
            box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        }
        /* Detalhe visual colorido no topo do card */
        .feedback-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background-color: var(--bg-light);
            border-radius: 8px 8px 0 0;
        }
        .feedback-card h4 {
            font-family: 'Poppins', sans-serif;
            margin: 0 0 20px 0;
            color: var(--text-dark);
            font-size: 12pt;
            border-bottom: 1px dashed var(--border-color);
            padding-bottom: 10px;
        }
        .feedback-section {
            margin-bottom: 15px;
        }
        .feedback-section:last-child {
            margin-bottom: 0;
        }
        .tag {
            font-family: 'Poppins', sans-serif;
            font-size: 8pt;
            text-transform: uppercase;
            letter-spacing: 1px;
            display: inline-block;
            margin-bottom: 8px;
            padding: 4px 10px;
            border-radius: 4px;
            font-weight: 600;
        }
        .tag-positivo {
            background-color: #E6F4EA;
            color: #1E8E3E;
        }
        .tag-construtivo {
            background-color: #FCE8E6;
            color: #D93025;
        }
        .feedback-text {
            margin: 0;
            color: var(--secondary);
            text-align: justify;
            line-height: 1.7;
            font-size: 10pt;
        }
        .quote-mark {
            position: absolute;
            right: 20px;
            bottom: 10px;
            font-size: 40pt;
            font-family: serif;
            color: var(--border-color);
            opacity: 0.4;
            line-height: 1;
        }
    </style>
</head>
<body>

    <div class="cover">
        <h1>Feedback 360°</h1>
        <h2>{{ destinatario }}</h2>
        <div class="intro-box">
            <p>
                Este é o ciclo de feedbacks da gestão. Seja receptivo ao conteúdo apresentado e mantenha a mente aberta para as respostas. A ferramenta contribuirá para o seu desenvolvimento individual e para a melhoria contínua de todo o time, além de aprimorar nosso ambiente de trabalho.
            </p>
        </div>
    </div>

    <div class="section">
        <h2 class="section-title">Avaliações Quantitativas</h2>
        
        {% for avaliacao in avaliacoes %}
        <div class="avaliador-block" style="{% if not loop.last %}page-break-after: always;{% endif %}">
            <div class="avaliador-nome">Avaliador: <span>{{ avaliacao.remetente }}</span></div>
            <table>
                <tr>
                    <th>Critério Avaliado</th>
                    <th style="text-align: center;">Nota</th>
                </tr>
                {% for criterio, nota in avaliacao.notas.items() %}
                <tr>
                    <td>{{ criterio }}</td>
                    <td class="score-cell"><span class="score-badge">{{ nota }}</span></td>
                </tr>
                {% endfor %}
            </table>
        </div>
        {% endfor %}
    </div>

    <div class="section">
        <h2 class="section-title">Feedbacks Qualitativos</h2>
        
        <div class="feedback-grid">
            {% for avaliacao in avaliacoes %}
            <div class="feedback-card">
                <h4>Feedback de: {{ avaliacao.remetente }}</h4>
                
                <div class="feedback-section">
                    <span class="tag tag-positivo">Pontos Positivos</span>
                    <p class="feedback-text">{{ avaliacao.positivo }}</p>
                </div>
                
                <div class="feedback-section">
                    <span class="tag tag-construtivo">Pontos Construtivos</span>
                    <p class="feedback-text">{{ avaliacao.construtivo }}</p>
                </div>
                <div class="quote-mark">”</div>
            </div>
            {% endfor %}
        </div>
    </div>

</body>
</html>
"""

def gerar_pdfs(csv_path, output_dir):
    # Cria o diretório de saída se não existir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Carrega os dados do csv
    df = pd.read_csv(csv_path)
    
    # Lista de colunas que NÃO são as perguntas
    colunas_texto = ['Email do Remetente', 'Remetente', 'Destinatário', 'Feedback Positivo', 'Feedback Construtivo']
    
    colunas_perguntas = [col for col in df.columns if col not in colunas_texto]
    
    # Configura o Jinja2 com o template HTML
    env = Environment(loader=DictLoader({'template.html': HTML_TEMPLATE}))
    template = env.get_template('template.html')

    # Agrupamento por destinatário
    grupos = df.groupby('Destinatário')

    for destinatario, dados_grupo in grupos:
        avaliacoes = []
        
        for _, row in dados_grupo.iterrows():
            # Mapeia as perguntas e as respectivas notas
            notas = {col: row[col] for col in colunas_perguntas}
            
            avaliacoes.append({
                'remetente': row['Remetente'],
                'notas': notas,
                'positivo': row['Feedback Positivo'],
                'construtivo': row['Feedback Construtivo']
            })
        
        # Renderiza o HTML com os dados do destinatário e suas avaliações
        html_renderizado = template.render(
            destinatario=destinatario,
            avaliacoes=avaliacoes
        )
        
        # Gera o PDF
        output_file = os.path.join(output_dir, f"Feedback_{destinatario.replace(' ', '_')}.pdf")
        HTML(string=html_renderizado, base_url=os.path.abspath('.')).write_pdf(output_file)
        
        print(f"✅ PDF gerado com sucesso para: {destinatario}")

gerar_pdfs('respostas_forms.csv', 'pdfs_gerados')