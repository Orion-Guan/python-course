"""
三、QA问答环节
3.1 接口如何直接返回后端文件给前端?
    from fastapi.responses import FileResponse
    # 定义访问首页接口路径
    @app.get("/")
    def get_index():
        return FileResponse("static/index.html")

3.2 如何只需要前端访问固定虚拟路径，服务端就可以映射对应的静态资源返回前端？
    from fastapi.staticfiles import StaticFiles
    #挂载静态资源目录(前端访问“/static/**”下的路径，系统将映射到“static”目录下，查找对应资源)
    app.mount("/static", StaticFiles(directory="static"), name="staticFiles")

"""
import json
import os
from typing import Any

# 导入fastAPI框架
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import datetime

from pydantic import BaseModel

# 创建fastapi应用实例
app = FastAPI(title="AI猜字谜", version="1.0")

#挂载静态资源目录(前端访问“/static/**”下的路径，系统将映射到“static”目录下，查找对应资源)
app.mount("/static", StaticFiles(directory="static"), name="staticFiles")


# 定义返回结果类
class Result(BaseModel):
    code: int
    message: str
    data: Any

# 定义创建会话接口
def generate_session_id()->str:
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")



# 定义访问首页接口路径
@app.get("/")
def get_index():
    return FileResponse("static/index.html")



@app.post("/api/sessions")
def create_session()->Result:
    """
    新建会话接口
    :return: Result(code=200, message="创建会话成功", data=会话id)---->自动将对象序列化为json格式
    """
    # 生成会话id
    session_id = generate_session_id()

    #组装会话信息并保存到文件
    session_info = {
        "session_id": session_id,
        "messages": []
    }

    # 检查会话目录是否存在，若不存在则创建
    if not os.path.exists("sessions"):
        os.mkdir("sessions")

    # 保存会话信息到文件
    with open(f"sessions/{session_id}.json", "w", encoding="utf-8") as f:
        json.dump(session_info, f, ensure_ascii=False, indent=4)

    #返回会话id
    return Result(code=200, message="创建会话成功", data=session_id)



# 测试启动服务
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
