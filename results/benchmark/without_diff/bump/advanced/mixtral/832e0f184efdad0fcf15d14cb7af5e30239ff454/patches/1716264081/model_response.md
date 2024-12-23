Here's the fixed method with the error resolved:

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
            try {
                pageMeta.addEnchant(getXEnchantment("power"), 1, false);
            } catch (IllegalArgumentException e) {
                e.printStackTrace();
            }
        }
    } else {
        pageMeta.setDisplayName(org.bukkit.ChatColor.RED + "Not a valid button! This is a bug, please report it.");
    }
    pageButton.setItemMeta(pageMeta);
    return pageButton;
}

private static org.bukkit.enchantments.Enchantment getXEnchantment(String enchantmentName) {
    for (org.bukkit.enchantments.Enchantment enchantment : org.bukkit.enchantments.Enchantment.values()) {
        if (enchantment.getName().equalsIgnoreCase(enchantmentName)) {
            return enchantment;
        }
    }
    throw new IllegalArgumentException("Invalid enchantment name: " + enchantmentName);
}
```

I have created a new private method `getXEnchantment` to get the `org.bukkit.enchantments.Enchantment` instance by its name. This way, we avoid using the removed `parseEnchantment()` method from `com.cryptomorin.xseries.XEnchantment`.