"""
一、Streamlit库
    作用： 使用Python代码快速构建简单的Web前端页面，通常用于数据科学与机器学习领域。
    使用步骤:
    1、安装streamlit库并导入到python文件中
    2、使用其提供的API方法编写前端页面
    3、streamlit run xxx.py 构建并运行web页面

"""



import streamlit as st

# 标题
st.title("您好! 关山月")  # 一级标题
st.header("二级标题")  # 二级标题
st.subheader("三级标题")  # 三级标题

# 段落
st.write(
    "老百姓穷得吃不上饭，还要被特权阶级压榨，心里早就不满了。"
    "这时候国王不但不解决问题，还想动用军队。"
    "在“自由平等”思想的鼓动下，1789年7月14日，忍无可忍的巴黎人民冲进巴士底狱，这场大火就这么烧起来了。"
)
st.write("这样讲是不是更好懂了？😊")

# 图片
st.image(
    "https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80")

# #音频
# st.audio("音频文件路径")
#
# #视频
# st.video("视频文件路径")
#
# #Logo
# st.logo("Logo文件路径")

# 表格
data = {
    "姓名": ["关悠然", "关熊大", "关熊二"],
    "性别": ["女", "男", "未知"]
}
st.table(data)

# 输入框
str1 = st.text_input("姓名:")
st.write(f"你输入的姓名为: {str1}")

# 输入框
str2 = st.text_input("密码:", type="password")
st.write(f"你输入的密码为: {str2}")

# 单选按钮
value = st.radio("性别:", ["男", "女", "未知"], index=2)
st.write(f"单选的值: {value}")

# 设计页面布局
st.set_page_config(
    page_title="Stream入门教程",   #标签页标题
    page_icon="🎃",  #标签页图标
    layout="wide",   #页面占满窗口，默认中心
    initial_sidebar_state="expanded",   #侧边栏扩展还是收缩
    menu_items={
        "Get help": "https://www.deepseek.com/",    #右侧菜单点击选项跳转到的地址
        # "About": "https://www.deepsee.org",
    }
)
