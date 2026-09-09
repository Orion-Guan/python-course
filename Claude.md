# 项目架构说明

> 本文面向维护者、学习者以及 Claude 等代码助手，介绍 `Orion-Guan/python-course` 的目录组织、运行方式和模块关系。项目当前是一个**按知识主题组织的 Python 学习代码仓库**，不是一个带统一构建入口的生产应用。

## 1. 项目定位

本项目以中文目录和示例脚本为主，内容从 Python 基础逐步扩展到数据分析、网络爬虫和 AI 应用。每个章节通常是可以独立阅读、修改和运行的教学示例，`README.md` 是知识点速通笔记和索引。

项目的主要特点：

- 章节之间以学习顺序组织，而不是以 Python package 依赖组织。
- 示例以 `.py` 脚本为主，数据分析部分使用 Jupyter Notebook（`.ipynb`）。
- 没有统一的 `pyproject.toml`、`requirements.txt`、测试目录或应用启动器。
- 代码和配套数据、图片、CSV、JSON、AI 会话记录放在相应章节目录下。
- 根目录没有统一的 CLI；运行哪个示例由学习者按章节选择。

## 2. 顶层目录结构

```text
python-course/
├── README.md                         # 知识点汇总、示例代码和学习索引
├── Claude.md                         # 本架构与协作说明
├── 一、入门程序/                      # 第一个 Python 程序
├── 二、数据存储与运算/                # 基本数据类型、高级数据类型、类型注解
├── 三、流程控制语句/                  # 条件判断、for/while 循环
├── 四、函数/                          # 函数基础、高级用法和案例
├── 五、Python模块/                    # 模块、包、导入方式和自定义模块
│   └── utils/                         # 教学用 Python 包（含 __init__.py）
├── 六、面向对象编程/                  # 类、对象和教务管理系统案例
│   └── 面向对象基础/
├── 七、异常处理/                      # try/except/finally 等
├── 八、文件操作/                      # 文本、JSON、CSV 读写
│   └── resources/                     # 文件操作示例数据
├── 九、AI应用/                        # OpenAI 兼容 API、Streamlit、Ollama 聊天应用
│   ├── resources/                     # 页面素材
│   └── sessions/                      # AI 伴侣本地 JSON 会话记录
├── 十、网络爬虫/                      # XPath、排行榜和 TMDB 数据采集
│   └── movies/                        # 爬虫生成的电影 CSV 数据
├── 十一、正则表达式/                  # Python re 模块示例
└── 十二、数据分析/                    # Pandas 数据处理与 Matplotlib 可视化
    ├── Pandas数据处理/                # 数据处理 Notebook
    ├── Matplotlib数据可视化报表/      # 图表 Notebook
    └── data/                          # 分析输入数据和生成的图片/CSV
```

## 3. 分层与依赖关系

虽然仓库没有严格的软件分层，但从职责上可以划分为以下几层：

### 3.1 语言基础层

目录 `一、入门程序` 至 `七、异常处理` 构成基础教学层，涵盖：

- 字面量、变量、基本数据类型和运算符；
- `list`、`tuple`、`set`、`dict` 等高级数据类型；
- 条件分支、循环、函数、递归、lambda、参数传递；
- 模块与包的导入方式；
- 类、对象、魔术方法和简单的面向对象案例；
- 异常捕获和资源处理。

这些示例主要依赖 Python 标准库，通常不需要网络或外部服务。`五、Python模块` 中的 `custom_module.py` 和 `utils/` 是教学用本地模块，演示 `import`、`from ... import`、`__name__` 和包导入。

### 3.2 本地数据与持久化层

`八、文件操作` 展示文本文件、JSON 和 CSV 的读写；其他章节会复用类似的本地文件方式：

- `九、AI应用/sessions/*.json` 保存 AI 伴侣的会话状态；
- `十、网络爬虫/movies/*.csv` 保存爬虫结果；
- `十二、数据分析/data/` 保存分析输入和输出。

这些文件属于示例数据或运行产物，不是数据库。路径多数是相对于仓库根目录的中文相对路径，因此从其他工作目录启动脚本可能导致找不到文件。

### 3.3 外部数据采集层

`十、网络爬虫` 使用 `requests` 发起 HTTP 请求，使用 `lxml.html` 和 XPath 解析网页，并通过 `csv` 写入结果：

```text
目标网站 ──requests──> HTML 响应 ──lxml/XPath──> Python 字典/列表 ──csv──> movies/*.csv
```

主要入口：

- `1.Xpath语法.py`：XPath 基础练习；
- `2.爬取编程语言排行榜.py`：读取 TIOBE 排行榜并打印；
- `3.获取TMDB电影榜单数据.py`：分批获取电影列表和详情，清洗字段后写入 CSV。

该层依赖外部网站的 HTML 结构，网站改版、网络不可用、频率限制都可能导致示例失效。爬取前应遵守目标网站的服务条款和 robots 规则。

### 3.4 数据分析与可视化层

`十二、数据分析` 使用 Notebook 作为交互式执行单元：

```text
CSV/图片数据 ──Pandas──> DataFrame 清洗、选择、排序、分组 ──Matplotlib──> 图表/图片
```

Pandas 示例覆盖 `Series`、`DataFrame`、数据读写、查看、过滤、缺失值和重复值处理、排序、分组统计；Matplotlib 示例覆盖折线图、柱状图和饼图。分析数据主要位于 `十二、数据分析/data/`，其中部分 CSV 可由爬虫章节生成或加工得到。

### 3.5 AI 应用层

`九、AI应用` 包含三个相互独立的示例，不是一个统一的后端：

1. `1.大模型API调用.py`
   - 使用 `openai` SDK 的兼容接口；
   - 从环境变量 `DEEPSEEK_API_KEY` 读取密钥；
   - 通过 DeepSeek `base_url` 调用聊天模型；
   - 结果直接打印到终端。

2. `2.Streamlit入门.py`
   - 使用 Streamlit API 构建静态/交互式演示页面；
   - 展示标题、文本、图片、表格、输入框、单选按钮和页面配置；
   - 不负责模型调用，也不依赖 `3. AI智能伴侣.py`。

3. `3.AI智能伴侣.py`
   - Streamlit 负责页面和交互；
   - Ollama 负责本地模型聊天，当前代码中的模型名为 `ornith:9b`；
   - `st.session_state` 保存当前页面的昵称、性格、会话 ID 和消息列表；
   - `九、AI应用/sessions/` 负责 JSON 会话的保存、加载和删除；
   - 通过流式响应逐段刷新 assistant 消息。

AI 伴侣的数据流如下：

```text
Streamlit 输入
    └──> session_state.messages
          └──> system prompt + 历史消息 ──ollama.chat──> 流式响应
                                             └──> session_state
                                                   └──> sessions/<session_id>.json
```

## 4. 运行环境与依赖

建议使用 Python 3.10 或更高版本：部分示例使用 `match/case`、`list[str]` 和 `|` 类型联合语法。项目未锁定依赖版本，按所运行的章节安装对应依赖即可：

```bash
# 可选：创建并启用虚拟环境
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1

# 网络爬虫
pip install requests lxml

# 数据分析和 Notebook
pip install pandas matplotlib jupyter

# AI API 示例
pip install openai

# Streamlit 示例
pip install streamlit

# 本地 Ollama 聊天示例
pip install ollama
```

运行示例时应在仓库根目录执行，以保证代码中写死的相对路径可用：

```bash
python "六、面向对象编程/面向对象基础/2.教务管理系统案例.py"
python "十、网络爬虫/2.爬取编程语言排行榜.py"
python "十、网络爬虫/3.获取TMDB电影榜单数据.py"
streamlit run "九、AI应用/2.Streamlit入门.py"
streamlit run "九、AI应用/3.AI智能伴侣.py"
jupyter notebook
```

大模型 API 示例需要先设置密钥，禁止把密钥写入代码或提交到仓库：

```bash
export DEEPSEEK_API_KEY="your-api-key"
python "九、AI应用/1.大模型API调用.py"
```

AI 伴侣还需要本机 Ollama 服务已启动，并且已准备代码中配置的模型；Ollama 默认服务地址由其 Python 客户端处理。

## 5. 代码组织约定

- 文件名和目录名以中文为主，修改或新增文件时保持现有章节命名风格。
- 教学脚本一般在文件底部使用 `if __name__ == '__main__':` 作为可执行入口；没有入口的文件通常是演示片段，直接运行即可查看输出。
- 可复用的教学函数放在对应章节脚本或 `五、Python模块` 中，不要为了一个示例引入复杂框架。
- 爬虫、文件操作和 AI 代码应明确区分“采集/调用”“清洗/处理”“持久化/展示”职责。
- 新增外部依赖时同步更新本文的依赖说明，并优先使用虚拟环境。
- 代码中的密钥、个人隐私、真实会话内容和不必要的大型运行产物不应提交。

## 6. 修改和验证指南

这是教学仓库，目前没有自动化测试套件。修改后建议按变更范围进行轻量验证：

1. 先检查 Python 语法：
   ```bash
   python -m compileall -q .
   ```
2. 对不需要外部服务的示例直接运行，并确认输出符合预期。
3. 修改文件操作示例时，检查相对路径、编码和 `newline=''` 行为，避免覆盖已有教学数据。
4. 修改爬虫时，避免无必要的大批量请求；检查 HTTP 状态、页面字段缺失和输出 CSV 表头。
5. 修改 Streamlit/AI 示例时，确认页面能启动、会话状态可恢复，并用环境变量/本地服务配置而不是硬编码凭据。
6. 修改 Notebook 时，同时检查输入数据路径和输出图表路径。

`compileall` 会在章节目录生成 `__pycache__`；这些缓存不属于项目内容，提交前应清理或确认未被纳入 Git。

## 7. 已知边界与维护注意事项

- 仓库没有统一依赖锁定文件，实际运行环境可能因第三方库版本不同而有差异。
- 部分示例依赖网络目标站点当前 DOM 结构，XPath 不是稳定 API。
- `十、网络爬虫/3.获取TMDB电影榜单数据.py` 中的抓取脚本会产生网络请求和 CSV 写入，不应在没有确认的情况下自动执行。
- Streamlit 页面会反复执行脚本，状态必须放在 `st.session_state`；不要把只应初始化一次的状态写成普通全局变量。
- 会话文件使用时间戳命名；同一秒内创建多个会话存在命名冲突风险，若要改进应采用更稳健的 ID（例如 UUID），并同步兼容已有 JSON 文件。
- 当前 AI 示例分别使用 DeepSeek 兼容 API 和 Ollama，本地模型、远程模型、密钥和服务地址不要混为同一配置。
- 根目录 `.gitignore` 当前主要忽略 `.venv` 和 `.idea`，新增缓存、密钥文件或临时输出时应评估是否需要补充忽略规则。

## 8. 给代码助手的工作原则

- 先阅读目标章节及其相邻资源，再修改代码；不要将教学示例整体重构为大型框架。
- 保持中文路径和现有教学意图，除非用户明确要求迁移或重命名。
- 对网络、AI、文件写入类操作优先采用可配置、可失败且不泄露凭据的实现。
- 修改后报告实际验证过的命令；如果未运行外部服务或网络依赖，应明确说明。
- 新增功能应尽量放在对应章节，不要把章节之间隐式耦合起来。
