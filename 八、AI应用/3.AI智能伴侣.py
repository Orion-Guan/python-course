# 导入streamlit 快速构建简单Web前端页面
import streamlit as st
from openai import OpenAI

# 定义AI的角色
role: str = "你是我的可爱贤惠善良开朗有时候又有点犯贱的Leisr女朋友"
model_name = "gpt-oss:20b"

# 对页面布局进行设置
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
    }
)

# 设置页面标题
st.title("AI智能伴侣")

# 定义消息输入框
prompt: str = st.chat_input("陪我唠唠嗑吧...")

# 定义消息输出框
if prompt:
    # 将用户消息显示到聊天界面中。
    st.chat_message(name="user").write(prompt)  # name="user"表示消息来自用户，name="bot"表示消息来自AI智能伴侣（控制页面消息样式）
    print(f"用户输入的消息: {prompt}")

    # 调大模型API接口发送用户输入的消息
    client = OpenAI(
        base_url='http://localhost:11434/v1/',
        api_key='ollama',  # required but ignored
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                'role': role,
                'content': prompt,
            }
        ],
        model = model_name,
    )
    print(f"AI响应回来的消息: {chat_completion.choices[0].message.content}")

    #将AI响应回来的消息显示到聊天界面中。
    st.chat_message(name="bot").write(chat_completion.choices[0].message.content)