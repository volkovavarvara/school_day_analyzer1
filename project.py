import streamlit as st
import matplotlib.pyplot as plt

st.title("Интерактивный анализ режима дня школьника")
st.info("Пожалуйста, отвечайте на вопросы, имея в виду ОДИН конкретный день, например, вчерашний учебный день. Так результаты будут максимально точными") 

# состояние страницы
if "show_result" not in st.session_state:
    st.session_state.show_result = False

# Тест
if not st.session_state.show_result:
    with st.form("test"):

        age = st.number_input("Сколько вам лет?", min_value=7, max_value=17, step=1)

        grade = st.number_input("В каком классе вы учитесь?", min_value=1, max_value=11, step=1)

        sleep = st.number_input("Сколько часов вы спали в этот день?",min_value=0.0, max_value=24.0, step=0.5)

        school = st.number_input("Сколько у вас было уроков?",min_value=0, max_value=10, step=1)

        school_hours = school * 0.75

        homework = st.number_input("Сколько часов вы потратили на выполнение домашнего задания в этот день?",min_value=0.0, max_value=24.0, step=0.5)

        way_to_school = st.number_input("Сколько времени у вас заняла дорога до школы (в минутах)?",min_value=0)
        way_home = st.number_input("Сколько времени у вас заняла дорога домой (в минутах)?",min_value=0)

        total_way_minutes = way_to_school + way_home
        way_hours = total_way_minutes // 60
        way_minutes = total_way_minutes % 60

        classes_hours = 0
        classes_minutes = 0
        st.write("Сколько времени длились дополнительные занятия?")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

        with col1:
            classes_hours = st.number_input("", min_value=0, max_value=24, step=1)
        with col2:
            st.write("")
            st.write("Час(ов)")
        with col3:
            classes_minutes = st.number_input("", min_value=0, max_value=59, step=10)
        with col4:
            st.write("")
            st.write("Минут(ы)")

        submit = st.form_submit_button("Показать результаты")

        if submit:
            total_time = sleep + school_hours + homework + way_hours + classes_hours 
            if total_time > 24:
                st.error('Суммарное время превышает 24 часа. Проверьте данные')
            else:
                st.session_state.age = age
                st.session_state.grade = grade
                st.session_state.sleep = sleep
                st.session_state.school_hours = school_hours
                st.session_state.homework = homework
                st.session_state.way_hours = way_hours
                st.session_state.way_minutes = way_minutes
                st.session_state.classes_hours = classes_hours
                st.session_state.classes_minutes = classes_minutes

                st.session_state.show_result = True

# Результаты

if st.session_state.show_result:
    st.header("Результаты")

    age = st.session_state.age
    grade = st.session_state.grade
    sleep = st.session_state.sleep
    school_hours = st.session_state.school_hours
    homework = st.session_state.homework
    way_hours = st.session_state.way_hours
    way_minutes = st.session_state.way_minutes
    classes_hours = st.session_state.classes_hours
    classes_minutes = st.session_state.classes_minutes

    way_minutes_hours = way_minutes / 60
    classes_minutes_hours = classes_minutes / 60

    free_time = 24 - (sleep + school_hours + homework + way_hours + way_minutes_hours + classes_hours + classes_minutes_hours)

    free_time_minutes = int(free_time * 60)
    free_hours = free_time_minutes // 60
    free_minutes = free_time_minutes % 60

    # Оценка сна
    if 7 <= age <= 10:
        if sleep < 10:
            st.write("Вы спите меньше нормы для своего возраста. Попробуйте ложиться спать раньше.")
            st.write("Недостаток сна может привести к усталости и снижению концентрации внимания.")
        elif sleep <= 11:
            st.write("Продолжительность сна соответствует норме для вашего возраста.")
        else:
            st.write("«Вы спите больше рекомендуемой нормы для вашего возраста.")
            st.write("Слишком долгий сон может снижать активность в течение дня.")
            st.write("Попробуйте немного сократить время сна и понаблюдать за самочувствием.")

    elif 11 <= age <= 14:
        if sleep < 9:
            st.write("Вы спите меньше нормы для своего возраста. Попробуйте ложиться спать раньше.")
            st.write("Недостаток сна может привести к усталости и снижению концентрации внимания.")
        elif sleep <= 10:
            st.write("Продолжительность сна соответствует норме для вашего возраста.")
        else:
            st.write("«Вы спите больше рекомендуемой нормы для вашего возраста.")
            st.write("Слишком долгий сон может снижать активность в течение дня.")
            st.write("Попробуйте немного сократить время сна и понаблюдать за самочувствием.")
    elif 15 <= age <= 17:
        if sleep < 8:
            st.write("Вы спите меньше нормы для своего возраста. Попробуйте ложиться спать раньше.")
            st.write("Недостаток сна может привести к усталости и снижению концентрации внимания.")
        elif sleep <= 9:
            st.write("Продолжительность сна соответствует норме для вашего возраста.")
        else:
            st.write("«Вы спите больше рекомендуемой нормы для вашего возраста.")
            st.write("Слишком долгий сон может снижать активность в течение дня.")
            st.write("Попробуйте немного сократить время сна и понаблюдать за самочувствием.")   
    else:
        st.write("Возраст вне диапазона")

    st.write(f"Свободное время в день: "f"{free_hours} час(ов), {free_minutes} минут(ы)")

    # Оценка времени на домашнее задание
    if grade == 1 and homework > 1:
        st.write("Время, затраченное на выполнение домашнего задания, превышает рекомендованную норму для вашего класса.")
        st.write("Рекомендуется сократить время выполнения домашнего задания, чтобы избежать переутомления и сохранить время для отдыха и сна.")
    elif 2 <= grade <= 3 and homework > 1.5:
        st.write("Время, затраченное на выполнение домашнего задания, превышает рекомендованную норму для вашего класса.")
        st.write("Рекомендуется сократить время выполнения домашнего задания, чтобы избежать переутомления и сохранить время для отдыха и сна.")
    elif 4 <= grade <= 5 and homework > 2:
        st.write("Время, затраченное на выполнение домашнего задания, превышает рекомендованную норму для вашего класса.")
        st.write("Рекомендуется сократить время выполнения домашнего задания, чтобы избежать переутомления и сохранить время для отдыха и сна.")
    elif 6 <= grade <= 8 and homework > 2.5:
        st.write("Время, затраченное на выполнение домашнего задания, превышает рекомендованную норму для вашего класса.")
        st.write("Рекомендуется сократить время выполнения домашнего задания, чтобы избежать переутомления и сохранить время для отдыха и сна.")
    elif 9 <= grade <= 11 and homework > 3.5:
        st.write("Время, затраченное на выполнение домашнего задания, превышает рекомендованную норму для вашего класса.")
        st.write("Рекомендуется сократить время выполнения домашнего задания, чтобы избежать переутомления и сохранить время для отдыха и сна.")

    # Оценка загруженности дня
    if free_time < 2:
        st.error('День сильно перегружен. Практически нет времени на отдых')
    elif free_time < 5:
        st.warning('День умеренно загружен')
    else:
        st.success('День сбалансирован')

    # Диаграмма
    labels = ["сон", "школа", "домашнее задание", "дорога", "доп.занятия", "свободное время"]
    sizes = [sleep, school_hours, homework, way_hours + way_minutes_hours, classes_hours + classes_minutes_hours, free_time]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels = labels, autopct = "%1.1f%%", startangle = 90)        
    ax.axis("equal")        
    st.subheader("Распределение времени за день")        
    st.pyplot(fig)        

    if st.button("Пройти тест заново"):
        st.session_state.show_result = False