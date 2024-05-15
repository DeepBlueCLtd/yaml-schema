# yaml-schema

Demonstrator for schema-controlled editing of YAML documents in VS-code

## 1. Objective

The objective of this investigation is to enable VS-Code to provide model designers with support in generating valid code, bringing these benefits:
- quicker development through user support and fewer defects in model data-files
- better quality (compliant) model data-files

See the schema controlled data editing below:
![screencast](./images/vs-code-yaml.gif)

The adoption of Schemas for modelling data files brings these benefits:
- simplify (reduce) validation code required with models
- more robust data validation, handled by mature codebases
- versioned schemas track and document chanding model APIs
- make dat exchange with 3rd parties more robust
- assist generation of compliant data-files, either via 3rd parties or AI

## 2. Create the schema

From a previous project we have this JSON schema:

![Structure of JSON schema for validation](./images/Default%20Schema%20Structure.png)

One thing important is that some of properties like propertyOrder will be ignored in new schema json.

The full documentation of JSON-schema is here: https://json-schema.org/

## 3. Let a YAML file declare schema to use

Create the yaml data matching the `missile.schema.json`:

![missilte-strike.yaml](./images/yaml.png)

Adding this line to the start of the file associates it with that schema, to assist in developing the document - including validation.

```yaml
# yaml-language-server: $schema=schemas/schema.json
```

## 4. Configure VS-Code to associate filename patterns with schemas.

Another way is to specify this association in settings.json, for the YAML extension.

First, install the `YAML` extension:

![yaml extension](./images/yaml%20extension.png)

Second, configure `YAML` extension settings:

![yaml extension settings](./images/extension%20settings.png)

And then go to settings.json (note: this can be at the user level or at the workspace level. For the latter, put the `settings.json` into a `vscode` folder in the workspace root folder).

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
    "./schemas/missile.schema.json": "*.missile.yaml",
    "./schemas/tank.schema.json": "*.tank.yaml"
  }
  //
}
```

## 5. Validate the yaml file using python

1. pip install pyyaml
2. pip install jsonschema

python .\validate_yaml.py [`yaml file`] [`schema json file`]

```shell
python .\validate_yaml.py missile-strike.yaml ./schemas/schema.json
```

![result](./images/result.png)

