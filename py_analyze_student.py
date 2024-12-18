# импорт библиотек
import pandas as pd
import numpy as np
import streamlit as st
import joblib
from joblib import load

# загрузка модели
model = joblib.load("work_life_balance_model.pkl")

all_columns = [
    'Work_Hours',
    'Job_Type',
    'Sleep_Hours',
    'Study_Hours',
    'Stress_Level',
    'Academic_Performance',
    'Social_Activity',
    'Job_Satisfaction'
    ]

# Загрузка LabelEncoder
le = load('label_encoder.joblib')

# Получение уникальных значений Job_Type из LabelEncoder
job_type_options = list(le.classes_)


# Указание контента сайта
st.title("Прогноз Work-Life Balance")

work_hours = st.number_input(
    "Количество часов работы в неделю",
    min_value=0,
    max_value=40,
    value=10,
    step=1
)
job_type = st.selectbox("Выберите тип работы", job_type_options)
sleep_hours = st.number_input(
    "Количество часов сна (среднее за неделю)",
    min_value=3,
    max_value=9,
    value=8,
    step=1
)
study_hours = st.number_input(
    "Количество часов учебы в неделю",
    min_value=0,
    max_value=25,
    value=10,
    step=1
)
stress_level = st.number_input(
    "Уровень стресса по ощущеням от 1 до 10",
    min_value=1,
    max_value=10,
    value=5,
    step=1
)
academic_performance = st.number_input(
    "Средний балл по учебе",
    min_value=2.0,
    max_value=5.0,
    value=4.0,
    step=0.1
)
social_activity = st.number_input(
    "Социальная активность (по насыщенности от 0 до 20)",
    min_value=0,
    max_value=20,
    value=10,
    step=1
)
job_satisfaction = st.number_input(
    "Удовлетворенность работой (от 1 до 10)",
    min_value=0,
    max_value=10,
    value=7,
    step=1
)

# Преобразование данных и прогноз
input_data = {
    'Work_Hours': work_hours,
    'Job_Type': job_type,
    'Sleep_Hours': sleep_hours,
    'Study_Hours': study_hours,
    'Stress_Level': stress_level,
    'Academic_Performance': academic_performance,
    'Social_Activity': social_activity,
    'Job_Satisfaction': job_satisfaction
}
#Создание датафрейма
input_df = pd.DataFrame([input_data], columns=all_columns).fillna(0)

#Преобразование поля работы и маштабирование
input_df["Job_Type"] = le.transform(input_df["Job_Type"])[0]

if st.button("Предсказать Work-Life Balance"):
    prediction = model.predict(input_scaled)
    st.success(f"Ориентировочный баланс, который у вас будет (от 0 до 10): {int(prediction[0])}")
