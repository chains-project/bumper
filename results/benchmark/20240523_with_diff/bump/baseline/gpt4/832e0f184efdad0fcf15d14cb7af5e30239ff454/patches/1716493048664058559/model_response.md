```java
@Override
public void init(Player player, InventoryContents contents) {
	try {
		/* White stained glass borders */
		ItemStack customBorders = XMaterial.YELLOW_STAINED_GLASS_PANE.parseItem();
		ItemMeta borderMeta = customBorders.getItemMeta();
		borderMeta.setDisplayName(" ");
		customBorders.setItemMeta(borderMeta);
		contents.fillBorders(ClickableItem.empty(customBorders));
		
		/* Pagination */
		Pagination pagination = contents.pagination();
		HashMap<String, String> messagesFromConfig = new HashMap<String, String>();
		ClickableItem[] currentMessages = new ClickableItem[0];
		FileConfiguration messagesConfig = main.getConfigManager().getMessagesConfig();
		
		for (String eaKey : messagesConfig.getConfigurationSection("Messages").getKeys(true)) {
			messagesFromConfig.put(eaKey, messagesConfig.getString("Messages." + eaKey));
		}
		currentMessages = new ClickableItem[messagesFromConfig.size()];
		
		int currSpot = 0;
		CommonDefinitions.sendDebugMessage("Adding all possible messages to inventory! Amount of messages: " + currentMessages.length);
		for (Map.Entry<String, String> entry : messagesFromConfig.entrySet()) {
			/* Init item, ensure pre-1.14 compatibility */
			ItemStack currentEntry = XMaterial.OAK_SIGN.parseItem();
			ItemMeta currentEntryMeta = currentEntry.getItemMeta();
			
			currentEntryMeta.setDisplayName(entry.getKey());
			ArrayList<String> lore = new ArrayList<>();
			if (messagesConfig.getString("Overrides." + entry.getKey()) != null) {
				lore.add(ChatColor.YELLOW + "" + ChatColor.ITALIC + CommonDefinitions.getMessage("wwcConfigGUIMessagesAlreadyOverriden"));
				currentEntryMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
				currentEntryMeta.addEnchant(XEnchantment.matchXEnchantment("power").get().parseEnchantment(), 1, false);
			}
			lore.add(CommonDefinitions.getMessage("wwcConfigGUIMessagesOverrideOriginalLabel") + ": " + messagesConfig.getString("Messages." + entry.getKey()));
			currentEntryMeta.setLore(lore);
			currentEntry.setItemMeta(currentEntryMeta);
			currentMessages[currSpot] = ClickableItem.of(currentEntry, e -> {
				// Start conversation
				ConversationFactory textConvo = new ConversationFactory(main).withModality(true)
						.withFirstPrompt(new ChatSettingsModifyOverrideTextConversation(ConfigurationMessagesOverridePossibleListGUI.this.overrideNewMessageSettings, entry.getKey()));
				textConvo.buildConversation(player).begin();
			});
			currSpot++;
		}
		
		/* 28 messages per page, start at 1, 1 */
		pagination.setItems(currentMessages);
		pagination.setItemsPerPage(28);
		pagination.addToIterator(contents.newIterator(SlotIterator.Type.HORIZONTAL, 1, 1).allowOverride(false));
		
		/* Bottom Left Option: Previous Page */
		if (!pagination.isFirst()) {
			contents.set(5, 2, ClickableItem.of(WWCInventoryManager.getCommonButton("Previous"), e -> {
				overrideNewMessageSettings.open(player,
						pagination.previous().getPage());
			}));
		} else {
			contents.set(5, 2, ClickableItem.of(WWCInventoryManager.getCommonButton("Previous"), e -> {
				ConfigurationMessagesOverrideCurrentListGUI.overrideMessagesSettings.open(player);
			}));
		}
		
		/* Middle Option: Current Page Number */
		contents.set(5, 4, ClickableItem.of(WWCInventoryManager.getCommonButton("Page Number", new String[] {pagination.getPage() + 1 + ""}), e -> {}));
		
		/* Bottom Right Option: Next Page */
		if (!pagination.isLast()) {
			contents.set(5, 6, ClickableItem.of(WWCInventoryManager.getCommonButton("Next"), e -> {
				overrideNewMessageSettings.open(player,
						pagination.next().getPage());
			}));
		}
	} catch (Exception e) {
		WWCInventoryManager.inventoryError(player, e);
	}
}
```