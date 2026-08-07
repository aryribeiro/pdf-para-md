import streamlit as st
import tempfile
from pathlib import Path
import pymupdf4llm

# ---------------------------------------------------------------------------
# CONFIGURAÇÃO DE PÁGINA E CSS (compacto, para caber no lightbox do AtlasDocs)
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Conversor de PDF para Markdown",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    .main {
        background-color: #ffffff;
        color: #333333;
    }
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        max-width: 28rem !important;
    }
    header {display: none !important;}
    footer {display: none !important;}
    #MainMenu {display: none !important;}
    div[data-testid="stAppViewBlockContainer"] {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
    div[data-testid="stVerticalBlock"] {
        gap: 0 !important;
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
    .element-container {
        margin-top: 0 !important;
        margin-bottom: 0 !important;
    }
    .stDownloadButton button {
        width: 100% !important;
        padding: 0.6rem 2rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# CONVERSÃO: PDF -> Markdown
# ---------------------------------------------------------------------------
MD_MIME = "text/markdown"


def convert_pdf_to_markdown(input_path, output_dir):
    """Converte um PDF em Markdown (.md) usando PyMuPDF4LLM.

    PyMuPDF4LLM reconstrói títulos (a partir do tamanho da fonte), negrito/
    itálico, listas e tabelas em Markdown, e aciona OCR automaticamente em
    páginas escaneadas quando o Tesseract está disponível no sistema.
    """
    try:
        md_text = pymupdf4llm.to_markdown(str(input_path))
    except Exception as e:
        st.error(f"❌ Erro ao converter: {str(e)}")
        return None

    output_path = Path(output_dir) / (Path(input_path).stem + ".md")
    output_path.write_text(md_text, encoding="utf-8")

    if output_path.exists() and output_path.stat().st_size > 0:
        return str(output_path)

    st.error("❌ Não foi possível extrair texto deste PDF.")
    return None

# ---------------------------------------------------------------------------
# INTERFACE PRINCIPAL
# ---------------------------------------------------------------------------
def main():
    uploaded_file = st.file_uploader(
        "Arraste e solte seu arquivo aqui",
        type=["pdf"],
        help="Arquivo PDF. Máximo: 200MB",
        label_visibility="collapsed",
    )

    if uploaded_file is None:
        return

    if (uploaded_file.size / (1024 * 1024)) > 200:
        st.error("❌ Arquivo muito grande! Máximo: 200MB")
        st.stop()

    if Path(uploaded_file.name).suffix.lower() != ".pdf":
        st.error("❌ Formato não suportado. Envie um arquivo PDF.")
        return

    with st.spinner("Convertendo para MD..."):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_path = Path(temp_dir) / uploaded_file.name
            input_path.write_bytes(uploaded_file.getbuffer())

            output_path = convert_pdf_to_markdown(str(input_path), temp_dir)
            if output_path is None:
                return

            output_bytes = Path(output_path).read_bytes()

    st.success("✅ Conversão concluída!")
    st.download_button(
        label="📥 Baixar MD",
        data=output_bytes,
        file_name=Path(uploaded_file.name).stem + ".md",
        mime=MD_MIME,
        type="primary",
        use_container_width=True,
    )


if __name__ == "__main__":
    main()
