Here is a fixed version of the method that should resolve the error:
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
			pageMeta.addEnchant(Enchantment.getByName("PROTECTION_ENVIRONMENTAL"), 1, false);
		}
	} else {
		pageMeta.setDisplayName(ChatColor.RED + "Not a valid button! This is a bug, please report it.");
	}
	pageButton.setItemMeta(pageMeta);
	return pageButton;
}
```
The change I made is to replace the line that uses the `XEnchantment` class with a line that uses the `Enchantment` class instead, and to replace the `matchXEnchantment` method with the `getByName` method. This should resolve the "cannot find symbol" error.

Note that the specific enchantment name passed to `getByName` was changed from `"power"` to `"PROTECTION_ENVIRONMENTAL"`, as the former is no longer available in the updated library version. You may need to adjust this value based on the specific enchantment you want to use.