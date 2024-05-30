Here is the patched method:

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
            pageMeta.addEnchant(java.util.Objects.requireNonNull(com.cryptomorin.xseries.XEnchantment.matchXEnchantment("power").orElseThrow(NullPointerException::new)).getBukkitEnchantment(), 1, false);
        }
    } else {
        pageMeta.setDisplayName(org.bukkit.ChatColor.RED + "Not a valid button! This is a bug, please report it.");
    }
    pageButton.setItemMeta(pageMeta);
    return pageButton;
}
```

The changes I made:

* Replaced the removed `parseEnchantment()` method with a call to `getBukkitEnchantment()` on the `XEnchantment` object returned by `matchXEnchantment("power")`.
* Wrapped the call to `matchXEnchantment()` in `Objects.requireNonNull()` to handle the case where the method returns `null`.
* Wrapped the call to `Objects.requireNonNull()` in `orElseThrow()` to throw a `NullPointerException` if `matchXEnchantment()` returns `null`.
* Added a `NullPointerException` as an argument to `orElseThrow()`.

These changes allow the code to work with the new library version.