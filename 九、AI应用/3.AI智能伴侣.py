# 导入streamlit 快速构建简单Web前端页面
import datetime
import os.path
import json

import streamlit as st
import ollama

# 对页面布局进行设置
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
    }
)
# 设置页面logo
st.logo(image="💖")

# 设置页面标题
st.title("AI智能伴侣")

# 使用session_state来保存对话消息(里面存放字典类型的消息)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 存放用户个人信息到session_state中
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "农肖福"
if "nature" not in st.session_state:
    st.session_state.nature = "阳光开朗大大咧咧，有时候稍微有点俏皮的南方姑娘"

# 页面初次加载创建当前会话标识
if "session_current" not in st.session_state:
    st.session_state.session_current = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def save_session():
    """
    保存当前会话信息到本地文件
    :return:
    """
    if st.session_state.session_current:
        session_data = {
            "session_id": st.session_state.session_current,
            "nick_name": st.session_state.nick_name,
            "nature": st.session_state.nature,
            "messages": st.session_state.messages
        }
        # 将当前会话信息序列化到本地文件
        if not os.path.exists("九、AI应用/sessions"):
            os.mkdir("九、AI应用/sessions")
        with open(f"九、AI应用/sessions/{st.session_state.session_current}.json", mode="w", encoding="utf-8") as file:
            json.dump(session_data, file, ensure_ascii=False, indent=2)
    pass


def session_list() -> list[str]:
    """
    获取本地保存的会话列表
    :return:
    """
    session_list = []
    if os.path.exists("九、AI应用/sessions"):
        for fileName_list in os.listdir("九、AI应用/sessions"):
            if fileName_list.endswith(".json"):
                session_list.append(fileName_list[:-5])
    return session_list


def load_session(session_cur: str) -> None:
    """
    加载当前会话信息
    :return:
    """
    if os.path.exists(f"九、AI应用/sessions/{session_cur}.json"):
        # 用户点击历史会话加载失败给出提示
        try:
            with open(f"九、AI应用/sessions/{session_cur}.json", mode="r", encoding="utf-8") as file:
                session_data = json.load(file)
                st.session_state.session_current = session_data["session_id"]
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.nature = session_data["nature"]
                st.session_state.messages = session_data["messages"]
        except Exception as e:
            st.error(f"加载会话失败")


def delete_session(session_id: str):
    """
    删除指定会话
    :param session_id:
    :return:
    """
    try:
        if os.path.exists(f"九、AI应用/sessions/{session_id}.json"):
            os.remove(f"九、AI应用/sessions/{session_id}.json")
            if st.session_state.session_current == session_id:  # 如果当前会话是被删除的会话，则清空当前会话信息,并创建新会话
                st.session_state.session_current = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                st.session_state.messages.clear()
    except Exception as e:
        st.error(f"删除会话失败")


# 显示侧边栏，with是streamlit的上下文管理器，用于控制流式输出
with st.sidebar:
    st.subheader("最佳灵魂伴侣")
    if st.button("新建会话", icon="📝", width="stretch") and st.session_state.messages:
        # 保存当前会话上下文
        save_session()
        # 创建并保存新会话
        st.session_state.messages.clear()
        st.session_state.session_current = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        save_session()
        st.rerun()  # 重新执行当前页面，刷新页面

    # 显示历史会话
    st.text("历史会话")
    # 获取历史会话标识列表
    history_sessions = session_list()
    if len(history_sessions) > 0:
        col1, col2 = st.columns([4, 1])  # 创建两列布局
        # 显示历史会话按钮
        for session_sign in reversed(history_sessions):
            with col1:
                if st.button(session_sign, icon="🔉", width="stretch", key=f"{session_sign}_load",
                             type="primary" if session_sign == st.session_state.session_current else "secondary"):
                    # 读取加载当前点击的历史会话信息
                    load_session(session_sign)
                    st.rerun()  # 重新执行当前页面

            with col2:
                if st.button("", icon="❌", width="stretch", key=f"{session_sign}_delete"):
                    # 删除指定会话
                    delete_session(session_sign)
                    st.rerun()  # 重新执行渲染当前页面
                    pass
    #加个分分割线
    st.divider()
    nick_name = st.text_input("昵称:", placeholder="请输入你的昵称", value=st.session_state.nick_name)
    nature = st.text_area("描述:", placeholder="你的个性描述", value=st.session_state.nature)
    st.session_state.nick_name = nick_name
    st.session_state.nature = nature

# 定义AI的角色
system_content: str = f"""
                        你叫{st.session_state.nick_name}，现在是用户的真实伴侣，请完全代入伴侣角色。规则：
                        1. 每次只回1条消息
                        2. 禁止任何场景或状态描述性文字
                        3.匹配用户的语言
                        4. 复简短，像微信聊天一样
                        5.有需要的话可以用❤☆等emoji表情
                        6. 用符合伴侣性格的方式对话
                        7. 回复的内容，要充分体现伴侣的性格特征
                        伴侣性格：
                        {st.session_state.nature}
                        你必须严格遵守上述规则来回复用户。
                        """

model_name = "ornith:9b"

# 设置当前会话页面
st.text("当前会话ID: %s" % st.session_state.session_current)

# 消息框显示历史会话(解决用户输入消息后消息框历史消息被覆盖问题)
for message in st.session_state.messages:
    st.chat_message(name=message["role"]).write(message["content"])

# 定义消息输入框
prompt_user: str = st.chat_input("陪我唠唠嗑吧...")  # 用户点击发送消息后，此文件会被重新执行渲染，导致之前的对话消息被覆盖掉了

# 定义消息输出框
if prompt_user:
    # 将用户消息显示到聊天界面中。
    st.chat_message(name="user").write(prompt_user)  # name="user"表示消息来自用户，name="bot"表示消息来自AI智能伴侣（控制页面消息样式）
    # 将用户消息保存到session_state中
    st.session_state.messages.append({"role": "user", "content": prompt_user})
    print(f"用户输入的消息: {prompt_user}")

    chat_completion = ollama.chat(
        model=model_name,
        messages=[
            {"role": "system", "content": system_content},
            *st.session_state.messages
        ],
        stream=True,
        options={
            "keep_alive": 60,  # 保活机制： LLM每次请求结束都会卸载模型，此配置是告诉LLM 等待60s若无新请求则从显存或内存中释放资源。
            "max_tokens": 888,  # 最大输出tokens数量: 限制大模型最大响应的token上限
            "num_thread": 8,  # 线程数： 设置LLM的并行计算线程数
            "num_ctx": 4096,  # 上下文数量： 设置LLM的上下文数量
        }
    )

    # 创建消息容器组件
    div = st.empty()  # 创建一个空白容器，用于显示AI消息
    # 流式输出响应AI消息
    show_msg = ""
    for chunk in chat_completion:
        if chunk.message.content is not None:
            show_msg += chunk.message.content
            div.chat_message(name="assistant").write(show_msg)  # 在容器中覆盖消息框显示每个流式词元，实现视觉流式输出效果

    # 将AI响应回来的消息保存到session_state中
    st.session_state.messages.append({"role": "assistant", "content": show_msg})
    save_session()  # 将AI响应回来的数据保存到本地文件中
    print(f"AI响应的消息: {show_msg}")
