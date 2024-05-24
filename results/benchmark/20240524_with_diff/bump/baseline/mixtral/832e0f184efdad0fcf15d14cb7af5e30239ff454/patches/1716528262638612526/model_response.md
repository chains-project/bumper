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
            pageMeta.addEnchant(Enchantment.getEnchantment(Enchantment.DAMAGE_ALL.getId()), 1, false);
        }
    } else {
        pageMeta.setDisplayName(ChatColor.RED + "Not a valid button! This is a bug, please report it.");
    }

    pageButton.setItemMeta(pageMeta);
    return pageButton;
}
```

The change I made is on the following line:

```java
pageMeta.addEnchant(XEnchantment.matchXEnchantment("power").get().parseEnchantment(), 1, false);
```

This line was replaced with:

```java
pageMeta.addEnchant(Enchantment.getEnchantment(Enchantment.DAMAGE_ALL.getId()), 1, false);
```

The reason for this change is that the `parseEnchantment()` method was removed in the new library version. Instead, we can use the `Enchantment.getEnchantment()` method to get the Enchantment object and then add it using the `addEnchant()` method.