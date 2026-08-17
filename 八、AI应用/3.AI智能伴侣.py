# 导入streamlit 快速构建简单Web前端页面
import streamlit as st
from openai import OpenAI


# 定义AI的角色
system_role: str = "你是我的可爱贤惠善良开朗有时候又有点犯贱的农肖福女朋友,用中文与我交互."
model_name = "ornith:9b"
# 调大模型API接口发送用户输入的消息
client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',  # required but ignored
)


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

# 使用session_state来保存对话消息(里面存放字典类型的消息)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 消息框显示历史会话(解决用户输入消息后消息框历史消息被覆盖问题)
for message in st.session_state.messages:
    st.chat_message(name = message["role"]).write(message["content"])


# 定义消息输入框
prompt_user: str = st.chat_input("陪我唠唠嗑吧...")   #用户点击发送消息后，此文件会被重新执行渲染，导致之前的对话消息被覆盖掉了


# 定义消息输出框
if prompt_user:
    # 将用户消息显示到聊天界面中。
    st.chat_message(name="user").write(prompt_user)  # name="user"表示消息来自用户，name="bot"表示消息来自AI智能伴侣（控制页面消息样式）
    # 将用户消息保存到session_state中
    st.session_state.messages.append({"role": "user", "content": prompt_user})
    print(f"用户输入的消息: {prompt_user}")

    # 调用OpenAI API接口发送用户输入的消息
    chat_completion = client.chat.completions.create(
        stream=True,   # 是否流式返回响应，默认为False
        model=model_name, # 模型名称
        messages=[   # 发送的消息列表
            {
                'role': "system",   # 系统角色（后台管理员）：给AI立规矩、定人设。定义AI的底层行为逻辑，通常不参与具体问答，但优先级最高。
                'content': system_role,
            },

            # {
            #     'role': "user",     # 用户角色（用户）：用户的提问。
            #     'content': prompt_user,
            # }

            *st.session_state.messages  # 解包，将session_state中的消息列表追加到messages中
        ]
    )

    # 将AI响应回来的消息显示到聊天界面中。
    # st.chat_message(name="assistant").write(chat_completion.choices[0].message.content)

    #创建消息容器组件
    div = st.empty() # 创建一个空白容器，用于显示AI消息
    #流式输出响应AI消息
    show_msg = ""
    for data_part in chat_completion:
        if data_part.choices[0].delta.content is not None:
            show_msg += data_part.choices[0].delta.content
            div.chat_message(name="assistant").write(show_msg)   #在容器中覆盖消息框显示每个流式词元，实现视觉流式输出效果


    # 将AI响应回来的消息保存到session_state中
    st.session_state.messages.append({"role": "assistant", "content": show_msg})
    print(f"AI响应的消息: {show_msg}")
