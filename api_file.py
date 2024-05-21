def apiShow():
    import streamlit as st
    import base64

    # 标题
    st.header("🔗API文档", divider="rainbow")

    # 本地PDF文件路径
    file_path = "./fileSource/接口文档.pdf"

    # 读取本地PDF文件为二进制数据
    with open(file_path, "rb") as file:
        pdf_data = file.read()

    # 将PDF文件转换为base64编码
    base64_pdf = base64.b64encode(pdf_data).decode('utf-8')

    # 使用HTML展示PDF文件
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1200" height="2000" type="application/pdf"></iframe>'

    # 在Streamlit页面中展示PDF文件
    st.markdown(pdf_display, unsafe_allow_html=True)