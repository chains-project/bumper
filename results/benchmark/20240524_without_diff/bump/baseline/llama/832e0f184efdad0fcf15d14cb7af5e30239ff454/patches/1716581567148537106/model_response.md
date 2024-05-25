```java
public static ItemStack getCommonButton(String buttonType, String[] args) {
	ItemStack pageButton = ItemStack.builder().material(Material.WHITE_STAINED_GLASS).build();
	ItemMeta pageMeta = pageButton.getItemMeta();
	pageMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
	if (buttonType.equalsIgnoreCase("Previous")) {
		pageButton.setMaterial(Material.RED_STAINED_GLASS);
		pageMeta.setDisplayName(ChatColor.RED + CommonDefinitions.getMessage("wwcConfigGUIPreviousPageButton"));
	} else if (buttonType.equalsIgnoreCase("Next")) {
		pageButton.setMaterial(Material.GREEN_STAINED_GLASS);
		pageMeta.setDisplayName(ChatColor.GREEN + CommonDefinitions.getMessage("wwcConfigGUINextPageButton"));
	} else if (buttonType.equalsIgnoreCase("Page Number")) {
		pageButton.setMaterial(Material.LILY_PAD);
		pageMeta.setDisplayName(ChatColor.AQUA + CommonDefinitions.getMessage("wwcGUIPageNumber", args));
		if (args[0].equals("1")) {
			pageMeta.addEnchant(Enchantment.DURABILITY, 1, false);
		}
	} else {
		pageMeta.setDisplayName(ChatColor.RED + "Not a valid button! This is a bug, please report it.");
	}
	pageButton.setItemMeta(pageMeta);
	return pageButton;
}
```