Here's the updated method with the changes required to fix the error:

```java
public static org.bukkit.inventory.ItemStack getCommonButton(java.lang.String buttonType, java.lang.String[] args) {
    org.bukkit.inventory.ItemStack pageButton = com.cryptomorin.xseries.XMaterial.WHITE_STAINED_GLASS.parseItem();
    org.bukkit.inventory.meta.ItemMeta pageMeta = pageButton.getItemMeta();
    pageMeta.addItemFlags(org.bukkit.inventory.ItemFlag.HIDE_ENCHANTS);
    if (buttonType.equalsIgnoreCase("Previous")) {
        pageButton = com.cryptomorin.xseries.XMaterial.RED_STAINED_GLASS.parseItem();
        pageMeta.setDisplayName(org.bukkit.ChatColor.RED + com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwcConfigGUIPreviousPageButton"));
    } else if (buttonType.equalsIgnoreCase("Next")) {
        pageButton = com.cryptomorin.xseries.XMaterial.GREEN_STAINED_GLASS.parseItem();
        pageMeta.setDisplayName(org.bukkit.ChatColor.GREEN + com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwcConfigGUINextPageButton"));
    } else if (buttonType.equalsIgnoreCase("Page Number")) {
        pageButton = com.cryptomorin.xseries.XMaterial.LILY_PAD.parseItem();
        pageMeta.setDisplayName(org.bukkit.ChatColor.AQUA + com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwcGUIPageNumber", args));
        if (args[0].equals("1")) {
            pageMeta.addEnchant(getXEnchantment("power"), 1, false);
        }
    } else {
        pageMeta.setDisplayName(org.bukkit.ChatColor.RED + "Not a valid button! This is a bug, please report it.");
    }
    pageButton.setItemMeta(pageMeta);
    return pageButton;
}

private static org.bukkit.enchantments.Enchantment getXEnchantment(java.lang.String enchantmentName) {
    for (org.bukkit.enchantments.Enchantment enchantment : org.bukkit.enchantments.Enchantment.values()) {
        if (enchantment.getName().equalsIgnoreCase(enchantmentName)) {
            return enchantment;
        }
    }
    return null;
}
```

The changes include adding a new private method `getXEnchantment` that returns the corresponding `Enchantment` object by its name. This method replaces the usage of `com.cryptomorin.xseries.XEnchantment.matchXEnchantment("power").get().parseEnchantment()` that is no longer available in the new library version.