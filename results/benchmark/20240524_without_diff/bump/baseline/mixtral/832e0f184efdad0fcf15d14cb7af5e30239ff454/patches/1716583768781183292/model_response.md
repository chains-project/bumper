Here's the fixed `getCommonButton` method with the necessary changes:

```java
public static ItemStack getCommonButton(String buttonType, String[] args) {
    Material buttonMaterial;
    ItemStack pageButton = Material.WHITE_STAINED_GLASS_PANE.createItemStack();
    ItemMeta pageMeta = pageButton.getItemMeta();
    pageMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
    if (buttonType.equalsIgnoreCase("Previous")) {
        buttonMaterial = Material.RED_STAINED_GLASS_PANE;
    } else if (buttonType.equalsIgnoreCase("Next")) {
        buttonMaterial = Material.GREEN_STAINED_GLASS_PANE;
    } else if (buttonType.equalsIgnoreCase("Page Number")) {
        buttonMaterial = Material.LILY_PAD;
        if (args[0].equals("1")) {
            pageMeta.addEnchant(Enchantment.DAMAGE_ALL, 1, false);
        }
    } else {
        pageMeta.setDisplayName(ChatColor.RED + "Not a valid button! This is a bug, please report it.");
        return pageButton;
    }
    pageButton = buttonMaterial.createItemStack();
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

The following changes have been made:

1. Changed `Material.WHITE_STAINED_GLASS` to `Material.WHITE_STAINED_GLASS_PANE` and `buttonMaterial.parseItem()` to `buttonMaterial.createItemStack()` for creating the `pageButton`.
2. Changed `Material.RED_STAINED_GLASS` to `Material.RED_STAINED_GLASS_PANE` and `Material.GREEN_STAINED_GLASS` to `Material.GREEN_STAINED_GLASS_PANE` for creating the buttons.
3. Replaced `Enchantment.getByKey(Enchantments.DAMAGE_ALL).get()` with `Enchantment.DAMAGE_ALL` for getting the enchantment.

These changes should resolve the dependency update failure.