from flask import Flask, render_template
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px

# Initialize Flask
server = Flask(__name__)

# Initialize Dash
app = dash.Dash(
    __name__,
    server=server,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        dbc.themes.LUX,
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css",
    ],
    url_base_pathname='/dashboard/'
)

# Skills data with font-awesome and external image icons
skills_data = {
    'Skill': ['Data Analysis', 'Machine Learning', 'Programming', 'Visualization', 'Deep Learning'],
    'Level': [25, 25, 20, 25, 30],
    'Icon': [
        'fas fa-chart-line',  # Font Awesome icon for Data Analysis
        'fas fa-robot',       # Font Awesome icon for Machine Learning
        'fas fa-code',        # Font Awesome icon for Programming
        'assets/DataVisualization.png',  # External image for Visualization
        'assets/DeepLearning.png'  # External image for Deep Learning
    ]
}

# Skills data with font-awesome and external image icons
skills_data_formatted =  [
    {
        'name': 'Flask',
        'desc': 'A micro web framework for Python, designed to make getting started quick and easy, with the ability to scale up to complex applications.',
        'image': 'assets/flask.png',
        'level': 25
    },
    {
        'name': 'Streamlit',
        'desc': 'An open-source app framework for Machine Learning and Data Science projects, allowing users to create interactive web applications.',
        'image': 'assets/logos_streamlit.svg',
        'level': 25
    },
    {
        'name': 'Power BI',
        'desc': 'A business analytics tool by Microsoft for creating reports and dashboards to visualize and share insights from data.',
        'image': 'assets/power-bi.png',
        'level': 20
    },
    {
        'name': 'Tableau',
        'desc': 'A powerful data visualization tool used in Business Intelligence to simplify raw data into understandable formats.',
        'image': 'assets/logos-tableau-icon.svg',
        'level': 25
    },
    {
        'name': 'SQL',
        'desc': 'A standard language for storing, manipulating, and retrieving data in relational databases.',
        'image': 'assets/sql.svg',
        'level': 30
    },
    {
        'name': 'HTML5',
        'desc': 'The latest version of HyperText Markup Language, used to structure content on the web.',
        'image': 'assets/html5.svg',
        'level': 30
    }
]




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
    {'name': 'Predictive Maintenance Model', 'desc': 'A machine learning model to predict equipment failures and optimize maintenance schedules.', 'image': 'assets/predictive_maintenance.jpg', 'tech_stack': 'ML, AI'},
    {'name': 'ChatBot', 'desc': 'An AI-powered chatbot designed to interact with users and answer inquiries based on pre-trained data.', 'image': 'assets/chatbot.png', 'tech_stack': 'K-means, Python'},
    {'name': 'Product Quality Checker', 'desc': 'A computer vision model using CNNs to classify and detect defects in product images for quality control before export.', 'image': 'assets/product_quality.jpg', 'tech_stack': 'CNN, TensorFlow'},
    {'name': 'Face Recognition System', 'desc': 'A facial recognition security system that grants or denies access based on facial features using deep learning models.', 'image': 'assets/face_recognition.jpg', 'tech_stack': 'FaceNet, VGG16'},
    {'name': 'Stock Management', 'desc': 'A system that tracks and organizes inventory in real-time to optimize stock levels and reduce errors.', 'image': 'assets/Inventory_Management.jpg', 'tech_stack': 'JavaScript, Node.js, MongoDB'},
    {'name': 'Web Scraping', 'desc': 'A web scraping tool to extract data from websites for analysis or use in other applications.', 'image': 'assets/WebScraping.jpg', 'tech_stack': 'Python, BeautifulSoup, Scrapy'}
]



# Layout for the dashboard
app.layout = dbc.Container([

# Row for Title
dbc.Row([
    dbc.Col(html.H1(
        "My Data Science Resume",
        className="text-center my-4",
        style={
            "font-family": "Arial, sans-serif",
            "font-weight": "bold",
            "color": "rgb(30 153 205)",
            "text-shadow": "2px 2px 4px rgba(0, 0, 0, 0.2)"
        }
    )),
], justify="center"),

    # Row for Profile Card
dbc.Row([
    dbc.Col(dbc.Card([
        dbc.CardImg(
            src="assets/r2.jpg",
            top=True,
            className="rounded-circle img-thumbnail mx-auto d-block",
            style={"width": "250px", "height": "250px", "border": "5px solid rgb(30 153 205)"}
        ),
        dbc.CardBody([
            html.H4("Mohamed Ramy Mahjoub", className="card-title text-center", style={"font-family": "Arial, sans-serif", "font-weight": "bold", "color": "rgb(30 153 205)"}),
            html.P("Data Scientist | Robotic Engineer", className="card-text text-center", style={"font-size": "1.1em","font-weight": "bold", "color": "#6c757d"}),
            html.P(
                "graduated from ENET`com Sfax since 2015",
                className="text-muted text-center",
                style={"font-size": "0.9em", "line-height": "1.5"}
            ),
            html.P(
                "Recent graduate from GOMYCODE Data Science program with 8 years of experience in industrial automation, robotics, and data analysis.",
                className="text-muted text-center",
                style={"font-size": "0.9em", "line-height": "1.5"}
            ),
            html.Div([
                html.I(className="bi bi-envelope-fill me-2", style={"color": "#007bff"}),
                html.Span("ramymh.contact@gmail.com", style={"font-weight": "bold", "color": "#495057"})
            ], className="d-flex justify-content-center align-items-center mb-3"),
            dbc.Button(
                [html.I(className="bi bi-linkedin me-2"), "LinkedIn"],
                color="primary",
                outline=False,
                href="https://www.linkedin.com/in/mohamedramymahjoub?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app",
                className="mx-auto d-block",
                target="_blank",
                style={"padding": "10px 20px", "font-size": "1em", "border-radius": "20px"}
            )
        ])
    ], className="shadow-lg p-4 bg-gradient rounded", style={"background": "linear-gradient(to bottom, #ffffff, #f8f9fa)"}), width=4),
], justify="center"),

    # Row for Skills Section (Bar and Pie Charts)
    dbc.Row([dbc.Col(html.H2("Skills", className="text-info mt-4"))], className="mt-5", style={"marginLeft": "20px"}),
   
    dbc.Row([
        dbc.Col([dcc.Graph(figure=skills_charts, config={"displayModeBar": False})], width=6),  # Width is assigned to dbc.Col
        dbc.Col([dcc.Graph(figure=competencies_chart, config={"displayModeBar": False})], width=6),  # Width is assigned to dbc.Col
    ], justify="center"),
    
    
    
    
 dbc.Row([
    dbc.Col([
        dbc.Row([
            dbc.Col(
                dbc.Card([
                    dbc.CardBody(
                        [
                            # Animated icon or image
                            html.Div(
                                html.Img(
                                    src=skills_data_formatted[i]['image'],
                                    style={"width": "40px", "height": "40px"}
                                ),
                                className="animate__animated animate__fadeInUp d-flex justify-content-center align-items-center mb-2"  # Animation + centrage
                            ),
                            # Skill name
                            html.P(
                                skills_data_formatted[i]['name'],
                                className="text-center mt-2"
                            ),
                            # Skill description
                            html.P(
                                skills_data_formatted[i]['desc'],
                                className="text-center text-muted small"
                            )
                        ]
                    )
                ], className="shadow-lg p-4 bg-gradient rounded h-100 d-flex flex-column justify-content-between", style={"width": "250px", "margin": "0.5rem"})
            ) for i in range(len(skills_data_formatted))
        ], justify="center")
    ], width=12)
], justify="center", className="mt-4"),


    dbc.Row([dbc.Col(html.H2("Projects", className="text-info mt-4"))], className="mt-5", style={"marginLeft": "20px"}),

    dbc.Row([
        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardImg(src=project['image'], top=True, className="rounded-circle mx-auto d-block", style={"width": "250px", "height": "250px"}),
                dbc.CardBody([
                    html.H5(project['name'], className="card-title text-center"),
                    html.P(project['desc'], className="card-text text-center"),
                    # Add badge for tech stack used in the project
                    dbc.Badge(project['tech_stack'], color="primary", className="mb-2")
                ]),
            ], className="mb-4 shadow-lg p-4 bg-gradient rounded h-300 d-flex flex-column justify-content-between"), width=6) for project in projects_data
        ])
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
            dbc.Col(
                dbc.Progress("English - Fluent", value=90, color="success", className="mb-2", 
                             style={"font-size": "1.3rem", "height": "40px", "text-align": "center", "line-height": "40px", "overflow": "hidden"}),
                width=11
            ),
        ], className="align-items-center"),  # Ensure proper vertical alignment
        dbc.Row([
            dbc.Col(html.Img(src="https://upload.wikimedia.org/wikipedia/en/c/c3/Flag_of_France.svg", style={"width": "30px"}), width=1),
            dbc.Col(
                dbc.Progress("French - Intermediate", value=70, color="info", className="mb-2", 
                             style={"font-size": "1.3rem", "height": "40px", "text-align": "center", "line-height": "40px", "overflow": "hidden"}),
                width=11
            ),
        ], className="align-items-center"),  # Ensure proper vertical alignment
        dbc.Row([
            dbc.Col(html.Img(src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Flag_of_Tunisia.svg/640px-Flag_of_Tunisia.svg.png", style={"width": "30px"}), width=1),
            dbc.Col(
                dbc.Progress("Arabic - Native", value=100, color="warning", className="mb-2", 
                             style={"font-size": "1.3rem", "height": "40px", "text-align": "center", "line-height": "40px", "overflow": "hidden"}),
                width=11
            ),
        ], className="align-items-center")  # Ensure proper vertical alignment
    ], width=6)
], style={"marginLeft": "15px", "marginRight": "15px", "height": "100%"}),


    

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
