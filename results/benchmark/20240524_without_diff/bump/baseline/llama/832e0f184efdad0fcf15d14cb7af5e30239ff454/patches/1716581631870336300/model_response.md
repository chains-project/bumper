```java
public static ItemStack getCommonButton(String buttonType, String[] args) {
    ItemStack pageButton;
    ItemMeta pageMeta;
    if (buttonType.equalsIgnoreCase("Previous")) {
        pageButton = XMaterial.RED_STAINED_GLASS.parseItem();
        pageMeta = pageButton.getItemMeta();
        pageMeta.setDisplayName(ChatColor.RED + CommonDefinitions.getMessage("wwcConfigGUIPreviousPageButton"));
    } else if (buttonType.equalsIgnoreCase("Next")) {
        pageButton = XMaterial.GREEN_STAINED_GLASS.parseItem();
        pageMeta = pageButton.getItemMeta();
        pageMeta.setDisplayName(ChatColor.GREEN + CommonDefinitions.getMessage("wwcConfigGUINextPageButton"));
    } else if (buttonType.equalsIgnoreCase("Page Number")) {
        pageButton = XMaterial.LILY_PAD.parseItem();
        pageMeta = pageButton.getItemMeta();
        pageMeta.setDisplayName(ChatColor.AQUA + CommonDefinitions.getMessage("wwcGUIPageNumber", args));
        if (args[0].equals("1")) {
            pageMeta.addEnchant(Enchantment.DURABILITY, 1, false);
        }
    } else {
        pageButton = XMaterial.WHITE_STAINED_GLASS.parseItem();
        pageMeta = pageButton.getItemMeta();
        pageMeta.setDisplayName(ChatColor.RED + "Not a valid button! This is a bug, please report it.");
    }
    pageMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
    pageButton.setItemMeta(pageMeta);
    return pageButton;
}
```