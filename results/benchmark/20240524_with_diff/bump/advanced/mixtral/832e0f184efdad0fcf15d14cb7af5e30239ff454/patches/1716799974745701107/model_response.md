Here's the updated method with the necessary changes to fix the error:

```java
public static org.bukkit.inventory.ItemStack getCommonButton(java.lang.String buttonType, java.lang.String[] args) {
    org.bukkit.inventory.ItemStack pageButton = java.util.Objects.requireNonNull(com.cryptomorin.xseries.XMaterial.WHITE_STAINED_GLASS.parseItem());
    org.bukkit.inventory.meta.ItemMeta pageMeta = pageButton.getItemMeta();
    pageMeta.addItemFlags(org.bukkit.inventory.ItemFlag.HIDE_ENCHANTS);
    if (buttonType.equalsIgnoreCase("Previous")) {
        pageButton = java.util.Objects.requireNonNull(com.cryptomorin.xseries.XMaterial.RED_STAINED_GLASS.parseItem());
        pageMeta.setDisplayName(org.bukkit.ChatColor.RED + com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwcConfigGUIPreviousPageButton"));
    } else if (buttonType.equalsIgnoreCase("Next")) {
        pageButton = java.util.Objects.requireNonNull(com.cryptomorin.xseries.XMaterial.GREEN_STAINED_GLASS.parseItem());
        pageMeta.setDisplayName(org.bukkit.ChatColor.GREEN + com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwcConfigGUINextPageButton"));
    } else if (buttonType.equalsIgnoreCase("Page Number")) {
        pageButton = java.util.Objects.requireNonNull(com.cryptomorin.xseries.XMaterial.LILY_PAD.parseItem());
        pageMeta.setDisplayName(org.bukkit.ChatColor.AQUA + com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwcGUIPageNumber", args));
        if (args[0].equals("1")) {
            pageMeta.addEnchant(com.cryptomorin.xseries.XEnchantment.matchXEnchantment("power").get(), 1, false);
        }
    } else {
        pageMeta.setDisplayName(org.bukkit.ChatColor.RED + "Not a valid button! This is a bug, please report it.");
    }
    pageButton.setItemMeta(pageMeta);
    return pageButton;
}
```

The main change is the replacement of `parseEnchantment()` with `get()` in the `com.cryptomorin.xseries.XEnchantment.matchXEnchantment("power").get()` line. This should fix the error.