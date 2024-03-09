# yaml-schema

Demonstrator for schema-controlled editing of YAML documents in VS-code

1. Create `schema.json`.
   We have to convert `missile-strike.schema.json` to valid schema json which we can use in our VS-code to validate `yaml` file. The `missile-strike.schema.json` is for previous project form.

The default and valid schema json file have below structure.
![Structure of JSON schema for validation](./images/Default%20Schema%20Structure.png)

One thing important is that some of properties like propertyOrder will be ignored in new schema json.

`https://json-schema.org/`
You can see the full documentation of JSON-schema here.

2. Create the example yaml data consulting the `schema.json` which is the result of converting original schema json - `missile-strike.schema.json`

![missilte-strike.yaml](./images/yaml.png)

Specify schema in VScode.

How to configure VS-Code to know which schema to use?

First, install `YAML` extension
![yaml extension](./images/yaml%20extension.png)

Second, configure
