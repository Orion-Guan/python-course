"""
TMDB-TOP100电影数据统计分析
功能：读取电影数据并生成包含4个子图的可视化统计报表
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from typing import List, Tuple


def load_movie_data(file_path: str) -> pd.DataFrame:
    """
    加载电影数据CSV文件
    
    Args:
        file_path: CSV文件路径
        
    Returns:
        包含电影数据的DataFrame
    """
    df = pd.read_csv(
        file_path,
        usecols=['电影名', '年份', '上映时间', '类型', '时常', '评分', '语言'],
        dtype={'年份': 'Int64'}
    )
    return df


def process_year_data(df: pd.DataFrame) -> Tuple[List[int], List[int]]:
    """
    处理年份数据，统计每年上映的电影数量
    
    Args:
        df: 电影数据DataFrame
        
    Returns:
        (年份列表, 对应年份的电影数量列表)
    """
    # 补充年份空值
    df['年份'] = df['上映时间'].str[:4].astype(int)
    
    # 获取x轴数据
    min_year = df['年份'].min()
    max_year = df['年份'].max()
    x_year = [year for year in range(min_year, max_year + 1, 1)]
    
    # 获取y轴数据
    year_count = df.groupby('年份').size()
    year_count = [int(year_count.get(year, 0)) for year in x_year]
    
    return x_year, year_count


def process_language_data(df: pd.DataFrame) -> Tuple[List[str], List[int]]:
    """
    处理语言数据，统计不同语言电影数量
    
    Args:
        df: 电影数据DataFrame
        
    Returns:
        (语言列表, 对应语言的电影数量列表)
    """
    # 将语言列的'-'转化为'未知'
    df['语言'] = df['语言'].str.replace('-', '未知')
    
    # 统计不同语言电影数量
    language_group = df.groupby('语言')['语言'].count().sort_values(ascending=False)
    
    x_language = language_group.index.tolist()
    y_language = language_group.values.tolist()
    
    return x_language, y_language


def process_type_data(df: pd.DataFrame) -> Tuple[List[str], List[int]]:
    """
    处理类型数据，统计不同类型电影数量
    
    Args:
        df: 电影数据DataFrame
        
    Returns:
        (类型列表, 对应类型的电影数量列表)
    """
    # 统计不同类型电影数量
    type_counts = df['类型'].str.split(',').explode().value_counts()
    
    x_type = type_counts.index.tolist()
    y_type = type_counts.values.tolist()
    
    return x_type, y_type


def process_rating_data(df: pd.DataFrame, threshold_ratio: float = 0.08) -> Tuple[List[str], List[int]]:
    """
    处理评分数据，统计不同评分电影数量（将数量较少的评分合并为'其他'）
    
    Args:
        df: 电影数据DataFrame
        threshold_ratio: 合并阈值比例（默认8%）
        
    Returns:
        (评分标签列表, 对应评分的电影数量列表)
    """
    critical_count = df['评分'].value_counts()
    
    # 将各评分的电影数量低于阈值的合并为'其他'
    other_critical = critical_count[critical_count < critical_count.sum() * threshold_ratio]
    normal_critical = critical_count[critical_count >= critical_count.sum() * threshold_ratio]
    
    # 将其他评分的电影数量合并
    normal_critical['其他'] = other_critical.sum()
    
    critical_label = normal_critical.index.tolist()
    critical_value = normal_critical.values.tolist()
    
    return critical_label, critical_value


def plot_year_trend(ax: Axes, x_year: List[int], y_year: List[int]) -> None:
    """
    绘制每年上映电影数量的折线图
    
    Args:
        ax: matplotlib Axes对象
        x_year: 年份列表
        y_year: 对应年份的电影数量列表
    """
    ax.plot(x_year, y_year, color='green')
    
    # 设置x,y轴刻度
    ax.set_xticks(x_year[0::10])
    ax.set_yticks(range(0, 19, 1))
    
    # 设置x,y轴标签
    ax.set_xlabel('年份', fontsize=10)
    ax.set_ylabel('电影数量', fontsize=10)
    
    # 设置网格
    ax.grid(True, linestyle='--', alpha=0.2)
    
    # 设置子图标题
    ax.set_title('每年上映的电影数量', fontsize=12)


def plot_language_distribution(ax: Axes, x_language: List[str], y_language: List[int]) -> None:
    """
    绘制不同语言电影数量的柱状图
    
    Args:
        ax: matplotlib Axes对象
        x_language: 语言列表
        y_language: 对应语言的电影数量列表
    """
    ax.bar(x_language, y_language, color='green', width=0.5)
    
    # 设置x轴刻度参数
    ax.tick_params(axis='x', rotation=90)
    
    # 设置x,y轴标签
    ax.set_xlabel('语言', fontsize=10)
    ax.set_ylabel('电影数量', fontsize=10)
    
    # 设置网格
    ax.grid(True, linestyle='--', alpha=0.2)
    
    # 设置子图标题
    ax.set_title('不同语言电影数量', fontsize=12)


def plot_type_distribution(ax: Axes, x_type: List[str], y_type: List[int]) -> None:
    """
    绘制不同类型电影数量的柱状图
    
    Args:
        ax: matplotlib Axes对象
        x_type: 类型列表
        y_type: 对应类型的电影数量列表
    """
    ax.bar(x_type, y_type, color='green', width=0.5)
    
    # 设置x轴刻度参数
    ax.tick_params(axis='x', rotation=90)
    
    # 设置x,y轴标签
    ax.set_xlabel('类型', fontsize=10)
    ax.set_ylabel('电影数量', fontsize=10)
    
    # 设置网格
    ax.grid(True, linestyle='--', alpha=0.2)
    
    # 设置子图标题
    ax.set_title('不同类型电影数量', fontsize=12)


def plot_rating_distribution(ax: Axes, labels: List[str], values: List[int]) -> None:
    """
    绘制不同评分电影数量的饼图
    
    Args:
        ax: matplotlib Axes对象
        labels: 评分标签列表
        values: 对应评分的电影数量列表
    """
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, radius=1)
    
    # 设置图例
    ax.legend(loc='lower center', ncol=4, bbox_to_anchor=(0.5, -0.3))
    
    # 设置子图标题
    ax.set_title('不同评分电影数量', fontsize=12)


def generate_report(
    data_file: str = 'data/movies_info3.csv',
    output_file: str = 'data/TMDB-TOP100电影数据统计图表.png',
    figsize: Tuple[int, int] = (15, 8),
    dpi: int = 100,
    save_dpi: int = 300
) -> None:
    """
    生成TMDB-TOP100电影数据统计分析报表
    
    Args:
        data_file: 输入数据文件路径
        output_file: 输出图表文件路径
        figsize: 画布尺寸（宽, 高）
        dpi: 显示分辨率
        save_dpi: 保存分辨率
    """
    # 配置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']
    
    # 加载数据
    df = load_movie_data(data_file)
    
    # 创建带有4个子图的画布
    fig, ax = plt.subplots(2, 2, figsize=figsize, dpi=dpi)
    
    # 设置整个画布的标题
    fig.suptitle('TMDB-TOP100电影数据统计分析', fontsize=15, x=0.5, y=0.95)
    
    # 设置画布中各子图之间的间距
    plt.tight_layout(h_pad=8, w_pad=5, pad=4)
    
    # 获取4个子图对象
    ax1: Axes = ax[0, 0]
    ax2: Axes = ax[0, 1]
    ax3: Axes = ax[1, 0]
    ax4: Axes = ax[1, 1]
    
    # 处理各项数据
    x_year, y_year = process_year_data(df)
    x_language, y_language = process_language_data(df)
    x_type, y_type = process_type_data(df)
    critical_label, critical_value = process_rating_data(df)
    
    # 绘制4个子图
    plot_year_trend(ax1, x_year, y_year)
    plot_language_distribution(ax2, x_language, y_language)
    plot_type_distribution(ax3, x_type, y_type)
    plot_rating_distribution(ax4, critical_label, critical_value)
    
    # 保存可视化图表
    plt.savefig(output_file, dpi=save_dpi)
    
    # 显示可视化图表
    plt.show()
    
    print(f"报表已保存至: {output_file}")


if __name__ == '__main__':
    generate_report()