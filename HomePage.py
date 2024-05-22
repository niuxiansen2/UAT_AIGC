import streamlit_antd_components as sac
import streamlit as st
from Bisheng_primary import *
from BIsheng_base import *
from openSource import *
from webLearning import *
from AIGC_Set import *
from TypicalCase import *
from api_file import *
from meetingLearning import *

st.set_page_config(page_title="UAT AIGC社区", page_icon="👽", layout="wide")

with st.sidebar:
    st.image("imgSource/logo.png", use_column_width=True)
    sac.menu([
        sac.MenuItem('主页', icon='house-fill', ),
        # sac.MenuItem('业务运营智能审批要件', icon='box-fill'),
        sac.MenuItem("bisheng平台学习", icon='robot', children=[
            sac.MenuItem('基本介绍'),
            sac.MenuItem('快速入门'),
            sac.MenuItem('典型案例', children=[
                sac.MenuItem('角色对话'),
                sac.MenuItem('文件对话'),
                sac.MenuItem('文本分析Agent构建'),
            ]),
            sac.MenuItem('接口文档'),
        ]),
        sac.MenuItem('AIGC应用合集', icon='git', ),
        sac.MenuItem("峰会学习", icon='google', children=[
            sac.MenuItem('人工智能'),
            sac.MenuItem('测试领域'),
            sac.MenuItem('其他')
        ]),
        sac.MenuItem('优秀开源案例', icon='gitlab'),
        sac.MenuItem('UI设计-Streamlit学习', icon='robot')]
        , key="menu", size=18, open_index=[1])

if st.session_state["menu"] == "主页":
    st.header("📂AIGC常用知识汇总", divider="rainbow")
    with st.container(height=900):
        col = st.columns(3)
        with col[1]:
            st.subheader("大模型基础知识")
        st.markdown(
            """
            **基础**：
    - 【ChatGPT提示工程师&AI大神吴恩达教你写提示词｜prompt engineering【完整中字九集全】-哔哩哔哩】 https://b23.tv/yBqBnA1
    -  吴恩达最新《LLM应用程序开发的LangChain》1_LangChain_Intro_v02.zh_gpt_subtitled_哔哩哔哩_bilibili
    - 【合集·LangChain in Action-哔哩哔哩】 https://space.bilibili.com/28357052/channel/collectiondetail?sid=1611560
    - 《解读 ChatGPT 背后的技术重点：RLHF、IFT、CoT、红蓝对抗》https://blog.csdn.net/HuggingFace/article/details/128843029


    **推荐文章：**
    - 《LangChain：Model as a Service粘合剂，被ChatGPT插件干掉了吗？》https://mp.weixin.qq.com/s/3coFhAdzr40tozn8f9Dc-w
    - 《AI Agent的千亿美金问题：如何重构10亿知识工作职业，掀起软件生产革命？》https://mp.weixin.qq.com/s/JYu_oXWbWbasT1fcBRo-cA
    - 《GitHub首席工程师：别再逼着用户跟AI聊天了！》https://mp.weixin.qq.com/s/wm__hW1rQSbZEBQchx-q4g
    - 《万字长文带你深入了解向量数据库》https://mp.weixin.qq.com/s/6IPMIYch3rA7DEJKm9xUmg
    - 投身LLM的道路https://mp.weixin.qq.com/s/vfsB5t3r5dBACKQx6FshVw
      - 向下走：去搞基模型预训练、部署、或者去做大模型基建；
      - 向上走：去做对齐工作，做 Agents，做应用；
      - 艰难之路：去搞大模型理论研究，可解释性，短期基本看不到回报，但这块成果对前两个都会有帮助。
    - 【注意，“人工智障”系列是大模型时代之前的文章，但问题值得持续思考】
      - 《为什么现在的人工智能助理都像人工智障？》https://mp.weixin.qq.com/s/_jyBZtp_43vTgtjcHsSlHQ
      - 《人工智障 2 : 你看到的AI与智能无关》https://mp.weixin.qq.com/s/KF4DgF9FPYW2D_M-uacNaw


    **进阶：**
    - 《Large Language Model in Action》https://wangwei1237.github.io/LLM_in_Action/
    - 【langchain官方文档】https://python.langchain.com/docs/get_started/introduction
    - 【OpenAI官方文档】https://cookbook.openai.com/
    - 《Building LLM applications for production》https://huyenchip.com/2023/04/11/llm-engineering.html
    - 《LLM Powered Autonomous Agents》https://lilianweng.github.io/posts/2023-06-23-agent/
            """
        )

if st.session_state["menu"] == "基本介绍":#使用markdown
    baseKnowledge2()
    # base2()

if st.session_state["menu"] == "快速入门":
    primaryLearning()

if st.session_state["menu"] == "优秀开源案例":
    openSourceUrl()

if st.session_state["menu"] == "AIGC应用合集":
    AIGC_SET()



if st.session_state["menu"] == "UI设计-Streamlit学习":
    main()

if st.session_state["menu"] == "角色对话":
    case_base_talk()
if st.session_state["menu"] == "文件对话":
    case_file_talk()
if st.session_state["menu"] == "文本分析Agent构建":
    case_analyze_agent()
if st.session_state["menu"] == "接口文档":
    apiShow()
if st.session_state["menu"] == "人工智能":
    meetingFile_AI()