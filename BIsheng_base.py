import streamlit as st
import base64
import streamlit.components.v1 as components
from streamlit import session_state as ss
from streamlit_pdf_viewer import pdf_viewer


def display_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" ' \
                      f'type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)


def base2():
    # Declare variable.
    if 'pdf_ref' not in ss:
        ss.pdf_ref = None

    # Access the uploaded ref via a key.
    st.file_uploader("Upload PDF file", type='pdf', key='pdf')

    if ss.pdf:
        ss.pdf_ref = ss.pdf  # backup

    # Now you can access "pdf_ref" anywhere in your app.
    if ss.pdf_ref:
        binary_data = ss.pdf_ref.getvalue()
        pdf_viewer(input=binary_data, width=1200)


def baseKnowledge():
    import streamlit as st
    import base64

    # 标题
    st.header("Bisheng基本介绍",divider="rainbow")

    # 本地PDF文件路径
    file_path = "./fileSource/基本介绍.pdf"

    # 读取本地PDF文件为二进制数据
    with open(file_path, "rb") as file:
        pdf_data = file.read()

    # 将PDF文件转换为base64编码
    base64_pdf = base64.b64encode(pdf_data).decode('utf-8')

    # 使用HTML展示PDF文件
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1200" height="2000" type="application/pdf"></iframe>'

    # 在Streamlit页面中展示PDF文件
    st.markdown(pdf_display, unsafe_allow_html=True)


