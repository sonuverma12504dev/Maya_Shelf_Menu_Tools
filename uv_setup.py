import os
import sys
import maya.cmds as cmds


# ------------------------------------------------------------
# Pipeline Tools Path
# ------------------------------------------------------------

PIPELINE_PATH = os.path.dirname(__file__)

if PIPELINE_PATH not in sys.path:
    sys.path.append(PIPELINE_PATH)


# ------------------------------------------------------------
# Load Pipeline Menu
# ------------------------------------------------------------

try:
    import menu_setup
    menu_setup.create_pipeline_menu()

except Exception as e:
    print("Failed to load Pipeline Tools Menu: {}".format(e))


# ------------------------------------------------------------
# Load Pipeline Shelf
# ------------------------------------------------------------

def load_pipeline_shelf():
    """
    Load the Pipeline Tools shelf from the MEL file.
    """

    shelf_file = os.path.join(PIPELINE_PATH, "shelf_PipelineTools.mel")
    if os.path.exists(shelf_file):
        try:
            cmds.mel.eval('source "{}";'.format(shelf_file.replace("\\", "/")))
            print("Pipeline Tools shelf loaded successfully.")
        except Exception as e:
            print("Failed to load Pipeline Tools shelf: {}".format(e))
    else:
        print("Shelf file not found: {}".format(shelf_file))


load_pipeline_shelf()

print("Pipeline Tools initialized successfully.")