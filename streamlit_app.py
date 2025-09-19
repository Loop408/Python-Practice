import streamlit as st

st.set_page_config(page_title="B.Tech CGPA Calculator", page_icon="")

st.title("B.Tech CGPA Calculator (Current Students)")

# Select current year (1 to 4)
year_label_to_value = {
    "1st Year": 1,
    "2nd Year": 2,
    "3rd Year": 3,
    "4th Year": 4,
}
selected_year_label = st.radio(
    "Select your current year",
    options=list(year_label_to_value.keys()),
    horizontal=True,
)
selected_year = year_label_to_value[selected_year_label]

# Assume 2 semesters per year; completed semesters = year * 2
completed_semesters = selected_year * 2

st.write(
    "Enter SGPA for the semesters you have completed. Future semesters are shown as Null."
)

sgpas = []
for i in range(1, 9):
    if i <= completed_semesters:
        choice = st.radio(
            f"Semester {i}",
            options=["Enter SGPA", "Null"],
            index=0,
            horizontal=True,
            key=f"sem_choice_{i}",
        )
        if choice == "Enter SGPA":
            sgpa_value = st.number_input(
                f"SGPA - Semester {i}",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.01,
                format="%.2f",
                key=f"sgpa_{i}",
            )
            sgpas.append(sgpa_value)
        else:
            sgpas.append(None)
    else:
        st.selectbox(
            f"SGPA - Semester {i}",
            options=["Null"],
            index=0,
            disabled=True,
            key=f"sgpa_null_{i}",
        )

cgpa = None
if st.button("Calculate CGPA"):
    valid_sgpas = [s for s in sgpas if s is not None]
    if len(valid_sgpas) == 0:
        st.error("Please enter at least one SGPA.")
    else:
        cgpa = sum(valid_sgpas) / len(valid_sgpas)

if cgpa is not None:
    st.success(f"Current CGPA (based on {len(sgpas)} semesters): {cgpa:.2f}")
