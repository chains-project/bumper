Here's the proposed patch for the given code:

```java
	public static ItemStack getCommonButton(String buttonType, String[] args) {
		Material buttonMaterial;
		ItemStack pageButton = Material.WHITE_STAINED_GLASS.parseItem();
		ItemMeta pageMeta = pageButton.getItemMeta();
		pageMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
		if (buttonType.equalsIgnoreCase("Previous")) {
			buttonMaterial = Material.RED_STAINED_GLASS;
		} else if (buttonType.equalsIgnoreCase("Next")) {
			buttonMaterial = Material.GREEN_STAINED_GLASS;
		} else if (buttonType.equalsIgnoreCase("Page Number")) {
			buttonMaterial = Material.LILY_PAD;
			if (args[0].equals("1")) {
				pageMeta.addEnchant(Enchantment.getByKey(Enchantments.DAMAGE_ALL).get(), 1, false);
			}
		} else {
			pageMeta.setDisplayName(ChatColor.RED + "Not a valid button! This is a bug, please report it.");
			return pageButton;
		}
		pageButton = buttonMaterial.parseItem();
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

This patch replaces the deprecated `XMaterial` and `XEnchantment` classes with the newer `Material` and `Enchantment` classes. I've also made some minor changes to the code for readability and to ensure that the enchantment is added only when the button type is "Page Number" and the page number is 1.