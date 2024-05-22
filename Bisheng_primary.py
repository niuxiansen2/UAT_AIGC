import streamlit_antd_components as sac
import streamlit as st

import base64

def fileshow():# st.set_page_config(page_title="bisheng快速入门", page_icon="📑", layout="wide")


    # 本地PDF文件路径
    file_path = "./fileSource/基本操作步骤.pdf"

    # 读取本地PDF文件为二进制数据
    with open(file_path, "rb") as file:
        pdf_data = file.read()

    # 将PDF文件转换为base64编码
    base64_pdf = base64.b64encode(pdf_data).decode('utf-8')

    # 使用HTML展示PDF文件
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1200" height="2000" type="application/pdf"></iframe>'

    # 在Streamlit页面中展示PDF文件
    st.markdown(pdf_display, unsafe_allow_html=True)
def primaryLearning():
    with st.container():
        st.header("⌨️基本操作入门",divider="rainbow")
        # fileshow()
        # st.divider()
        # st.divider()

        import streamlit.components.v1 as components
        components.iframe("https://blog.csdn.net/weixin_41165446/article/details/139114907", width=1200,
                          height=2000, scrolling=True)

