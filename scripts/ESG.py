import pandas as pd
import os

# Define the input file path
input_file = r'C:\Users\HarshNair\Downloads\emissions_data.xlsx'  # full path to the input file

# Get the directory of the input file
output_folder = os.path.dirname(input_file)

# Define output file paths in the same directory as input
validated_output = os.path.join(output_folder, 'validated_emissions_data.xlsx')
reduction_output = os.path.join(output_folder, 'reduction_opportunity_matrix.xlsx')
template_output = os.path.join(output_folder, 'emissions_data_template.xlsx')

# Check if the input file exists
if os.path.exists(input_file):
    data = pd.read_excel(input_file)
    data['Total_Emissions'] = data['Scope_1'] + data['Scope_2'] + data['Scope_3']
    invalid_rows = data[data[['Scope_1','Scope_2','Scope_3']].isnull().any(axis=1)]
    if not invalid_rows.empty:
        print('Warning: Missing data found in the following rows:')
        print(invalid_rows)
    else:
        print('All data valid!')
    data.to_excel(validated_output, index=False)
    print(f'Validated data saved to {validated_output}')
    total_emissions = data['Total_Emissions'].sum()
    print(f'Total emissions across all entries: {total_emissions}')
else:
    print(f'Error: Input file {input_file} not found. Please ensure the file is present in the directory.')

# Create reduction opportunity matrix
reduction_opportunities = pd.DataFrame({
    'Category': ['Fleet Optimization', 'Energy Efficiency', 'Renewable Energy'],
    'Potential_Reduction_tCO2e': [500, 800, 1200],
    'Estimated_Investment_USD': [100000, 200000, 300000]
})
reduction_opportunities.to_excel(reduction_output, index=False)
print(f'Reduction opportunities matrix created and saved to {reduction_output}')

# Create Excel data collection template
if not os.path.exists(input_file):
    data_template = pd.DataFrame({
        'Source': [],
        'Scope_1': [],
        'Scope_2': [],
        'Scope_3': [],
        'Notes': []
    })
    data_template.to_excel(template_output, index=False)
    print(f'Excel data collection template created and saved to {template_output}')
else:
    print(f'Skipped template creation since {input_file} already exists.')
