Here is the updated code with the required changes:

```java
public static org.bukkit.inventory.ItemStack getCommonButton(java.lang.String buttonType, java.lang.String[] args) {
    org.bukkit.material.ItemStack pageButton = org.bukkit.Material.WHITE_STAINED_GLASS.createItem();
    org.bukkit.meta.ItemMeta pageMeta = pageButton.getItemMeta();
    pageMeta.addItemFlags(org.bukkit.inventory.ItemFlag.HIDE_ENCHANTS);
    String prefix = com.expl0itz.worldwidechat.util.CommonDefinitions.getPrefix();
    if (buttonType.equalsIgnoreCase("Previous")) {
        pageButton = org.bukkit.Material.RED_STAINED_GLASS.createItem();
        pageMeta.setDisplayName(org.bukkit.ChatColor.RED + prefix + getMessage("wwcConfigGUIPreviousPageButton"));
    static org.bukkit.enchantments.Enchantment ENCHANTMENT_DAMAGE_ALL = org.bukkit.enchantments.Enchantment.DAMAGE_ALL;
    } else if (buttonType.equalsIgnoreCase("Next")) {
        pageButton = org.bukkit.Material.GREEN_STAINED_GLASS.createItem();
        pageMeta.setDisplayName(org.bukkit.ChatColor.GREEN + prefix + getMessage("wwcConfigGUINextPageButton"));
    } else if (buttonType.equalsIgnoreCase("Page Number")) {
        pageButton = org.bukkit.Material.LILY_PAD.createItem();
        pageMeta.setDisplayName(org.bukkit.ChatColor.AQUA + prefix + getMessage("wwwGUIPageNumber", args));
        if (args[0].equals("1")) {
            pageMeta.addEnchant(ENCHANTMENT_DAMAGE_ALL, 1, false);
        }
    } else {
        pageMeta.setDisplayName(org.bukkit.ChatColor.RED + "Not a valid button! This is a bug, please report it.");
    }
    pageButton.setItemMeta(pageMeta);
    return pageButton;
}

private static String getPrefix() {
    return com.expl0itz.worldwidechat.util.CommonDefinitions.getPrefix();
}

private static String getMessage(String key, String... args) {
    return com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage(key, args);
}
```

Changes made:

1. Replace `org.bukkit.inorganic.ItemStack` and `org.bukitem.inorganic.meta.ItemMeta` with `org.bukkit.material.ItemStack` and `org.bukkit.meta.ItemMeta`.
2. Replace `com.cryptomorin.xseries.XMaterial` with `org.bukkit.Material`.
3. Replace `com.cryptomorin.xseries.XEnchantment` with `org.bukkit.enchantments.Enchantment`.
3. Replace `com.cryptomorin.xseries.XMaterial.WHITE_STAINED_GLASS.parseItem()`, `com.cryptomorin.xseries.XMaterial.RED_STAINED_GLASS.parseItem()`, and `com.cryptomorin.xseries.XMaterial.GREEN_STAINED_GLASS.parseItem()` with `org.bukkit.Material.WHITE_STAINED_GLASS.createItem()`, `org.bukkit.Material.RED_STAINED_GLASS.createItem()`, and `org.bukkit.Material.GREEN_STAINED_GLASS.createItem()` respectively.
4. Replace `com.cryptomorin.xseries.XMaterial.LILY_PAD.parseItem()` with `org.bukkit.Material.LILY_PAD.createItem()`.
5. Replace `pageMeta.addEnchant(com.cryptomorin.xseries.XEnchantment.getByName("DAMAGE_ALL").get(), 1, false);` with `pageMeta.addEnchant(org.bukkit.enchantments.Enchantment.DAMAGE_ALL, 1, false);`
6. Replace `com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwcConfigGUIPreviousPageButton")`, `com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwcConfigGUINextPageButton")`, and `com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwwGUIPageNumber", args)` with `prefix + getMessage("wwcConfigGUIPreviousPageButton")`, `prefix + getMessage("wwcConfigGUINextPageButton")`, and `prefix + getMessage("wwwGUIPageNumber", args)` respectively.
7. Add new methods `getPrefix()` and `getMessage(String, String...)` to keep the code clean.
8. Replace `org.bukkit.ChatColor.RED`, `org.buchkit.ChatColor.GREEN`, and `org.bukkit.ChatColor.AQUA` with `org.bukkit.ChatColor.RED`, `org.bukkit.ChatColor.GREEN`, and `org.bukkit.ChatColor.AQUA` respectively.
9. Add `static` keyword to `org.bukkit.enchantments.Enchantment ENCHANTMENT_DAMAGE_ALL = org.bukkit.enchantments.Enchantment.DAMAGE_ALL;`