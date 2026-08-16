# Maya_Shelf_Menu_Tools

# Maya Shelf, Menu & Environment Setup

A simple Maya pipeline setup that automatically loads custom **menus, shelves, and pipeline tools** when Maya starts.

## Features

* Custom Pipeline Tools menu
* Organized tool categories and submenus
* Custom Maya shelf with tool icons
* Automatic startup using `userSetup.py`
* Environment configuration using `Maya.env`
* Supports Windows and Linux

## Project Structure

```text
maya-shelf-menu-setup/
│
├── README.md
├── menu_setup.py
├── shelf_PipelineTools.mel
├── userSetup.py
│
├── env/
│   ├── Maya.env.windows
│   └── Maya.env.linux
│
└── icons/
    ├── assetReview.png
    ├── uvExport.png
    ├── unusedNodes.png
    └── unusedPlugins.png
```

## Setup Flow

```text
Maya Launch
     ↓
Maya.env
     ↓
Set Pipeline Paths
     ↓
userSetup.py
     ↓
Load Menu + Shelf
     ↓
Pipeline Tools Ready
```

## Files

### `Maya.env`

Defines environment variables used by the pipeline.

Example:

```text
MAYA_SCRIPT_PATH=/mnt/pipeline/maya/scripts
PYTHONPATH=/mnt/pipeline/maya
PIPELINE_TOOLS=/mnt/pipeline/maya
```

### `userSetup.py`

Runs during Maya startup and initializes the pipeline environment by loading the custom menu and shelf.

### `menu_setup.py`

Creates the **Pipeline Tools** menu and organizes tools into categories such as:

```text
Pipeline Tools
├── Modeling Tools
│   ├── Asset Review Tool
│   └── UV Export Tool
│
└── Cleanup Tools
    ├── Remove Unused Nodes
    └── Remove Unused Plugins
```

### `shelf_PipelineTools.mel`

Creates a custom Maya shelf with buttons and icons for quick access to pipeline tools.

## Environment Paths

### Windows

```text
C:\Users\<username>\Documents\maya\<version>\Maya.env
```

Example:

```text
MAYA_SCRIPT_PATH=C:\PipelineTools\maya\scripts
PYTHONPATH=C:\PipelineTools\maya
PIPELINE_TOOLS=C:\PipelineTools\maya
```

### Linux

```text
/home/<username>/maya/<version>/Maya.env
```

Example:

```text
MAYA_SCRIPT_PATH=/mnt/pipeline/maya/scripts
PYTHONPATH=/mnt/pipeline/maya
PIPELINE_TOOLS=/mnt/pipeline/maya
```

## Requirements

* Autodesk Maya
* Python
* Maya `cmds`
* Required pipeline tool modules
* Valid pipeline paths
