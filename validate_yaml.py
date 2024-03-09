import json
import yaml
import jsonschema
import argparse

def validate_yaml(yaml_file, schema_file):
    # Load the JSON schema
    with open(schema_file, 'r') as schema_file:
        schema = json.load(schema_file)

    # Load the YAML file to validate
    with open(yaml_file, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)

    # Validate the YAML data against the JSON schema
    try:
        jsonschema.validate(instance=data, schema=schema)
        print("Validation successful: The YAML file is valid against the schema.")
    except jsonschema.exceptions.ValidationError as e:
        print("Validation error: The YAML file is not valid against the schema.")
        print(e)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Validate a YAML file against a JSON schema.')
    parser.add_argument('yaml_file', help='Path to the YAML file for validation')
    parser.add_argument('schema_file', help='Path to the JSON schema file')
    args = parser.parse_args()
    
    validate_yaml(args.yaml_file, args.schema_file)
