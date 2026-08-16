import maya.cmds as cmds


def create_pipeline_menu():
    menu_name = "Pipeline Tools"

    # Remove existing menu if it already exists
    if cmds.menu(menu_name, exists=True):
        cmds.deleteUI(menu_name)

    # Create main Pipeline Tools menu
    cmds.menu(menu_name, label="Pipeline Tools", parent="MayaWindow", tearOff=True)

    # =========================================================
    # Modeling Tools
    # =========================================================

    modeling_menu = cmds.menuItem(label="Modeling Tools", subMenu=True)
    cmds.menuItem(label="Asset Review Tool", parent=modeling_menu, annotation="Review model from multiple views", command="import asset_review; asset_review.show()")
    cmds.menuItem(label="UV Export Tool", parent=modeling_menu, annotation="Clean duplicate UVs and export", command="import uv_export; uv_export.show()")

    # =========================================================
    # Cleanup Tools
    # =========================================================

    cleanup_menu = cmds.menuItem(label="Cleanup Tools", subMenu=True)

    cmds.menuItem(label="Remove Unused Nodes", parent=cleanup_menu, annotation="Remove unused nodes from the scene", command="import remove_unused_nodes; remove_unused_nodes.remove_unused_nodes()")
    cmds.menuItem(label="Remove Unused Plugins", parent=cleanup_menu, annotation="Find and unload unused plugins", command="import remove_unused_plugins; remove_unused_plugins.remove_unused_plugins()")

    # Separator
    cmds.separator(parent=menu_name)

    # About option
    cmds.menuItem(label="About Pipeline Tools", parent=menu_name, command='print("Maya Pipeline Tools")')
    print("Pipeline Tools menu created successfully :)")


create_pipeline_menu()