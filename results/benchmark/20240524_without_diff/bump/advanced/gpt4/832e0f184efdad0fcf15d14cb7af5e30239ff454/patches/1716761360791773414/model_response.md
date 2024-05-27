```java
@java.lang.Override
public void init(org.bukkit.entity.Player player, fr.minuskube.inv.content.InventoryContents contents) {
    try {
        /* Default white stained glass borders for inactive, yellow if player has existing translation session */
        org.bukkit.inventory.ItemStack customDefaultBorders = com.cryptomorin.xseries.XMaterial.WHITE_STAINED_GLASS_PANE.parseItem();
        if (!main.getActiveTranslator(targetPlayerUUID).getInLangCode().equals("")) {
            customDefaultBorders = com.cryptomorin.xseries.XMaterial.YELLOW_STAINED_GLASS_PANE.parseItem();
        }
        org.bukkit.inventory.meta.ItemMeta defaultBorderMeta = customDefaultBorders.getItemMeta();
        defaultBorderMeta.setDisplayName(" ");
        customDefaultBorders.setItemMeta(defaultBorderMeta);
        contents.fillBorders(fr.minuskube.inv.ClickableItem.empty(customDefaultBorders));
        /* Init current active translator */
        com.expl0itz.worldwidechat.util.ActiveTranslator currTranslator = main.getActiveTranslator(targetPlayerUUID);
        /* Pagination: Lets you generate pages rather than set defined ones */
        fr.minuskube.inv.content.Pagination pagination = contents.pagination();
        fr.minuskube.inv.ClickableItem[] listOfAvailableLangs = new fr.minuskube.inv.ClickableItem[main.getSupportedTranslatorLanguages().size()];
        /* Add each supported language from each respective translator */
        for (int i = 0; i < main.getSupportedTranslatorLanguages().size(); i++) {
            org.bukkit.inventory.ItemStack currentLang = com.cryptomorin.xseries.XMaterial.ARROW.parseItem();
            if (com.cryptomorin.xseries.XMaterial.TARGET.parseItem() != null) {
                currentLang = com.cryptomorin.xseries.XMaterial.TARGET.parseItem();
            }
            org.bukkit.inventory.meta.ItemMeta currentLangMeta = currentLang.getItemMeta();
            java.util.ArrayList<java.lang.String> lore = new java.util.ArrayList<>();
            /* Add Glow Effect */
            currentLangMeta.addItemFlags(org.bukkit.inventory.ItemFlag.HIDE_ENCHANTS);
            if (currTranslator.getOutLangCode().equals(main.getSupportedTranslatorLanguages().get(i).getLangCode())) {
                currentLangMeta.addEnchant(com.cryptomorin.xseries.XEnchantment.matchXEnchantment("power").get().get(), 1, false);
                lore.add(((org.bukkit.ChatColor.YELLOW + "") + org.bukkit.ChatColor.ITALIC) + com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwctGUISourceOrTargetTranslationAlreadyActive"));
            }
            currentLangMeta.setDisplayName(main.getSupportedTranslatorLanguages().get(i).getLangName());
            if (!main.getSupportedTranslatorLanguages().get(i).getNativeLangName().equals("")) {
                lore.add(main.getSupportedTranslatorLanguages().get(i).getNativeLangName());
            }
            lore.add(main.getSupportedTranslatorLanguages().get(i).getLangCode());
            currentLangMeta.setLore(lore);
            currentLang.setItemMeta(currentLangMeta);
            java.lang.String outLang = main.getSupportedTranslatorLanguages().get(i).getLangCode();
            listOfAvailableLangs[i] = fr.minuskube.inv.ClickableItem.of(currentLang, ( e) -> {
                /* Send to /wwct */
                com.expl0itz.worldwidechat.commands.WWCTranslate translateCommand;
                if (!targetPlayerUUID.equals("GLOBAL-TRANSLATE-ENABLED")) {
                    translateCommand = new com.expl0itz.worldwidechat.commands.WWCTranslate(((org.bukkit.command.CommandSender) (player)), null, null, new java.lang.String[]{ main.getServer().getPlayer(java.util.UUID.fromString(targetPlayerUUID)).getName(), selectedSourceLanguage, outLang });
                } else {
                    translateCommand = new com.expl0itz.worldwidechat.commands.WWCGlobal(((org.bukkit.command.CommandSender) (player)), null, null, new java.lang.String[]{ selectedSourceLanguage, outLang });
                }
                player.closeInventory();
                translateCommand.processCommand();
            });
        }
        /* 28 langs per page, start at 1, 1 */
        pagination.setItems(listOfAvailableLangs);
        pagination.setItemsPerPage(28);
        pagination.addToIterator(contents.newIterator(SlotIterator.Type.HORIZONTAL, 1, 1).allowOverride(false));
        /* Bottom Left Option: Previous Page */
        if (!pagination.isFirst()) {
            contents.set(5, 2, fr.minuskube.inv.ClickableItem.of(com.expl0itz.worldwidechat.inventory.WWCInventoryManager.getCommonButton("Previous"), ( e) -> getTargetLanguageInventory(selectedSourceLanguage, targetPlayerUUID).open(player, pagination.previous().getPage())));
        } else {
            contents.set(5, 2, fr.minuskube.inv.ClickableItem.of(com.expl0itz.worldwidechat.inventory.WWCInventoryManager.getCommonButton("Previous"), ( e) -> com.expl0itz.worldwidechat.inventory.wwctranslategui.WWCTranslateGUISourceLanguage.getSourceLanguageInventory(selectedSourceLanguage, targetPlayerUUID).open(player)));
        }
        /* Bottom Right Option: Next Page */
        if (!pagination.isLast()) {
            contents.set(5, 6, fr.minuskube.inv.ClickableItem.of(com.expl0itz.worldwidechat.inventory.WWCInventoryManager.getCommonButton("Next"), ( e) -> getTargetLanguageInventory(selectedSourceLanguage, targetPlayerUUID).open(player, pagination.next().getPage())));
        }
        /* Last Option: Page Number */
        contents.set(5, 8, fr.minuskube.inv.ClickableItem.of(com.expl0itz.worldwidechat.inventory.WWCInventoryManager.getCommonButton("Page Number", new java.lang.String[]{ (pagination.getPage() + 1) + "" }), ( e) -> {
        }));
    } catch (java.lang.Exception e) {
        com.expl0itz.worldwidechat.inventory.WWCInventoryManager.inventoryError(player, e);
    }
}
```