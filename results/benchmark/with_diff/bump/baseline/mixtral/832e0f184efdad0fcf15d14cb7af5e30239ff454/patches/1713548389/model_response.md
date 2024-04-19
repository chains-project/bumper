Here's the updated `getCommonButton` method that should fix the error:

```java
public static ItemStack getCommonButton(String buttonType, String[] args) {
    ItemStack pageButton = XMaterial.WHITE_STAINED_GLASS.parseItem();
    ItemMeta pageMeta = pageButton.getItemMeta();
    pageMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
    if (buttonType.equalsIgnoreCase("Previous")) {
        pageButton = XMaterial.RED_STAINED_GLASS.parseItem();
        pageMeta.setDisplayName(ChatColor.RED + CommonDefinitions.getMessage("wwcConfigGUIPreviousPageButton"));
    } else if (buttonType.equalsIgnoreCase("Next")) {
        pageButton = XMaterial.GREEN_STAINED_GLASS.parseItem();
        pageMeta.setDisplayName(ChatColor.GREEN + CommonDefinitions.getMessage("wwcConfigGUINextPageButton"));
    } else if (buttonType.equalsIgnoreCase("Page Number")) {
        pageButton = XMaterial.LILY_PAD.parseItem();
        pageMeta.setDisplayName(ChatColor.AQUA + CommonDefinitions.getMessage("wwcGUIPageNumber", args));
        if (args[0].equals("1")) {
            Enchantment enchantment = XEnchantment.matchXEnchantment("power").get();
            pageMeta.addEnchant(enchantment, 1, false);
        }
    } else {
        pageMeta.setDisplayName(ChatColor.RED + "Not a valid button! This is a bug, please report it.");
    }
    pageButton.setItemMeta(pageMeta);
    return pageButton;
}
```

The main change is the way the enchantment is added. Instead of calling `parseEnchantment()` on the `XEnchantment` object, the `matchXEnchantment()` method is used to get the corresponding `Enchantment` object, and then it's added using the `addEnchant()` method on the `ItemMeta` object.