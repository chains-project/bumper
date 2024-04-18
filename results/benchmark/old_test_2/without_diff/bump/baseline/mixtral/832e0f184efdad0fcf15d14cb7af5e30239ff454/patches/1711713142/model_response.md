Here's a proposed patch for the given code. It replaces the usage of the `XMaterial` class, which appears to have been removed, with the `Material` class and the `ItemStack` constructor. It also uses `Enchantment.getByName` instead of `XEnchantment.matchXEnchantment`.

```java
public static ItemStack getCommonButton(String buttonType, String[] args) {
    ItemStack pageButton = new ItemStack(Material.WHITE_STAINED_GLASS);
    ItemMeta pageMeta = pageButton.getItemMeta();
    pageMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
    if (buttonType.equalsIgnoreCase("Previous")) {
        pageButton = new ItemStack(Material.RED_STAINED_GLASS);
        pageMeta.setDisplayName(ChatColor.RED
                + CommonDefinitions.getMessage("wwcConfigGUIPreviousPageButton"));
    } else if (buttonType.equalsIgnoreCase("Next")) {
        pageButton = new ItemStack(Material.GREEN_STAINED_GLASS);
        pageMeta.setDisplayName(ChatColor.GREEN
                + CommonDefinitions.getMessage("wwcConfigGUINextPageButton"));
    } else if (buttonType.equalsIgnoreCase("Page Number")) {
        pageButton = new ItemStack(Material.LILY_PAD);
        pageMeta.setDisplayName(ChatColor.AQUA
                + CommonDefinitions.getMessage("wwcGUIPageNumber", args));
        if (args[0].equals("1")) {
            pageMeta.addEnchant(Enchantment.getByName("DAMAGE_ALL").get(), 1, false);
        }
    } else {
        pageMeta.setDisplayName(ChatColor.RED + "Not a valid button! This is a bug, please report it.");
    }

    pageButton.setItemMeta(pageMeta);
    return pageButton;
}
```

This code should fix the "cannot find symbol" error caused by the missing `XMaterial` class, and it should work as long as the `Material`, `ItemMeta`, `ItemFlag`, `ChatColor`, `CommonDefinitions`, and `Enchantment` classes are still available.