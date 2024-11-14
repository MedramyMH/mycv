from flask import Flask, render_template
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px

# Initialize Flask and Dash
server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.LUX, "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"], url_base_pathname='/dashboard/')

skills_data = {
    'Skill': ['Data Analysis', 'Machine Learning', 'Programming', 'Robotics', 'Automation'],
    'Level': [30, 25, 20, 15, 10]
}
skill_language = {
    'Skill': ['Python', 'SQL', 'Java'],
    'Level': [40, 35, 25]
}

# Bar chart for technical skills
skills_charts = px.bar(
    x=skills_data['Skill'], y=skills_data['Level'], labels={'x': 'Skill', 'y': 'Proficiency'},
    title="Technical Skills", color=skills_data['Skill'], color_discrete_sequence=px.colors.sequential.Viridis
)

# Pie chart for competencies
competencies_chart = px.pie(
    names=skill_language['Skill'], values=skill_language['Level'], title="Language Distribution",
    color_discrete_sequence=px.colors.sequential.Plasma
)

# Language Pie Charts
language_data = {
    'Language': ['English', 'French', 'Arabic'],
    'Proficiency': [90, 70, 100]
}

language_chart = px.pie(
    names=language_data['Language'], 
    values=language_data['Proficiency'], 
    title="Language Proficiency",
    color_discrete_sequence=px.colors.sequential.Plasma
)

projects_data = [
    {'name': 'Predictive Maintenance Model', 'desc': 'A predictive model for equipment failure using ML.'},
    {'name': 'Customer Segmentation', 'desc': 'Clustering customers for targeted marketing campaigns.'},
    {'name': 'Product Quality Checker', 'desc': 'Develop a Product Quality Checker using machine learning to classify product images as OK (good quality) or NOK (defective).'},
    {'name': 'Face Recognition System using FaceNet/VGG16', 'desc': 'Develop a security system that recognizes individuals and grants or denies access based on facial features.'}
]

# Layout for the dashboard
app.layout = dbc.Container([
    # Row for Title
    dbc.Row([
        dbc.Col(html.H1("My Data Science Resume", className="text-center my-4 text-primary")),
    ]),
    # Row for Profile Card
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardImg(src="/assets/r1.jpg", top=True, className="rounded-circle img-thumbnail mx-auto d-block", style={"width": "150px", "height": "150px"}),
            dbc.CardBody([
                html.H4("Mohamed Ramy Mahjoub", className="card-title text-center"),
                html.P("Data Scientist | Robotic Engineer", className="card-text text-center"),
                html.P("Recent graduate from GOMYCODE Data Science program with 3 years of experience in industrial automation, robotics, and data analysis.", className="text-muted text-center"),
                dbc.Button("LinkedIn", color="primary", outline=True, href="https://www.linkedin.com/in/mohamedramymahjoub?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app", className="mx-auto d-block", target="_blank"),
            ])
        ], className="shadow p-3 mb-5 bg-white rounded"), width=4),  # Width is assigned to dbc.Col
    ], justify="center"),

    # Row for Skills Section (Bar and Pie Charts)
    dbc.Row([dbc.Col(html.H2("Skills", className="text-info mt-4"))], className="mt-5", style={"marginLeft": "20px"}),
   
    dbc.Row([
        dbc.Col([dcc.Graph(figure=skills_charts, config={"displayModeBar": False})], width=6),  # Width is assigned to dbc.Col
        dbc.Col([dcc.Graph(figure=competencies_chart, config={"displayModeBar": False})], width=6),  # Width is assigned to dbc.Col
    ], justify="center"),

    # Row for Projects Section
    dbc.Row([dbc.Col(html.H2("Projects", className="text-info mt-4"))], className="mt-5", style={"marginLeft": "20px"}),
    dbc.Row([
        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5(project['name'], className="card-title"),
                    html.P(project['desc'], className="card-text")
                ])
            ], className="mb-4 shadow-sm"), width=6) for project in projects_data  # Width is assigned to dbc.Col
        ]),
    ], justify="center"),

    # Row for Experience Section
    dbc.Row([
        html.H2("Experience", className="text-info mt-4"),
        dbc.Card([
            dbc.CardBody([
                html.P("Automation Computer Engineer with 4 years of experience in Algeria, specializing in Siemens, Schneider, and OMRON CX programming.", className="card-text"),
                html.H5("Previous roles:"), html.P("Automation Engineer : 2016-2020", className="card-text"),html.P("Production Engineer : 2020-2021", className="card-text"),html.P("Samples Coordinator : 2021-2023", className="card-text"),
                html.H5("Actual position: "), html.P("Robotic and AI Engineer : since 2023 experienced in designing and implementing robotic systems and AI.", className="card-text")
            ])
        ], className="shadow-sm p-4 bg-light")
    ], justify="center", style={"marginLeft": "15px", "marginRight": "15px"}),
    
    # Language Skill Meters
    dbc.Row([dbc.Col(html.H2("Languages", className="text-info mt-4"))], className="mt-5", style={"marginLeft": "20px"}),
    dbc.Row([
        dbc.Col([
            
            dbc.Row([
                dbc.Col(html.Img(src="https://upload.wikimedia.org/wikipedia/en/a/a4/Flag_of_the_United_States.svg", style={"width": "30px"}), width=1),
                dbc.Col(dbc.Progress("English - Fluent", value=90, color="success", className="mb-2"), width=11),
            ]),
            dbc.Row([
                dbc.Col(html.Img(src="https://upload.wikimedia.org/wikipedia/en/c/c3/Flag_of_France.svg", style={"width": "30px"}), width=1),
                dbc.Col(dbc.Progress("French - Intermediate", value=70, color="info", className="mb-2"), width=11),
            ]),
            dbc.Row([
                dbc.Col(html.Img(src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Flag_of_Tunisia.svg/640px-Flag_of_Tunisia.svg.png", style={"width": "30px"}), width=1),
                dbc.Col(dbc.Progress("Arabic - Native", value=100, color="warning", className="mb-2"), width=11),
            ])
        ], width=6)
    ], style={"marginLeft": "15px", "marginRight": "15px"}),

    

    # Row for Certificate Section at the Bottom
    dbc.Row([dbc.Col(html.H2("Certificate", className="text-info mt-4"))], className="mt-5", style={"marginLeft": "20px"}),
    dbc.Row([
        dbc.Col(html.Iframe(src="https://diploma.gomycode.app/?id=31724641215864560", style={"width": "100%", "height": "1000px", "border": "none"}), width=12)  # Width is assigned to dbc.Col
    ])
], fluid=True)


# Flask route
@server.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
