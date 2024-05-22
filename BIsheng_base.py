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


def baseKnowledge2():
    st.header("Bisheng平台简介", divider="rainbow")
    st.markdown("""

##### BISHENG毕昇 是一款 **:red[开源的]** LLM应用开发平台。 

## **1.1 BISHENG特点**

•     **便捷**：即使是业务人员，基于我们预置的毕昇助手与技能模板，通过简单直观的表单填写方式快速搭建以大模型为核心的智能应用。

•     **灵活**：对大模型技术有了解的人员，我们紧跟最前沿大模型技术生态提供数百种开发组件，基于可视化且自由的流程编排能力，可开发出丰富的大模型应用（智能问答、报告生成、自动化、数据分析等）。

•     **可靠与企业级**：当前许多同类的开源项目仅适用于实验测试场景，缺少真正生产使用的企业级特性，包括：高并发下的高可用、应用运营及效果持续迭代优化、贴合真实业务场景的实用功能等，这些都是毕昇平台的差异化能力；另外，更直观的是，企业内的数据质量参差不齐，想要真正把所有数据利用起来，首先需要有完备的非结构化数据治理能力，而这是**过去几年我们团队所积累的核心能力**，这部分我们也完全免费提供了出来。

    """)
    st.image("fileSource/基本操作_img/clip_image003.jpg")

    st.markdown("""
    ## **1.2 开源**

⭐️ BISHENG于2023年8月底正式基于**Apache 2.0****协议开源（无任何附加协议），可二开商用**，Github地址：https://github.com/dataelement/bisheng

    """)

    st.image("fileSource/基本操作_img/clip_image005.jpg", use_column_width=True)

    st.markdown("""
    ## **1.3 Demo地址**

⭐️ **Demo****环境地址：**https://bisheng.dataelem.com/

  直接注册账号即可进行试用，demo环境仅用于功能体验  

  # **应用场景**

视频演示

•     [BISHENG：开源的企业级LLMOps ，满足大模型企业落地的所有想象~_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Xw4116774/?vd_source=9a977bfbc02ca26ec2125a00d8a4558b)

•     [What？大模型可以生成靠谱专业报告了？_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Hi4y1v7aL/?spm_id_from=333.999.0.0&vd_source=9a977bfbc02ca26ec2125a00d8a4558b)

•     [硬核更新！！在BISHENG平台让AI打辩论~ BISHENG集成AutoGen！！快来一起玩花活~_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV11b4y1M7EF/?spm_id_from=333.999.0.0&vd_source=9a977bfbc02ca26ec2125a00d8a4558b)

•     [还是挺厉害的！复制接口文档，让大模型帮我调接口，而且用国内模型也能实现_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV16M411o7gh/?spm_id_from=333.999.0.0&vd_source=9a977bfbc02ca26ec2125a00d8a4558b)

使用毕昇平台，我们可以搭建各类丰富的大模型应用：

    """)
    st.image("fileSource/基本操作_img/use.png", use_column_width=True)
    st.markdown("""

# **常用资源链接**

| 链接                                                         | 说明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [BISHENG Blog](https://dataelem.feishu.cn/wiki/BiNowcaYWilewdksXQ5cZl3tnzy) | 企业大模型应用落地思考、产品设计思考、PPT讲解等              |
| [全量功能列表](https://dataelem.feishu.cn/wiki/KO8kws0QuifwgSk8r8rcODOvnLf) |                                                              |
| [私有化部署](https://dataelem.feishu.cn/wiki/BSCcwKd4Yiot3IkOEC8cxGW7nPc) | 平台私有化部署方法。                                         |
| [技能构建指南](https://dataelem.feishu.cn/wiki/JL4AwM7NuipbAkk3RdNc00eunSg) | 关于BISHENG构建技能时，高级配置中各个常用组件的使用说明。    |
| [应用案例](https://dataelem.feishu.cn/wiki/ZfkmwLPfeiAhQSkK2WvcX87unxc) | 常见应用场景的构建方法教学。                                 |
| [经验技巧](https://dataelem.feishu.cn/wiki/OWFRwknFaiIMajke4m5cFeLrnie) | 具体场景落地过程中，一些实用的效果优化经验技巧。             |
| [技能市场](https://dataelem.feishu.cn/wiki/Jad2wGHGWiNOaFkYwMOcYwnpnXe) | BISHENG官方提供的各类丰富实用技能模板，下载后导入平台填写APIKEY等信息即可使用。 |
| [ProxyChatLLM](https://dataelem.feishu.cn/wiki/A65GwSXT6iscfikI0alcbgxAndf) | 直接在BISHENG使用各主流厂商大模型服务的方法。                |
| [问题排查手册 ](https://dataelem.feishu.cn/wiki/JvyJwh0priBOIrkhJF5cLeVMnvg) | 出现常见问题排查与解决方法。                                 |
| [开发者指南](https://dataelem.feishu.cn/wiki/ITmJwMXVliBnzpkW3nkcqPVrnse) | BISHENG各个模块的技术说明，以及代码PR方法说明。              |
| [FAQ](https://dataelem.feishu.cn/wiki/XdGCwkDJviC0Z8klbdbcF790n9b) | 关于BISHENG的常见问题。          
    """)


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


