Here's a patch for the given code failure:

```java
public static ItemStack getCommonButton(String buttonType, String[] args) {
    XMaterial material = XMaterial.WHITE_STAINED_GLASS;
    ItemStack pageButton = material.parseItem();
    ItemMeta pageMeta = pageButton.getItemMeta();
    pageMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);

    if (buttonType.equalsIgnoreCase("Previous")) {
        material = XMaterial.RED_STAINED_GLASS;
        pageButton = material.parseItem();
        pageMeta.setDisplayName(ChatColor.RED +
                CommonDefinitions.getMessage("wwcConfigGUIPreviousPageButton"));
    } else if (buttonType.equalsIgnoreCase("Next")) {
        material = XMaterial.GREEN_STAINED_GLASS;
        pageButton = material.parseItem();
        pageMeta.setDisplayName(ChatColor.GREEN +
                CommonDefinitions.getMessage("wwcConfigGUINextPageButton"));
    } else if (buttonType.equalsIgnoreCase("Page Number")) {
        material = XMaterial.LILY_PAD;
        pageButton = material.parseItem();
        pageMeta.setDisplayName(ChatColor.AQUA +
                CommonDefinitions.getMessage("wwcGUIPageNumber", args));

        if (args[0].equals("1")) {
            pageMeta.addEnchant(XEnchantment.getByName("power").get(), 1, false);
        }
    } else {
        pageMeta.setDisplayName(ChatColor.RED + "Not a valid button! This is a bug, please report it.");
    }

    pageButton.setItemMeta(pageMeta);
    return pageButton;
}
```

Changes made:

1. Replaced `XMaterial.parseItem()` with a variable `material` of type `XMaterial`.
2. Changed `XMaterial.matchXEnchantment("power").get().parseEnchantment()` to `XEnchantment.getByName("power").get()` to avoid the "cannot find symbol" error.