```java
public static ItemStack getCommonButton(String buttonType, String[] args) {
    ItemStack pageButton = XMaterial.WHITE_STAINED_GLASS.parseItem();
    ItemMeta pageMeta = pageButton.getItemMeta();
    pageMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
    if (buttonType.equalsIgnoreCase("Previous")) {
        pageButton = XMaterial.RED_STAINED_GLASS.parseItem();
        pageMeta.setDisplayName(ChatColor.RED
                + CommonDefinitions.getMessage("wwcConfigGUIPreviousPageButton"));
    } else if (buttonType.equalsIgnoreCase("Next")) {
        pageButton = XMaterial.GREEN_STAINED_GLASS.parseItem();
        pageMeta.setDisplayName(ChatColor.GREEN
                + CommonDefinitions.getMessage("wwcConfigGUINextPageButton"));
    } else if (buttonType.equalsIgnoreCase("Page Number")) {
        pageButton = XMaterial.LILY_PAD.parseItem();
        pageMeta.setDisplayName(ChatColor.AQUA
                + CommonDefinitions.getMessage("wwcGUIPageNumber", args));
        if (args[0].equals("1")) {
            Enchantment enchantment = XEnchantment.matchXEnchantment("power").get().parseEnchantment();
            pageMeta.addEnchant(enchantment, 1, false);
        }
    } else {
        pageMeta.setDisplayName(ChatColor.RED + "Not a valid button! This is a bug, please report it.");
    }
    
    pageButton.setItemMeta(pageMeta);
    return pageButton;
}
```
In the new version of the library, the method `parseEnchantment()` is not available. Instead, the `get()` method is used to get the enchantment. Then, the enchantment is added to the `ItemMeta`.