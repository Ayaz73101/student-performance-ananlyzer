import streamlit as st
import pandas as pd
import joblib


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #888;
    margin-bottom: 30px;
}

.result-card {
    padding: 25px;
    border-radius: 15px;
    background-color: #1e293b;
    border: 1px solid #475569;
    text-align: center;
    color: white;
}

.score {
    font-size: 48px;
    font-weight: 700;
    color: white;
}

.category {
    font-size: 24px;
    font-weight: 600;
    color: white;
}

.section-title {
    font-size: 24px;
    font-weight: 600;
    margin-top: 20px;
    margin-bottom: 15px;
}

div.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD MODEL
# =========================================================

MODEL_PATH = "model/student_performance_model.pkl"

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    st.error("❌ Unable to load the machine learning model.")
    st.exception(e)
    st.stop()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🎓 Student Analyzer")

    st.markdown("---")

    st.subheader("About")

    st.write(
        "This application uses a Machine Learning model "
        "to predict a student's overall academic performance "
        "based on behavioral and academic-related factors."
    )

    st.markdown("---")

    st.subheader("🤖 Model")

    st.write("Gradient Boosting Regressor")

    st.markdown("---")

    st.subheader("📌 Features")

    st.write("• Attendance / Absence")
    st.write("• Self-study hours")
    st.write("• Part-time job")
    st.write("• Extracurricular activities")
    st.write("• Gender")
    st.write("• Career aspiration")

    st.markdown("---")

    st.caption("Student Performance Analyzer v1.0")


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🎓 Student Performance Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine Learning based student performance prediction system'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# NAVIGATION
# =========================================================

tab_home, tab_prediction, tab_analytics, tab_model = st.tabs([
    "🏠 Home",
    "🔮 Prediction",
    "📊 Analytics",
    "🤖 Model Information"
])


# =========================================================
# HOME TAB
# =========================================================

with tab_home:

    st.subheader("Welcome to Student Performance Analyzer 👋")

    st.write(
        """
        Student Performance Analyzer is a machine-learning based
        application designed to estimate a student's overall academic
        performance using behavioral, attendance, study and
        career-related information.
        """
    )

    st.markdown("### 🚀 What this application does")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            "📋\n\n"
            "**Student Analysis**\n\n"
            "Enter a student's academic and behavioral information."
        )

    with col2:
        st.info(
            "🤖\n\n"
            "**Machine Learning**\n\n"
            "A Gradient Boosting model generates the predicted score."
        )

    with col3:
        st.info(
            "📊\n\n"
            "**Performance Insights**\n\n"
            "View predicted performance and model analytics."
        )

    st.markdown("### 🔄 Machine Learning Workflow")

    st.write(
        """
        Dataset → Data Cleaning → Feature Engineering →
        Preprocessing → Model Training → Model Evaluation →
        Hyperparameter Tuning → Prediction
        """
    )

    st.markdown("### 🧠 Input Features")

    features = pd.DataFrame({
        "Feature": [
            "Gender",
            "Part-Time Job",
            "Absence Days",
            "Extracurricular Activities",
            "Weekly Self-Study Hours",
            "Career Aspiration"
        ],
        "Type": [
            "Categorical",
            "Boolean",
            "Numerical",
            "Boolean",
            "Numerical",
            "Categorical"
        ]
    })

    st.dataframe(
        features,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# PREDICTION TAB
# =========================================================

with tab_prediction:

    st.markdown(
        '<div class="section-title">📋 Student Information</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        gender = st.selectbox(
            "Gender",
            ["male", "female"]
        )

        part_time_job = st.selectbox(
            "Part-Time Job",
            [False, True],
            format_func=lambda x: "Yes" if x else "No"
        )

        absence_days = st.number_input(
            "Absence Days",
            min_value=0,
            max_value=30,
            value=5,
            step=1
        )

    with col2:

        extracurricular_activities = st.selectbox(
            "Extracurricular Activities",
            [False, True],
            format_func=lambda x: "Yes" if x else "No"
        )

        weekly_self_study_hours = st.number_input(
            "Weekly Self-Study Hours",
            min_value=0,
            max_value=50,
            value=10,
            step=1
        )

        career_aspiration = st.selectbox(
            "Career Aspiration",
            [
                "Lawyer",
                "Doctor",
                "Government Officer",
                "Artist",
                "Unknown",
                "Software Engineer",
                "Teacher",
                "Business Owner",
                "Scientist",
                "Banker",
                "Writer",
                "Accountant",
                "Designer",
                "Construction Engineer",
                "Game Developer",
                "Stock Investor",
                "Real Estate Developer"
            ]
        )

    st.markdown("---")

    predict_button = st.button(
        "🔮 Predict Student Performance"
    )

    if predict_button:

        student = pd.DataFrame({
            "gender": [gender],
            "part_time_job": [part_time_job],
            "absence_days": [absence_days],
            "extracurricular_activities": [
                extracurricular_activities
            ],
            "weekly_self_study_hours": [
                weekly_self_study_hours
            ],
            "career_aspiration": [
                career_aspiration
            ]
        })

        try:

            prediction = model.predict(student)[0]

            # Keep prediction between 0 and 100
            prediction = max(0, min(100, prediction))

            # ---------------------------------------------
            # PERFORMANCE CATEGORY
            # ---------------------------------------------

            if prediction >= 90:
                category = "Excellent"
                message = "Outstanding predicted academic performance."

            elif prediction >= 80:
                category = "Very Good"
                message = "Strong predicted academic performance."

            elif prediction >= 70:
                category = "Good"
                message = "Good predicted academic performance."

            elif prediction >= 60:
                category = "Average"
                message = "Average predicted academic performance."

            elif prediction >= 50:
                category = "Needs Improvement"
                message = (
                    "Additional academic support may be useful."
                )

            else:
                category = "At Risk"
                message = (
                    "The prediction indicates a need for "
                    "additional academic attention."
                )

            # =================================================
            # RESULT
            # =================================================

            st.markdown("---")

            st.markdown(
                '<div class="section-title">📊 Prediction Result</div>',
                unsafe_allow_html=True
            )

            result_col1, result_col2 = st.columns(2)

            with result_col1:

                st.markdown(
                    f"""
                    <div class="result-card">
                        <div>Predicted Overall Score</div>
                        <div class="score">{prediction:.2f}</div>
                        <div>out of 100</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with result_col2:

                st.markdown(
                    f"""
                    <div class="result-card">
                        <div>Performance Category</div>
                        <div class="category">{category}</div>
                        <div>Student Assessment</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.write("")

            st.progress(prediction / 100)

            st.info(f"💡 {message}")

            # =================================================
            # STUDENT PROFILE
            # =================================================

            st.markdown(
                '<div class="section-title">👤 Student Profile</div>',
                unsafe_allow_html=True
            )

            profile_col1, profile_col2, profile_col3 = st.columns(3)

            with profile_col1:

                st.metric(
                    "Absence Days",
                    absence_days
                )

                st.metric(
                    "Part-Time Job",
                    "Yes" if part_time_job else "No"
                )

            with profile_col2:

                st.metric(
                    "Self-Study Hours",
                    f"{weekly_self_study_hours} hrs/week"
                )

                st.metric(
                    "Extracurricular",
                    "Yes" if extracurricular_activities else "No"
                )

            with profile_col3:

                st.metric(
                    "Gender",
                    gender.title()
                )

                st.metric(
                    "Career",
                    career_aspiration
                )

            # =================================================
            # INPUT SUMMARY
            # =================================================

            st.markdown(
                '<div class="section-title">📋 Input Summary</div>',
                unsafe_allow_html=True
            )

            profile = pd.DataFrame({
                "Parameter": [
                    "Gender",
                    "Part-Time Job",
                    "Absence Days",
                    "Extracurricular Activities",
                    "Weekly Self-Study Hours",
                    "Career Aspiration"
                ],
                "Value": [
                    gender.title(),
                    "Yes" if part_time_job else "No",
                    absence_days,
                    "Yes" if extracurricular_activities else "No",
                    weekly_self_study_hours,
                    career_aspiration
                ]
            })

            st.dataframe(
                profile,
                use_container_width=True,
                hide_index=True
            )

            # =================================================
            # DOWNLOAD REPORT
            # =================================================

            result_data = pd.DataFrame({
                "Gender": [gender],
                "Part-Time Job": [part_time_job],
                "Absence Days": [absence_days],
                "Extracurricular Activities": [
                    extracurricular_activities
                ],
                "Weekly Self Study Hours": [
                    weekly_self_study_hours
                ],
                "Career Aspiration": [
                    career_aspiration
                ],
                "Predicted Score": [
                    round(prediction, 2)
                ],
                "Performance Category": [
                    category
                ]
            })

            csv = result_data.to_csv(index=False)

            st.download_button(
                label="📥 Download Prediction Report",
                data=csv,
                file_name="student_prediction_report.csv",
                mime="text/csv"
            )

        except Exception as e:

            st.error("❌ Prediction failed.")
            st.exception(e)


# =========================================================
# ANALYTICS TAB
# =========================================================

with tab_analytics:

    st.subheader("📊 Model Analytics")

    st.write(
        "Explore the machine learning model's feature importance "
        "and cross-validation performance."
    )

    # =====================================================
    # FEATURE IMPORTANCE
    # =====================================================

    st.markdown("### 🧠 Feature Importance")

    try:

        preprocessor = model.named_steps["preprocessor"]
        trained_model = model.named_steps["model"]

        feature_names = preprocessor.get_feature_names_out()

        importance = trained_model.feature_importances_

        feature_importance = pd.DataFrame({
            "Feature": feature_names,
            "Importance": importance
        })

        feature_importance["Feature"] = (
            feature_importance["Feature"]
            .str.replace("num__", "", regex=False)
            .str.replace("cat__", "", regex=False)
        )

        feature_importance = feature_importance.sort_values(
            "Importance",
            ascending=False
        )

        st.bar_chart(
            feature_importance.set_index("Feature")[
                "Importance"
            ]
        )

        feature_importance["Importance"] = (
            feature_importance["Importance"].round(4)
        )

        st.dataframe(
            feature_importance,
            use_container_width=True,
            hide_index=True
        )

    except Exception as e:

        st.error("Unable to calculate feature importance.")
        st.exception(e)

    # =====================================================
    # MODEL COMPARISON
    # =====================================================

    st.markdown("---")

    st.markdown("### 📈 Model Comparison")

    cv_results = pd.DataFrame({
        "Model": [
            "Gradient Boosting",
            "Random Forest",
            "Extra Trees",
            "Decision Tree",
            "Linear Regression"
        ],
        "Mean CV RMSE": [
            4.435,
            4.456,
            4.491,
            4.571,
            4.679
        ]
    })

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Selected Model",
            "Gradient Boosting"
        )

    with col2:

        st.metric(
            "CV RMSE",
            "4.435"
        )

    with col3:

        st.metric(
            "Validation",
            "5-Fold"
        )

    st.bar_chart(
        cv_results.set_index("Model")[
            "Mean CV RMSE"
        ]
    )

    st.dataframe(
        cv_results,
        use_container_width=True,
        hide_index=True
    )

    st.info(
        "RMSE represents the typical magnitude of prediction "
        "error. Lower RMSE indicates lower prediction error "
        "on the cross-validation folds."
    )


# =========================================================
# MODEL INFORMATION TAB
# =========================================================

with tab_model:

    st.subheader("🤖 Machine Learning Model")

    st.write(
        "The Student Performance Analyzer uses a "
        "**Gradient Boosting Regressor** to predict the "
        "student's overall score."
    )

    st.markdown("### 📊 Model Evaluation")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Model",
            "Gradient Boosting"
        )

    with col2:

        st.metric(
            "CV RMSE",
            "4.435"
        )

    with col3:

        st.metric(
            "Validation",
            "5-Fold CV"
        )

    st.markdown("### 📋 Features Used")

    model_features = pd.DataFrame({
        "Feature": [
            "Gender",
            "Part-Time Job",
            "Absence Days",
            "Extracurricular Activities",
            "Weekly Self-Study Hours",
            "Career Aspiration"
        ],
        "Role": [
            "Categorical predictor",
            "Categorical predictor",
            "Numerical predictor",
            "Categorical predictor",
            "Numerical predictor",
            "Categorical predictor"
        ]
    })

    st.dataframe(
        model_features,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### 🔄 Machine Learning Pipeline")

    st.code(
        """
Raw Dataset
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
Train/Test Split
     ↓
Preprocessing
     ↓
Model Training
     ↓
5-Fold Cross Validation
     ↓
Hyperparameter Tuning
     ↓
Gradient Boosting Model
     ↓
Student Performance Prediction
        """,
        language="text"
    )

    st.info(
        "The model predicts an overall performance score based "
        "on the selected input features. The prediction should "
        "be interpreted as a model estimate rather than a "
        "guaranteed academic outcome."
    )