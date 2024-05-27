```java
@java.lang.Override
public void init(org.bukkit.entity.Player player, fr.minuskube.inv.content.InventoryContents contents) {
    try {
        /* White stained glass borders */
        org.bukkit.inventory.ItemStack customBorders = com.cryptomorin.xseries.XMaterial.YELLOW_STAINED_GLASS_PANE.parseItem();
        org.bukkit.inventory.meta.ItemMeta borderMeta = customBorders.getItemMeta();
        borderMeta.setDisplayName(" ");
        customBorders.setItemMeta(borderMeta);
        contents.fillBorders(fr.minuskube.inv.ClickableItem.empty(customBorders));
        /* Pagination */
        fr.minuskube.inv.content.Pagination pagination = contents.pagination();
        java.util.HashMap<java.lang.String, java.lang.String> messagesFromConfig = new java.util.HashMap<java.lang.String, java.lang.String>();
        fr.minuskube.inv.ClickableItem[] currentMessages = new fr.minuskube.inv.ClickableItem[0];
        org.bukkit.configuration.file.FileConfiguration messagesConfig = main.getConfigManager().getMessagesConfig();
        for (java.lang.String eaKey : messagesConfig.getConfigurationSection("Messages").getKeys(true)) {
            messagesFromConfig.put(eaKey, messagesConfig.getString("Messages." + eaKey));
        }
        currentMessages = new fr.minuskube.inv.ClickableItem[messagesFromConfig.size()];
        int currSpot = 0;
        com.expl0itz.worldwidechat.util.CommonDefinitions.sendDebugMessage("Adding all possible messages to inventory! Amount of messages: " + currentMessages.length);
        for (java.util.Map.Entry<java.lang.String, java.lang.String> entry : messagesFromConfig.entrySet()) {
            /* Init item, ensure pre-1.14 compatibility */
            org.bukkit.inventory.ItemStack currentEntry = com.cryptomorin.xseries.XMaterial.OAK_SIGN.parseItem();
            org.bukkit.inventory.meta.ItemMeta currentEntryMeta = currentEntry.getItemMeta();
            currentEntryMeta.setDisplayName(entry.getKey());
            java.util.ArrayList<java.lang.String> lore = new java.util.ArrayList<>();
            if (messagesConfig.getString("Overrides." + entry.getKey()) != null) {
                lore.add(((org.bukkit.ChatColor.YELLOW + "") + org.bukkit.ChatColor.ITALIC) + com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwcConfigGUIMessagesAlreadyOverriden"));
                currentEntryMeta.addItemFlags(org.bukkit.inventory.ItemFlag.HIDE_ENCHANTS);
                currentEntryMeta.addEnchant(com.cryptomorin.xseries.XEnchant.wrap(com.cryptomorin.xseries.XMaterial.matchXMaterial("PROTECTION").get().parseMaterial()), 1);
            }
            lore.add((com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwcConfigGUIMessagesOverrideOriginalLabel") + ": ") + messagesConfig.getString("Messages." + entry.getKey()));
            currentEntryMeta.setLore(lore);
            currentEntry.setItemMeta(currentEntryMeta);
            currentMessages[currSpot] = fr.minuskube.inv.ClickableItem.of(currentEntry, (e) -> {
                // Start conversation
                org.bukkit.conversations.ConversationFactory textConvo = new org.bukkit.conversations.ConversationFactory(main).withModality(true).withFirstPrompt(new com.expl0itz.worldwidechat.conversations.configuration.ChatSettingsModifyOverrideTextConversation(ConfigurationMessagesOverridePossibleListGUI.overrideNewMessageSettings, entry.getKey()));
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
            contents.set(5, 2, fr.minuskube.inv.ClickableItem.of(com.expl0itz.worldwidechat.inventory.WWCInventoryManager.getCommonButton("Previous"), (e) -> {
                com.expl0itz.worldwidechat.inventory.configuration.ConfigurationMessagesOverridePossibleListGUI.overrideNewMessageSettings.open(player, pagination.previous().getPage());
            }));
        } else {
            contents.set(5, 2, fr.minuskube.inv.ClickableItem.of(com.expl0itz.worldwidechat.inventory.WWCInventoryManager.getCommonButton("Previous"), (e) -> {
                ConfigurationMessagesOverrideCurrentListGUI.overrideMessagesSettings.open(player);
            }));
        }
        /* Middle Option: Current Page Number */
        contents.set(5, 4, fr.minuskube.inv.ClickableItem.of(com.expl0itz.worldwidechat.inventory.WWCInventoryManager.getCommonButton("Page Number", new java.lang.String[]{ java.lang.String.valueOf(pagination.getPage() + 1) }), (e) -> {}));
        /* Bottom Right Option: Next Page */
        if (!pagination.isLast()) {
            contents.set(5, 6, fr.minuskube.inv.ClickableItem.of(com.expl0itz.worldwidechat.inventory.WWCInventoryManager.getCommonButton("Next"), (e) -> {
                com.expl0itz.worldwidechat.inventory.configuration.ConfigurationMessagesOverridePossibleListGUI.overrideNewMessageSettings.open(player, pagination.next().getPage());
            }));
        }
    } catch (java.lang.Exception e) {
        com.expl0itz.worldwidechat.inventory.WWCInventoryManager.inventoryError(player, e);
    }
}
```