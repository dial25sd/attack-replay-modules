# Attack Replay Modules

Collection of modules & metadata for the Attack Replay Framework.

## Disclaimer
Even though this repo only contains a curated collection of modules for usage with the Attack Replay Framework, side effects may occur and potentially impact target systems.

## Folder Structure 
ARF can handle modules from Metasploit Framework (MSF) as well as standalone (dockerized) modules.

```
.
├── modules/
│   ├── exploits/
│   │   ├── EXPLOIT-1-MSF/
│   │   │   └── module_data_msf.yml
│   │   ├── EXPLOIT-2-STANDALONE/
│   │   │   ├── module_data_standalone.yml
│   │   │   ├── Dockerfile
│   │   │   ├── poc.py
│   │   │   └── requirements.txt
│   │   │       ...
│   ├── param_scanner/
│   │   └── PARAM-SCANNER-1
│   │       ...
│   ├── plausibility_checks/
│   │   └── PLAUSIBILITY-CHECK-1
│   │       ...
│   └── vuln_scanner/
│       └── VULN-SCANNER-1
│           ...
└── vulns/
    ├── vuln_cve-1234-5678.yml
    └── ...
```

### `modules` directory
A module in this repo is only recognized by the Attack Replay Framework if it contains a valid `.yml` file with module data.  
This file needs to be placed in the very same folder as the module's resources and its name needs to start with `module_`.
Only **one** `.yml` file per directory allowed.  

Samples for such files can be retrieved from `attack-replay/data_templates/`.   
Be aware of the different module data requirements for _MSF_ and _standalone_ modules:
 - directories for _MSF_ modules must not contain any resources apart from the `.yml` file.
 - directories for _standalone_ modules need to contain **exactly one** `Dockerfile` and might contain any additional resources such as scripts or other requirements.

### `vulns` directory
While `.yml` files in the `modules` directory each represent a single module, a `.yml` file in `vulns` can represent one or more vulnerabilities.  
This file is used to assign the modules specified earlier to one or more vulnerabilities.  
Samples can be found in the same location as for modules.

# Extension
- Make sure to only ever use non-intrusive modules in order to comply with the Attack Replay Framework requirements.
- templates for all kinds of metadata files can be found in `data_templates/`.

## Add a new vuln
1. Write the metadata file or edit an existing one/the template accordingly.
1. Save it in the `vulns/` directory.

## Add a new ARF module

### 1. Get a Module from a trusted source
Try to only ever use modules from trusted sources or make sure you have carefully reviewed the source code.

Try eg:  
 - Search Metasploit
 - Search Exploit DB
 - diverse GitHub repose

### 2. Categorize
Categorize the new module and create a new folder in the appropriate directory  
*For standalone modules:* copy the script/executable and other potentially required dependencies to this folder

### 3. Dockerize it
*only required for standalone (non-MSF) modules!*

1. make the module executable inside a docker container: needed parameters will be provided using environment variables
2. save the Dockerfile in the modules directory

### 4. Specify the Module Metadata
- specify the module metadata accordingly
- make sure the parameter names match the ones used in the Dockerfile / by Metasploit

### 5. Use it!
- feed the framework with events that trigger your module and watch it go brrrr