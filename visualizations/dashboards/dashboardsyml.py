import os
import yaml

# Define the name of the dashboard
dashboard_name = 'OS Hunting Dashboard'

# Define the directory containing the Sigma rules
sigma_dir = 'C:\\Users\\SalmaAlmaz\\Documents\\Mitre-threat-coverage\\visualizations\\visualizations'

# Create a list to store the visualization names
visualization_list = []

# Loop through each Sigma rule and add the visualization name to the list
for filename in os.listdir(sigma_dir):
    if filename.endswith('.yml'):
        with open(os.path.join(sigma_dir, filename), 'r') as f:
            sigma_rule = yaml.safe_load(f)
            visualization_list.append(sigma_rule['title'])

# Define the YAML dictionary for the dashboard
dashboard_dict = {
    'author': 'DS',
    'type': 'dashboard',
    'name': dashboard_name,
    'title': dashboard_name,
    'darktheme': True,
    'visualizations': visualization_list
}

# Write the YAML file
with open('dashboard.yml', 'w') as f:
    yaml.dump(dashboard_dict, f)
