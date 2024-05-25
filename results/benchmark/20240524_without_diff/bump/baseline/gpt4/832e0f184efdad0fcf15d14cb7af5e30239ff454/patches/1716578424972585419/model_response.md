```java
@Override
public void init(Player player, InventoryContents contents) {
	try {
		ActiveTranslator targetTranslator = main.getActiveTranslator(targetPlayerUUID);
		
		ItemStack customBorders = XMaterial.WHITE_STAINED_GLASS_PANE.parseItem();
		ItemMeta borderMeta = customBorders.getItemMeta();
		borderMeta.setDisplayName(" ");
		customBorders.setItemMeta(borderMeta);
		contents.fillBorders(ClickableItem.empty(customBorders));
		
		if (targetTranslator.getTranslatingChatOutgoing() || targetTranslator.getTranslatingChatIncoming()) {
			ItemStack customBordersActive = XMaterial.GREEN_STAINED_GLASS_PANE.parseItem();
			ItemMeta borderMetaActive = customBordersActive.getItemMeta();
			borderMetaActive.setDisplayName(" ");
			customBordersActive.setItemMeta(borderMetaActive);
			contents.fillBorders(ClickableItem.empty(customBordersActive));
		}
		
		if ((player.getUniqueId().toString().equals(targetPlayerUUID) && player.hasPermission("worldwidechat.wwctco")) || (!player.getUniqueId().toString().equals(targetPlayerUUID)) && player.hasPermission("worldwidechat.wwctco.otherplayers")) {
			ItemStack outgoingChatButton = XMaterial.CHEST_MINECART.parseItem();
			ItemMeta outgoingChatMeta = outgoingChatButton.getItemMeta();
			if (targetTranslator.getTranslatingChatOutgoing()) {
				outgoingChatMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
				outgoingChatMeta.addEnchant(Enchantment.ARROW_DAMAGE, 1, false);
				outgoingChatMeta.setDisplayName(ChatColor.GREEN
						+ CommonDefinitions.getMessage("wwctGUIChatOutgoingButton"));
			} else {
				outgoingChatMeta.setDisplayName(ChatColor.YELLOW
						+ CommonDefinitions.getMessage("wwctGUIChatOutgoingButton"));
			}
			outgoingChatButton.setItemMeta(outgoingChatMeta);
			contents.set(1, 3, ClickableItem.of(outgoingChatButton, e -> {
				String[] args = { main.getServer().getPlayer(UUID.fromString(targetPlayerUUID)).getName() };
				WWCTranslateChatOutgoing translateChatOutgoing = new WWCTranslateChatOutgoing((CommandSender) player, null, null, args);
				translateChatOutgoing.processCommand();
				getTranslateChatMenu(targetPlayerUUID).open(player);
			}));	
		}
		
		if ((player.getUniqueId().toString().equals(targetPlayerUUID) && player.hasPermission("worldwidechat.wwctci")) || (!player.getUniqueId().toString().equals(targetPlayerUUID)) && player.hasPermission("worldwidechat.wwctci.otherplayers")) {
        	ItemStack incomingChatButton = XMaterial.MAP.parseItem();
			ItemMeta incomingChatMeta = incomingChatButton.getItemMeta();
			if (targetTranslator.getTranslatingChatIncoming()) {
				incomingChatMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
				incomingChatMeta.addEnchant(Enchantment.ARROW_DAMAGE, 1, false);
				incomingChatMeta.setDisplayName(ChatColor.GREEN
						+ CommonDefinitions.getMessage("wwctGUIChatIncomingButton"));
			} else {
				incomingChatMeta.setDisplayName(ChatColor.YELLOW
						+ CommonDefinitions.getMessage("wwctGUIChatIncomingButton"));
			}
			incomingChatButton.setItemMeta(incomingChatMeta);
			contents.set(1, 5, ClickableItem.of(incomingChatButton, e -> {
				String[] args = { main.getServer().getPlayer(UUID.fromString(targetPlayerUUID)).getName() };
				WWCTranslateChatIncoming translateChatIncoming = new WWCTranslateChatIncoming((CommandSender) player, null, null, args);
				translateChatIncoming.processCommand();
				getTranslateChatMenu(targetPlayerUUID).open(player);
			}));	
		}
		
		contents.set(2, 4, ClickableItem.of(WWCInventoryManager.getCommonButton("Previous"), e -> {
			WWCTranslateGUIMainMenu.getTranslateMainMenu(targetPlayerUUID).open(player);
		}));
	} catch (Exception e) {
		WWCInventoryManager.inventoryError(player, e);
	}
}
```