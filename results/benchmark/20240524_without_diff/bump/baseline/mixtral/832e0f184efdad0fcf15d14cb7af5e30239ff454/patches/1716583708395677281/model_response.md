Here's a patch to fix the error:

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

The changes include:

- Replacing `parseItem()` with `createItemStack()` for `Material` instances, as the former method has been removed.
- Replacing the deprecated `getByKey(NamespacedKey)` method in `Enchantment` with the direct `Enchantment` reference.