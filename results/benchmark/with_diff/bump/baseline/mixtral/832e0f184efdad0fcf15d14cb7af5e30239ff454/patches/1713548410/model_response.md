Here's the fixed version of the `getCommonButton` method:

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
            pageMeta.addEnchant(Enchantment.getEnchantment(XEnchantment.POWER.getID()), 1, false);
        }
    } else {
        pageMeta.setDisplayName(ChatColor.RED + "Not a valid button! This is a bug, please report it.");
    }
    pageButton.setItemMeta(pageMeta);
    return pageButton;
}
```

The change is in the line where an enchantment is added. Instead of using the `parseEnchantment()` method from the `XEnchantment` class, I used the `getEnchantment()` method from the `Enchantment` class and passed the ID obtained from the `XEnchantment` class. This way, the code works with the new version of the library.