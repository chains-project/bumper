Here's the proposed patch:

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
		if (args.length > 0 && args[0].equals("1")) {
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

- Replacing deprecated `parseItem()` method with `createItemStack()` for `Material` and `ItemStack`.
- Adding a bounds check for the `args` array before accessing the first element.
- Changing the `getItemMeta()` call to be before the `buttonMaterial` assignment.