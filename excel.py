import pandas as pd

# Function to generate rows with specific configurations
def generate_rows_with_configurations(configurations):
    all_rows = []
    for config in configurations:
        base_data = config["base_data"]
        entries = config["entries"]
        for entry in entries:
            row = base_data.copy()
            row.update(entry)
            # Check where to get the template from (entry or base_data) for "name" construction
            template = entry.get("template") or base_data.get("template", "Default Template")
            row["name"] = f'{entry["id"]} - {template}'
            all_rows.append(row)
    return all_rows

# Example configuration for the first set of data
config1 = {
    "base_data": {
        "project": "ProjectName1",
        "queue": "QueueType1",
        "template": "TemplateName1",
        "start": "YYYY-MM-DDTHH:MM:SS.000Z",
        "due": "YYYY-MM-DDTHH:MM:SS.000Z",
        "zone": "Zone1",
    },
    "entries": [
        {"index": 1, "id": 1001},
        {"index": 2, "id": 1002},
        {"index": 3, "id": 1003},
    ]
}

# Example configuration for the second set of data
config2 = {
    "base_data": {
        "project": "ProjectName2",
        "queue": "QueueType2",
        "template": "TemplateName2",
        "start": "YYYY-MM-DDTHH:MM:SS.000Z",
        "due": "YYYY-MM-DDTHH:MM:SS.000Z",
        "zone": "Zone2",
    },
    "entries": [
        {"index": 4, "id": 2001},
        {"index": 5, "id": 2002},
        {"index": 6, "id": 2003},
    ]
}

# Additional index-ID pairs requiring the same set of templates
additional_pairs = [
    {"index": 7, "id": 3001},
    {"index": 8, "id": 3002},
    # Add more pairs as needed
]

# Define the templates for config3
templates = [
    "Template A",
    "Template B",
    "Template C",
    # Add more templates as needed
]

# Configuration for the third set of data with multiple templates
config3 = {
    "base_data": {
        "project": "ProjectName3",
        "queue": "QueueType3",
        "start": "YYYY-MM-DDTHH:MM:SS.000Z",
        "due": "YYYY-MM-DDTHH:MM:SS.000Z",
        "zone": "Zone3",
    },
    "entries": []
}

# Populate the entries list within config3 for each index-ID pair and template combination
for pair in additional_pairs:
    for template in templates:
        config3["entries"].append({
            "index": pair["index"],
            "id": pair["id"],
            "template": template,
        })

# Combine all configurations into a list
configurations = [config1, config2, config3]

# Generate the rows with specific configurations
all_rows = generate_rows_with_configurations(configurations)

# Convert to DataFrame and specify column order
df = pd.DataFrame(all_rows)
column_order = ["index", "project", "queue", "template", "name", "start", "due", "id", "zone"]
df = df[column_order]

# Save to CSV
df.to_csv("output_combined.csv", index=False)
