# yaml-schema

Demonstrator for schema-controlled editing of YAML documents in VS-code

## 1. Create the schema

Create `missile.schema.json`.

The default and valid schema json file have below structure.
![Structure of JSON schema for validation](./images/Default%20Schema%20Structure.png)

One thing important is that some of properties like propertyOrder will be ignored in new schema json.

`https://json-schema.org/`
You can see the full documentation of JSON-schema here.

## 2. Let a YAML file declare schema to use

Create the example yaml data consulting the `schema.json` which is the result of converting original schema json - `missile-strike.schema.json`

![missilte-strike.yaml](./images/yaml.png)

At the begining of yaml file by adding this line, we can easily validate the yaml file against to schema.json

```yaml
# yaml-language-server: $schema=schemas\schema.json
```

## 3. Configure VS-Code to associate filename patterns with schemas.

Another way, is to specify settings.json for YAML extension
Specify schema in VScode.

How to configure VS-Code to know which schema to use?

First, install `YAML` extension:

![yaml extension](./images/yaml%20extension.png)

Second, configure `YAML` extension settings:


![yaml extension settings](./images/yaml%20extension.png)

And then go to settings.json (note: this can be at the user level or at the workspace level. For the latter, put the `settings.json` into a `vscode` folder in the workspace root folder.

![settings.json](./images/settings.png)

In `settings.json` define `yaml.schemas`

```json
{
  "workbench.colorTheme": "Default Dark Modern",
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.tabSize": 2,
  "git.confirmSync": false,
  "git.enableSmartCommit": true,
  "explorer.confirmDelete": false,
  "javascript.updateImportsOnFileMove.enabled": "never",
  "explorer.confirmDragAndDrop": false,
  "redhat.telemetry.enabled": true,
  "yaml.format.singleQuote": true,
  // define schema of yaml file
  "yaml.schemas": {
    "./schemas/schema.json": "missile-strike.yaml"
  }
  //
}
```

## 4. Validate the yaml file using python

1. pip install pyyaml
2. pip install jsonschema

python .\validate_yaml.py [`yaml file`] [`schema json file`]

```shell
python .\validate_yaml.py missile-strike.yaml ./schemas/schema.json
```

![result](./images/result.png)

