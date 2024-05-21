import streamlit as st
import base64
import streamlit.components.v1 as components
from streamlit import session_state as ss
from streamlit_pdf_viewer import pdf_viewer
import streamlit_antd_components as sac

def openSourceUrl():
    st.subheader("👋🏻👋🏻优秀开源案例（截止20240522）",divider="rainbow")
    st.markdown("""

1. **Llama 3**：Meta发布的开源大语言模型，具备8B和70B参数，支持广泛的使用场景。 [GitHub](https://github.com/meta-llama/llama3)

2. **Mistral**：Mistral AI 2024年2月发布的闭源大模型，拥有32K上下文，性能卓越。 [GitHub](https://github.com/MistralAI/mistral)

3. **Vicuna**：由UC伯克利学者联手CMU、斯坦福等推出的模型，参数量13B、7B，性能相当于90%的ChatGPT。 [GitHub](https://github.com/lm-sys/FastChat)

4. **零一万物**：李开复牵头的开源大模型，参数数量为6B和34B，有基座版、微调版和量化版。 [GitHub](https://github.com/lingyiwanwu/lingyiwanwu)

5. **Qwen**：通义千问开源版本，参数数量为1.8B/7B/14B/72B，2024年3月底发布了MoE版本。 [GitHub](https://github.com/QwenLM/Qwen)

6. **DeepSeek**：幻方团队开发的开源大模型，参数数量为7B和67B，有多个版本。 [GitHub](https://github.com/fantai/DeepSeek)

7. **Chinese-Llama-2**：通过精细调整和预训练，让Llama-2模型更好地理解和生成中文文本的项目。 [GitHub](https://github.com/Chinese-Llama-2/Chinese-Llama-2)

8. **Gemma**：Google发布的开源小语言模型，参数量为2B和7B，基于Gemini技术。 [GitHub](http://ai.google.com/gemma) - 注意：这个链接不是标准的GitHub链接，可能是一个错误或过时的链接。

9. **Phi**：微软发布的大语言模型，有mini(3.8B)、small（7B）和medium（14B）三个版本。 [GitHub](https://github.com/microsoft/phi)

10. **DBRX**：Databricks Mosaic AI发布的开源大语言混合专家(MoE)模型，参数量为132B。 [GitHub](https://github.com/Databricks-MosaicAI/dbrx)

11. **Starling**：加州大学伯克利分校发布的模型，参数量7B。 [GitHub](https://github.com/ucberkeleystarling/starling)

12. **Mistral Large**：Mistral AI 2024年2月发布的闭源大模型，具体参数未公开。 [GitHub](https://github.com/MistralAI/mistral) - 注意：此项目在上文中提到为闭源，因此可能没有GitHub链接。


    """)
    sac.divider(label='这是一条分割线', icon='house', align='center', color='orange')
    