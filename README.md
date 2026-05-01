# 🔄 Feedback 360° - Porte Empresa Júnior

Este repositório contém um script em Python desenvolvido para automatizar a geração de relatórios individuais em PDF para o ciclo de Feedback 360° da **Porte Empresa Júnior (UFJF)**. 

O sistema lê as respostas exportadas de um formulário do Google Sheets (em formato CSV), organiza as notas quantitativas e os comentários qualitativos (pontos positivos e construtivos) e gera um documento PDF com design padronizado para cada membro avaliado.

## 📂 Estrutura do Projeto

O repositório está organizado da seguinte forma:

- `main.py`: O script principal em Python que processa os dados e gera os PDFs.
- `respostas_forms.csv`: Arquivo de exemplo mostrando o formato esperado da planilha de respostas baixada do Google Forms/Sheets.
- `imagem_fundo_capa.png`: Imagem de exemplo utilizada como arte de fundo para a página de capa do relatório.
- `imagem_fundo_laranja.png`: Imagem de exemplo utilizada como arte de fundo para as páginas internas do relatório.

## ⚙️ Pré-requisitos

Para rodar o script no seu computador (Windows), você precisará instalar algumas ferramentas. Siga a ordem abaixo:

1. **Python:** Baixe e instale a versão mais recente em [python.org](https://www.python.org/downloads/). 
   > ⚠️ **Atenção:** Na primeira tela de instalação, certifique-se de marcar a caixa **"Add Python to PATH"**.
2. **Editor de Código (IDE):** Recomendamos o **Visual Studio Code (VS Code)** pela facilidade de uso, mas sinta-se livre para usar qualquer outro editor da sua preferência. Baixe o VS Code em [code.visualstudio.com](https://code.visualstudio.com/).
3. **MSYS2 (Apenas Windows):** Necessário para a biblioteca de geração de PDF (WeasyPrint) renderizar o layout corretamente.
   - Baixe e instale o [MSYS2](https://www.msys2.org/).
   - Abra o aplicativo **MSYS2 UCRT64** no menu iniciar.
   - Cole o comando abaixo no terminal preto e aperte Enter (digite `Y` quando perguntado se deseja prosseguir):
     ```bash
     pacman -S mingw-w64-ucrt-x86_64-pango mingw-w64-ucrt-x86_64-libffi
     ```

## 🚀 Como Utilizar

**Passo 1: Preparar os arquivos**<br>
Coloque o script `main.py`, as duas imagens de fundo (`imagem_fundo_capa.png` e `imagem_fundo_laranja.png`) e a sua planilha de respostas do Google Sheets (baixada no formato `.csv` e renomeada para `respostas_forms.csv`) **dentro da mesma pasta** no seu computador.

**Passo 2: Configurar caminhos no código**<br>
Abra a pasta na IDE e clique no arquivo `main.py`. Verifique as linhas onde o fundo (background-image) é chamado e atualize o caminho para a pasta do seu computador, garantindo que os nomes das imagens correspondam aos arquivos baixados.
Exemplo: `file:///C:/Feedback360Porte/imagem_fundo_capa.png`.

**Passo 3: Instalar as bibliotecas do projeto**<br>
No terminal integrado da IDE (no VS Code, `Terminal > New Terminal` no menu superior) ou no CMD do seu computador, execute o comando abaixo para instalar as dependências necessárias:
```bash
pip install pandas jinja2 weasyprint
```

**Passo 4: Gerar os Relatórios**<br>
Com tudo configurado, basta rodar o script! No mesmo terminal, digite:
```bash
python main.py
```

Uma nova pasta chamada `pdfs_gerados` será criada automaticamente, contendo todos os feedbacks individuais prontos para serem enviados aos membros!

---
*Desenvolvido em colaboração com Maria Carvalho para a Porte Empresa Júnior.*