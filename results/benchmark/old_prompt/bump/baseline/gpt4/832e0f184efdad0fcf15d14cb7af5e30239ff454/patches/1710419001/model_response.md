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
			pageMeta.addEnchant(Enchantment.matchEnchantment("power"), 1, false);
		}
	} else {
		pageMeta.setDisplayName(ChatColor.RED + "Not a valid button! This is a bug, please report it.");
	}
	
	pageButton.setItemMeta(pageMeta);
	return pageButton;
}
```
In the above code, I replaced the `XEnchantment.matchXEnchantment("power").get().parseEnchantment()` line with `Enchantment.matchEnchantment("power")`. This is because the `XEnchantment` class is not part of the standard Bukkit API and might have been removed or renamed in a dependency update. The `Enchantment` class is part of the standard Bukkit API and should always be available.