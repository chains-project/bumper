Here's the fixed `getCommonButton` method:

```java
public static ItemStack getCommonButton(String buttonType, String[] args) {
    Material buttonMaterial;
    ItemStack pageButton = Material.WHITE_STAINED_GLASS_PANE.createItemStack(1);
    ItemMeta pageMeta = pageButton.getItemMeta();
    pageMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
    if (buttonType.equalsIgnoreCase("Previous")) {
        buttonMaterial = Material.RED_STAINED_GLASS;
    } else if (buttonType.equalsIgnoreCase("Next")) {
        buttonMaterial = Material.GREEN_STAINED_GLASS;
    } else if (buttonType.equalsIgnoreCase("Page Number")) {
        buttonMaterial = Material.LILY_PAD;
        if (args[0].equals("1")) {
            pageMeta.addEnchant(Enchantment.DAMAGE_ALL, 1, false);
        }
    } else {
        pageMeta.setDisplayName(ChatColor.RED + "Not a valid button! This is a bug, please report it.");
        return pageButton;
    }
    pageButton = buttonMaterial.createItemStack(1);
    pageMeta.setDisplayName(ChatColor.WHITE + CommonDefinitions.getMessage("wwcConfigGUIPageButton"));
    if (!buttonType.equalsIgnoreCase("Page Number")) {
        pageMeta.setDisplayName(ChatColor.getByChar('&') + switch (buttonType) {
            case "Previous" -> "cRed" + CommonDefinitions.getMessage("wwcConfigGUIPreviousPageButton");
            case "Next" -> "aGreen" + CommonDefinitions.getMessage("wwcConfigGUINextPageButton");
            default -> "1";
        });
    }
    pageButton.setItemMeta(pageMeta);
    return pageButton;
}
```

The changes include:

- Replacing `Material.WHITE_STAINED_GLASS.parseItem()` and `buttonMaterial.parseItem()` with `Material.WHITE_STAINED_GLASS_PANE.createItemStack(1)` and `buttonMaterial.createItemStack(1)` respectively.
- Replacing `Enchantment.getByKey(Enchantments.DAMAGE_ALL).get()` with `Enchantment.DAMAGE_ALL`.
- Adding the missing `.createItemStack(1)` to `pageButton = buttonMaterial.parseItem();`.

These changes should resolve the "expected" error.