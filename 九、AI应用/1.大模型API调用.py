"""
一、python包管理工具
pip install 包名=版本号          #下载第三方软件包
pip uninstall  包名=版本号       #卸载包
pip list                       # 列出系统已安装的软件包
pip show  包名                  #查看包详情

二、提示词工程
角色能力、核心任务需求步骤拆解、约束条件（要求）

"""

# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI  # 从openai包中导入OpenAI对象

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),   #从DEEPSEEK_API_KEY环境变量中加载大模型api_key
    base_url="https://api.deepseek.com")   # 大模型访问地址

response = client.chat.completions.create(
    model="deepseek-v4-pro",     #模型名称
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},   #发给大模型的系统提示词
        {"role": "user", "content": "Hello"},  #发给大模型的用户提示词
    ],
    stream=False,    #是否开启流式输出
    reasoning_effort="high",   #推理效果
    extra_body={"thinking": {"type": "enabled"}}
)

print(response.choices[0].message.content)   #打印输出大模型的响应消息
