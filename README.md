# 📄 Conversor de PDF para Markdown

Aplicação web em Python/Streamlit que converte **arquivos PDF em Markdown (.md)**, usando a biblioteca PyMuPDF4LLM.

## 🎯 O que faz

| Entrada | Saída |
| --- | --- |
| `.pdf` | **`.md`** (Markdown) |

- Interface de tela única (upload → converter → baixar)
- Reconstrói títulos, **negrito**/*itálico*, listas e tabelas em Markdown (não é apenas texto corrido)
- OCR automático em páginas escaneadas quando o Tesseract está disponível no sistema — lê **português e inglês** (`ocr_language="por+eng"`); páginas com texto nativo não passam por OCR
- Processamento em diretórios temporários — nenhum arquivo é armazenado

## 🚀 Rodar localmente

Pré-requisitos: Python 3.10+.

```bash
pip install -r requirements.txt
streamlit run app.py
```

Abre em `http://localhost:8501`.

## ☁️ Deploy no Streamlit Cloud

1. Faça push para o GitHub
2. Em [share.streamlit.io](https://share.streamlit.io), conecte o repositório
3. O `packages.txt` (incluído) instala o Tesseract OCR e o pacote de idioma português (`tesseract-ocr-por`) automaticamente — habilita a conversão de PDFs escaneados em português e inglês. Se não for necessário, o arquivo pode ser removido sem afetar PDFs com texto nativo
4. Deploy

## 📋 Estrutura

```
pdf-para-md/
├── app.py            # Aplicação principal
├── requirements.txt  # Dependências Python (streamlit, pymupdf4llm)
├── packages.txt      # Pacotes do sistema (Tesseract OCR, opcional)
└── README.md
```

## 🛠️ Tecnologias

- **Streamlit** — interface web
- **PyMuPDF4LLM** — motor de conversão PDF → Markdown (baseado no PyMuPDF/MuPDF)
- **Tesseract OCR** (opcional) — leitura de páginas escaneadas em português e inglês

## ⚖️ Licenciamento da biblioteca de conversão

O PyMuPDF4LLM (e o PyMuPDF, sua base) é distribuído sob dupla licença: **AGPL v3** ou licença comercial da Artifex. A cláusula de uso em rede da AGPL costuma se aplicar a apps rodando como serviço — o que inclui o uso embutido no AtlasDocs. Não sou advogado; vale confirmar com o jurídico se a AGPL atende ao uso pretendido ou se compensa a licença comercial.

## 🔒 Privacidade

Os arquivos são processados em diretórios temporários e removidos após a conversão. Nada é armazenado permanentemente.

---

Desenvolvido com ❤️ usando Python e Streamlit.
