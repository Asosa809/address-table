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

# Configuration for the first set of data
config1 = {
    "base_data": {
        "project": "CSG1-Robin-Retrofit-2024-slKivaA02",
        "queue": "AR FSS - v2",
        "template": "Perimeter Safety Controller Workscope",
        "start": "2024-03-04T12:00:00.000Z",
        "due": "2024-07-05T23:59:00.000Z",
        "zone": "slKivaA02",
    },
    "entries": [
        {"index": 45, "id": 2330},
        {"index": 64, "id": 2375},
        {"index": 32, "id": 2155},
    ]
}

# Configuration for the second set of data with different queue, template, etc.
config2 = {
    "base_data": {
        "project": "CSG1-Robin-Retrofit-2024-slKivaA02",
        "queue": "AR Perimeter Guard - v2",
        "template": "Swing Gate Workscope",
        "start": "2024-08-01T00:00:00.000Z",
        "due": "2024-12-31T23:59:00.000Z",
        "zone": "slKivaA02",
    },
    "entries": [
        {"index": 48, "id": 2335},
        {"index": 31, "id": 2154},
        {"index": 63, "id": 2374},
    ]
}

# Additional index-ID pairs requiring the same set of seven templates
additional_pairs = [
    {"index": 25, "id": 2143},
    {"index": 26, "id": 2145},
    {"index": 27, "id": 2147},
    {"index": 28, "id": 2149},
    {"index": 29, "id": 2151},
    {"index": 33, "id": 2156},
    {"index": 35, "id": 2303},
    {"index": 36, "id": 2307},
    {"index": 41, "id": 2318},
    {"index": 42, "id": 2322},
    {"index": 52, "id": 2342},
    {"index": 53, "id": 2348},
    {"index": 59, "id": 2362},
    {"index": 60, "id": 2366},
]

# Define the seven different templates for config3
templates = [
    "100. Robin",
    "200. Robin",
    "300. Robin",
    "400. Robin",
    "500. Robin",
    "600. Robin",
    "700. Robin",
]

# Configuration for the third set of data with multiple templates
config3 = {
    "base_data": {
        "project": "CSG1-Robin-Retrofit-2024-slKivaA02",
        "queue": "AR Stations - v2",
        "start": "2024-03-04T12:00:00.000Z",
        "due": "2024-07-05T23:59:00.000Z",
        "zone": "slKivaA02",
    },
    "entries": []
}

# Populate the entries list within config3 for each index-ID pair and template combination
for pair in [{"index": 24, "id": 2141}] + additional_pairs:
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

