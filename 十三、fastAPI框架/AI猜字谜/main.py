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


# 导入fastAPI框架
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# 创建fastapi应用实例
app = FastAPI(title="AI猜字谜", version="1.0")

#挂载静态资源目录(前端访问“/static/**”下的路径，系统将映射到“static”目录下，查找对应资源)
app.mount("/static", StaticFiles(directory="static"), name="staticFiles")

# 定义访问首页接口路径
@app.get("/")
def get_index():
    return FileResponse("static/index.html")

# 测试启动服务
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
