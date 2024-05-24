```java
@Override
public void init(Player player, InventoryContents contents) {
	try {
		/* Default white stained glass borders for inactive */
		ItemStack customDefaultBorders = XMaterial.WHITE_STAINED_GLASS_PANE.parseItem();
		if (!main.getActiveTranslator(targetPlayerUUID).getUUID().equals("")) {
			customDefaultBorders = XMaterial.GREEN_STAINED_GLASS_PANE.parseItem();
		}
		ItemMeta defaultBorderMeta = customDefaultBorders.getItemMeta();
		defaultBorderMeta.setDisplayName(" ");
		customDefaultBorders.setItemMeta(defaultBorderMeta);
		contents.fillBorders(ClickableItem.empty(customDefaultBorders));

		/* New translation button */
		ItemStack translationButton = XMaterial.COMPASS.parseItem();
		ItemMeta translationMeta = translationButton.getItemMeta();
		translationMeta.setDisplayName(
				CommonDefinitions.getMessage("wwctGUITranslationButton"));
		translationButton.setItemMeta(translationMeta);
		contents.set(2, 4, ClickableItem.of(translationButton, e -> {
			WWCTranslateGUISourceLanguage.getSourceLanguageInventory("", targetPlayerUUID).open(player);
		}));

		/* Set active translator to our current target */
		ActiveTranslator targetTranslator = main.getActiveTranslator(targetPlayerUUID);
		
		if (!main.getActiveTranslator(targetPlayerUUID).getUUID().equals("")) {
			/* Make compass enchanted */
			translationMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
			translationMeta.addEnchant(Enchantment.matchEnchantment("power"), 1, false);
			translationMeta.setDisplayName(CommonDefinitions.getMessage("wwctGUIExistingTranslationButton"));
			List<String> outLore = new ArrayList<>();
			outLore.add(ChatColor.LIGHT_PURPLE + CommonDefinitions.getMessage("wwctGUIExistingTranslationInput", new String[] {ChatColor.LIGHT_PURPLE + "" + ChatColor.BOLD + targetTranslator.getInLangCode()}));
			outLore.add(ChatColor.LIGHT_PURPLE + CommonDefinitions.getMessage("wwctGUIExistingTranslationOutput", new String[] {ChatColor.LIGHT_PURPLE + "" + ChatColor.BOLD + targetTranslator.getOutLangCode()}));
			translationMeta.setLore(outLore);
			translationButton.setItemMeta(translationMeta);

			// Remaining code...
		}
	} catch (Exception e) {
		WWCInventoryManager.inventoryError(player, e);
	}
}
```