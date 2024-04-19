Here's the updated `getCommonButton` method that fixes the error:

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
            pageMeta.addEnchant(Enchantment.getByKey(NamespacedKey.minecraft("power")), 1, false);
        }
    } else {
        pageMeta.setDisplayName(ChatColor.RED + "Not a valid button! This is a bug, please report it.");
    }
    pageButton.setItemMeta(pageMeta);
    return pageButton;
}
```

The change is replacing the following line:

```java
pageMeta.addEnchant(XEnchantment.matchXEnchantment("power").get().parseEnchantment(), 1, false);
```

with:

```java
pageMeta.addEnchant(Enchantment.getByKey(NamespacedKey.minecraft("power")), 1, false);
```

The reason for this change is that the `parseEnchantment()` method has been removed in the updated library version. Instead, you can use `Enchantment.getByKey(NamespacedKey.minecraft("power"))` to get the `Enchantment` object and then add it to the item meta using `addEnchant()`.