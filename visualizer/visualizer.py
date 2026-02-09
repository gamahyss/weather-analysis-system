import pandas
from matplotlib import pyplot

def visualize_daily_data(df: pandas.DataFrame):
    fig, axes = pyplot.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Погодные данные за день', fontsize=16, fontweight='bold')
    
    if 'temperature_2m_max' in df.columns and 'temperature_2m_min' in df.columns:
        ax1 = axes[0, 0]
        ax1.bar(['Макс. темп.', 'Мин. темп.'], 
                [df['temperature_2m_max'].iloc[0], df['temperature_2m_min'].iloc[0]],
                color=['#ff6b6b', '#4ecdc4'])
        ax1.set_ylabel('Температура (°C)')
        ax1.set_title('Температура')
        ax1.grid(axis='y', alpha=0.3)
    
    if 'precipitation_sum' in df.columns:
        ax2 = axes[0, 1]
        ax2.bar(['Осадки'], [df['precipitation_sum'].iloc[0]], color='#3498db')
        ax2.set_ylabel('Осадки (мм)')
        ax2.set_title('Осадки')
        ax2.grid(axis='y', alpha=0.3)
    
    if 'wind_speed_10m_max' in df.columns:
        ax3 = axes[1, 0]
        ax3.bar(['Макс. скорость ветра'], [df['wind_speed_10m_max'].iloc[0]], color='#9b59b6')
        ax3.set_ylabel('Скорость ветра (км/ч)')
        ax3.set_title('Скорость ветра')
        ax3.grid(axis='y', alpha=0.3)
    
    ax4 = axes[1, 1]
    ax4.axis('off')
    info_text = "Сводка за день:\n\n"
    if 'temperature_2m_max' in df.columns:
        info_text += f"Макс. температура: {df['temperature_2m_max'].iloc[0]:.1f}°C\n"
    if 'temperature_2m_min' in df.columns:
        info_text += f"Мин. температура: {df['temperature_2m_min'].iloc[0]:.1f}°C\n"
    if 'precipitation_sum' in df.columns:
        info_text += f"Осадки: {df['precipitation_sum'].iloc[0]:.1f} мм\n"
    if 'wind_speed_10m_max' in df.columns:
        info_text += f"Макс. скорость ветра: {df['wind_speed_10m_max'].iloc[0]:.1f} км/ч"
    ax4.text(0.1, 0.5, info_text, fontsize=12, verticalalignment='center',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    pyplot.tight_layout()
    pyplot.show()

def visualize_monthly_data(daily_temp_max: pandas.DataFrame, 
                          daily_temp_min: pandas.DataFrame,
                          daily_prec: pandas.DataFrame,
                          daily_wind_speed: pandas.DataFrame,
                          average_values: pandas.DataFrame,
                          max_values: pandas.DataFrame,
                          min_values: pandas.DataFrame):

    fig = pyplot.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    
    fig.suptitle('Погодные данные за месяц', fontsize=16, fontweight='bold')
    
    ax1 = fig.add_subplot(gs[0, :])
    days = range(1, len(daily_temp_max) + 1)
    ax1.plot(days, daily_temp_max['max_temp'], 'o-', color='#ff6b6b', label='Макс. температура', linewidth=2)
    ax1.plot(days, daily_temp_min['min_temp'], 'o-', color='#4ecdc4', label='Мин. температура', linewidth=2)
    ax1.fill_between(days, daily_temp_max['max_temp'], daily_temp_min['min_temp'], 
                     alpha=0.3, color='#95e1d3')
    ax1.set_xlabel('День месяца')
    ax1.set_ylabel('Температура (°C)')
    ax1.set_title('Температура по дням')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    ax2 = fig.add_subplot(gs[1, 0])
    ax2.bar(days, daily_prec['prec'], color='#3498db', alpha=0.7)
    ax2.set_xlabel('День месяца')
    ax2.set_ylabel('Осадки (мм)')
    ax2.set_title('Осадки по дням')
    ax2.grid(axis='y', alpha=0.3)
    
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.plot(days, daily_wind_speed['wind_speed'], 'o-', color='#9b59b6', linewidth=2)
    ax3.set_xlabel('День месяца')
    ax3.set_ylabel('Скорость ветра (км/ч)')
    ax3.set_title('Скорость ветра по дням')
    ax3.grid(True, alpha=0.3)
    
    ax4 = fig.add_subplot(gs[1, 2])
    ax4.axis('off')
    stats_text = "Статистика за месяц:\n\n"
    stats_text += "Средние значения:\n"
    stats_text += f"  Температура макс.: {average_values['avrg_temp_max'].iloc[0]:.1f}°C\n"
    stats_text += f"  Температура мин.: {average_values['avrg_temp_min'].iloc[0]:.1f}°C\n"
    stats_text += f"  Осадки: {average_values['avrg_prec'].iloc[0]:.1f} мм\n"
    stats_text += f"  Скорость ветра: {average_values['avrg_wind_speed'].iloc[0]:.1f} км/ч\n\n"
    stats_text += "Максимальные значения:\n"
    stats_text += f"  Температура: {max_values['max_temp'].iloc[0]:.1f}°C\n"
    stats_text += f"  Осадки: {max_values['max_prec'].iloc[0]:.1f} мм\n"
    stats_text += f"  Скорость ветра: {max_values['max_wind_speed'].iloc[0]:.1f} км/ч\n\n"
    stats_text += "Минимальные значения:\n"
    stats_text += f"  Температура: {min_values['min_temp'].iloc[0]:.1f}°C\n"
    stats_text += f"  Осадки: {min_values['min_prec'].iloc[0]:.1f} мм\n"
    stats_text += f"  Скорость ветра: {min_values['min_wind_speed'].iloc[0]:.1f} км/ч"
    ax4.text(0.1, 0.5, stats_text, fontsize=10, verticalalignment='center',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    ax5 = fig.add_subplot(gs[2, :])
    categories = ['Темп. макс.', 'Темп. мин.', 'Осадки', 'Ветер']
    avg_values = [
        average_values['avrg_temp_max'].iloc[0],
        average_values['avrg_temp_min'].iloc[0],
        average_values['avrg_prec'].iloc[0],
        average_values['avrg_wind_speed'].iloc[0]
    ]
    colors = ['#ff6b6b', '#4ecdc4', '#3498db', '#9b59b6']
    bars = ax5.bar(categories, avg_values, color=colors, alpha=0.7)
    ax5.set_ylabel('Значения')
    ax5.set_title('Средние значения параметров за месяц')
    ax5.grid(axis='y', alpha=0.3)
    
    for bar, val in zip(bars, avg_values):
        height = bar.get_height()
        ax5.text(bar.get_x() + bar.get_width()/2., height,
                f'{val:.1f}',
                ha='center', va='bottom')
    
    pyplot.show()

def visualize_yearly_data(monthly_values: pandas.DataFrame,
                         average_values: pandas.DataFrame,
                         max_values: pandas.DataFrame,
                         min_values: pandas.DataFrame):
    """
    Визуализирует данные о погоде за год.
    
    Args:
        monthly_values: DataFrame со средними значениями по месяцам (12 строк)
        average_values: DataFrame со средними значениями за год
        max_values: DataFrame с максимальными значениями за год
        min_values: DataFrame с минимальными значениями за год
    """
    fig = pyplot.figure(figsize=(16, 12))
    gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)
    
    fig.suptitle('Погодные данные за год', fontsize=16, fontweight='bold')
    
    months = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн',
              'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']
    
    ax1 = fig.add_subplot(gs[0, :])
    ax1.plot(months, monthly_values['temp_max'], 'o-', color='#ff6b6b', 
             label='Средняя макс. температура', linewidth=2, markersize=8)
    ax1.plot(months, monthly_values['temp_min'], 'o-', color='#4ecdc4', 
             label='Средняя мин. температура', linewidth=2, markersize=8)
    ax1.fill_between(months, monthly_values['temp_max'], monthly_values['temp_min'], 
                     alpha=0.3, color='#95e1d3')
    ax1.set_xlabel('Месяц')
    ax1.set_ylabel('Температура (°C)')
    ax1.set_title('Средняя температура по месяцам')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.tick_params(axis='x', rotation=45)
    
    ax2 = fig.add_subplot(gs[1, 0])
    ax2.bar(months, monthly_values['prec'], color='#3498db', alpha=0.7)
    ax2.set_xlabel('Месяц')
    ax2.set_ylabel('Осадки (мм)')
    ax2.set_title('Средние осадки по месяцам')
    ax2.grid(axis='y', alpha=0.3)
    ax2.tick_params(axis='x', rotation=45)
    
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.plot(months, monthly_values['wind_speed'], 'o-', color='#9b59b6', 
             linewidth=2, markersize=8)
    ax3.set_xlabel('Месяц')
    ax3.set_ylabel('Скорость ветра (км/ч)')
    ax3.set_title('Средняя скорость ветра по месяцам')
    ax3.grid(True, alpha=0.3)
    ax3.tick_params(axis='x', rotation=45)
    
    ax4 = fig.add_subplot(gs[2, 0])
    ax4.axis('off')
    stats_text = "Статистика за год:\n\n"
    stats_text += "Средние значения:\n"
    stats_text += f"  Температура макс.: {average_values['avrg_temp_max'].iloc[0]:.1f}°C\n"
    stats_text += f"  Температура мин.: {average_values['avrg_temp_min'].iloc[0]:.1f}°C\n"
    stats_text += f"  Осадки: {average_values['avrg_prec'].iloc[0]:.1f} мм\n"
    stats_text += f"  Скорость ветра: {average_values['avrg_wind_speed'].iloc[0]:.1f} км/ч\n\n"
    stats_text += "Максимальные значения:\n"
    stats_text += f"  Температура: {max_values['max_temp'].iloc[0]:.1f}°C\n"
    stats_text += f"  Осадки: {max_values['max_prec'].iloc[0]:.1f} мм\n"
    stats_text += f"  Скорость ветра: {max_values['max_wind_speed'].iloc[0]:.1f} км/ч\n\n"
    stats_text += "Минимальные значения:\n"
    stats_text += f"  Температура: {min_values['min_temp'].iloc[0]:.1f}°C\n"
    stats_text += f"  Осадки: {min_values['min_prec'].iloc[0]:.1f} мм\n"
    stats_text += f"  Скорость ветра: {min_values['min_wind_speed'].iloc[0]:.1f} км/ч"
    ax4.text(0.1, 0.5, stats_text, fontsize=10, verticalalignment='center',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    ax5 = fig.add_subplot(gs[2, 1])
    ax5_twin = ax5.twinx()
    
    temp_max_norm = (monthly_values['temp_max'] - monthly_values['temp_max'].min()) / \
                    (monthly_values['temp_max'].max() - monthly_values['temp_max'].min()) * 100
    prec_norm = (monthly_values['prec'] - monthly_values['prec'].min()) / \
                (monthly_values['prec'].max() - monthly_values['prec'].min()) * 100
    wind_norm = (monthly_values['wind_speed'] - monthly_values['wind_speed'].min()) / \
                (monthly_values['wind_speed'].max() - monthly_values['wind_speed'].min()) * 100
    
    ax5.plot(months, temp_max_norm, 'o-', color='#ff6b6b', label='Температура (норм.)', linewidth=2)
    ax5_twin.plot(months, prec_norm, 's-', color='#3498db', label='Осадки (норм.)', linewidth=2)
    ax5_twin.plot(months, wind_norm, '^-', color='#9b59b6', label='Ветер (норм.)', linewidth=2)
    
    ax5.set_xlabel('Месяц')
    ax5.set_ylabel('Температура (нормализованная)', color='#ff6b6b')
    ax5_twin.set_ylabel('Осадки и ветер (нормализованные)', color='#3498db')
    ax5.set_title('Сравнение всех параметров по месяцам (нормализованные)')
    ax5.tick_params(axis='x', rotation=45)
    ax5.grid(True, alpha=0.3)
    
    lines1, labels1 = ax5.get_legend_handles_labels()
    lines2, labels2 = ax5_twin.get_legend_handles_labels()
    ax5.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    pyplot.show()