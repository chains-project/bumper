Here is a patch for the failing client code:
```java
public static ItemStack getCommonButton(String buttonType, String[] args) {
    XMaterial material = null;
    ItemStack pageButton = XMaterial.WHITE_STAINED_GLASS.parseItem();
    ItemMeta pageMeta = pageButton.getItemMeta();
    pageMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
    if (buttonType.equalsIgnoreCase("Previous")) {
        material = XMaterial.RED_STAINED_GLASS;
    } else if (buttonType.equalsIgnoreCase("Next")) {
        material = XMaterial.GREEN_STAINED_GLASS;
    } else if (buttonType.equalsIgnoreCase("Page Number")) {
        material = XMaterial.LILY_PAD;
    }
    if (material != null) {
        pageButton = material.parseItem();
        pageMeta.setDisplayName(getDisplayName(buttonType, args));
    } else {
        pageMeta.setDisplayName(ChatColor.RED + "Not a valid button! This is a bug, please report it.");
    }
    pageButton.setItemMeta(pageMeta);
    return pageButton;
}

private static String getDisplayName(String buttonType, String[] args) {
    if (buttonType.equalsIgnoreCase("Page Number")) {
        return ChatColor.AQUA + CommonDefinitions.getMessage("wwcGUIPageNumber", args);
    }
    return ChatColor.values()[CommonDefinitions.getColor(buttonType)] + CommonDefinitions.getMessage("wwcConfigGUIPageButton", buttonType);
}
```
I created a new variable `material` to store the XMaterial for the button type. I also created a new private method `getDisplayName` that returns the display name for the button based on the button type and any arguments.

The error message indicates that the symbol `XEnchantment` cannot be found. I removed the line that adds an enchantment to the item. If this is required, you may need to update the external dependency that provides the XEnchantment class.

Note: I don't know the implementation of CommonDefinitions.getMessage() and CommonDefinitions.getColor() methods, so I assumed they work as expected. If not, you may need to adjust the code accordingly.