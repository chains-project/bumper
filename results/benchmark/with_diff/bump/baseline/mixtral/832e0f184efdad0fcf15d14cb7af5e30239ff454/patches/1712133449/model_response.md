Here's the updated `getCommonButton` method that should fix the error:

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
            Enchantment enchantment = XEnchantment.matchXEnchantment("power").get();
            pageMeta.addEnchant(enchantment, 1, false);
            pageButton.setItemMeta(pageMeta);
            pageButton = XMaterial.LILY_PAD.parseItem(pageMeta);
        }
    } else {
        pageMeta.setDisplayName(ChatColor.RED + "Not a valid button! This is a bug, please report it.");
    }
    pageButton.setItemMeta(pageMeta);
    return pageButton;
}
```

The main change is to replace the removed `parseEnchantment()` method with a call to `matchXEnchantment()` to get the desired `Enchantment` object, and then add the enchantment to the `pageMeta` using the `addEnchant()` method. After adding the enchantment, the `pageMeta` is applied to the `pageButton` using `parseItem()` again.

This change should fix the error and allow the code to compile and run with the new library version.