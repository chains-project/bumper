```java
@java.lang.Override
public void init(org.bukkit.entity.Player player, fr.minuskube.inv.content.InventoryContents contents) {
    try {
        org.bukkit.inventory.ItemStack customDefaultBorders = com.cryptomorin.xseries.XMaterial.WHITE_STAINED_GLASS_PANE.parseItem();
        if (!main.getActiveTranslator(targetPlayerUUID).getInLangCode().equals("")) {
            customDefaultBorders = com.cryptomorin.xseries.XMaterial.YELLOW_STAINED_GLASS_PANE.parseItem();
        }
        org.bukkit.inventory.meta.ItemMeta defaultBorderMeta = customDefaultBorders.getItemMeta();
        defaultBorderMeta.setDisplayName(" ");
        customDefaultBorders.setItemMeta(defaultBorderMeta);
        contents.fillBorders(fr.minuskube.inv.ClickableItem.empty(customDefaultBorders));
        com.expl0itz.worldwidechat.util.ActiveTranslator currTranslator = main.getActiveTranslator(targetPlayerUUID);
        fr.minuskube.inv.content.Pagination pagination = contents.pagination();
        fr.minuskube.inv.ClickableItem[] listOfAvailableLangs = new fr.minuskube.inv.ClickableItem[main.getSupportedTranslatorLanguages().size()];
        for (int i = 0; i < main.getSupportedTranslatorLanguages().size(); i++) {
            org.bukkit.inventory.ItemStack currentLang = com.cryptomorin.xseries.XMaterial.BOOK.parseItem();
            org.bukkit.inventory.meta.ItemMeta currentLangMeta = currentLang.getItemMeta();
            java.util.ArrayList<java.lang.String> lore = new java.util.ArrayList<>();
            currentLangMeta.addItemFlags(org.bukkit.inventory.ItemFlag.HIDE_ENCHANTS);
            if (selectedSourceLanguage.equals(main.getSupportedTranslatorLanguages().get(i).getLangCode())) {
                currentLangMeta.addEnchant(com.cryptomorin.xseries.XEnchantment.matchXEnchantment("power").get().parseEnchant(), 1, false);
                lore.add(((org.bukkit.ChatColor.GREEN + "") + org.bukkit.ChatColor.ITALIC) + com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwctGUISourceTranslationSelected"));
            } else if (currTranslator.getInLangCode().equals(main.getSupportedTranslatorLanguages().get(i).getLangCode())) {
                currentLangMeta.addEnchant(com.cryptomorin.xseries.XEnchantment.matchXEnchantment("power").get().parseEnchant(), 1, false);
                lore.add(((org.bukkit.ChatColor.YELLOW + "") + org.bukkit.ChatColor.ITALIC) + com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwctGUISourceOrTargetTranslationAlreadyActive"));
            }
            currentLangMeta.setDisplayName(main.getSupportedTranslatorLanguages().get(i).getLangName());
            if (!main.getSupportedTranslatorLanguages().get(i).getNativeLangName().equals("")) {
                lore.add(main.getSupportedTranslatorLanguages().get(i).getNativeLangName());
            }
            lore.add(main.getSupportedTranslatorLanguages().get(i).getLangCode());
            currentLangMeta.setLore(lore);
            currentLang.setItemMeta(currentLangMeta);
            java.lang.String thisLangCode = main.getSupportedTranslatorLanguages().get(i).getLangCode();
            listOfAvailableLangs[i] = fr.minuskube.inv.ClickableItem.of(currentLang, ( e) -> {
                com.expl0itz.worldwidechat.inventory.wwctranslategui.WWCTranslateGUITargetLanguage.getTargetLanguageInventory(thisLangCode, targetPlayerUUID).open(player);
            });
        }
        pagination.setItems(listOfAvailableLangs);
        pagination.setItemsPerPage(28);
        pagination.addToIterator(contents.newIterator(SlotIterator.Type.HORIZONTAL, 1, 1).allowOverride(false));
        if (!pagination.isFirst()) {
            contents.set(5, 2, fr.minuskube.inv.ClickableItem.of(com.expl0itz.worldwidechat.inventory.WWCInventoryManager.getCommonButton("Previous"), ( e) -> {
                getSourceLanguageInventory(selectedSourceLanguage, targetPlayerUUID).open(player, pagination.previous().getPage());
            }));
        } else {
            contents.set(5, 2, fr.minuskube.inv.ClickableItem.of(com.expl0itz.worldwidechat.inventory.WWCInventoryManager.getCommonButton("Previous"), ( e) -> {
                com.expl0itz.worldwidechat.inventory.wwctranslategui.WWCTranslateGUIMainMenu.getTranslateMainMenu(targetPlayerUUID).open(player);
            }));
        }
        if (!main.getTranslatorName().equalsIgnoreCase("Amazon Translate")) {
            org.bukkit.inventory.ItemStack skipSourceButton = com.cryptomorin.xseries.XMaterial.BOOKSHELF.parseItem();
            org.bukkit.inventory.meta.ItemMeta skipSourceMeta = skipSourceButton.getItemMeta();
            skipSourceMeta.setDisplayName(org.bukkit.ChatColor.YELLOW + com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwctGUIAutoDetectButton"));
            skipSourceMeta.addItemFlags(org.bukkit.inventory.ItemFlag.HIDE_ENCHANTS);
            java.util.ArrayList<java.lang.String> lore = new java.util.ArrayList<>();
            if (currTranslator.getInLangCode().equals("None")) {
                skipSourceMeta.addEnchant(com.cryptomorin.xseries.XEnchantment.matchXEnchantment("power").get().parseEnchant(), 1, false);
                lore.add(((org.bukkit.ChatColor.GREEN + "") + org.bukkit.ChatColor.ITALIC) + com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwctGUISourceTranslationSelected"));
            } else if (selectedSourceLanguage.equalsIgnoreCase("None")) {
                skipSourceMeta.addEnchant(com.cryptomorin.xseries.XEnchantment.matchXEnchantment("power").get().parseEnchant(), 1, false);
                lore.add(((org.bukkit.ChatColor.YELLOW + "") + org.bukkit.ChatColor.ITALIC) + com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwctGUISourceOrTargetTranslationAlreadyActive"));
            }
            skipSourceButton.setItemMeta(skipSourceMeta);
            contents.set(5, 4, fr.minuskube.inv.ClickableItem.of(skipSourceButton, ( e) -> com.expl0itz.worldwidechat.inventory.wwctranslategui.WWCTranslateGUITargetLanguage.getTargetLanguageInventory("None", targetPlayerUUID).open(player)));
        }
        if (!pagination.isLast()) {
            contents.set(5, 6, fr.minuskube.inv.ClickableItem.of(com.expl0itz.worldwidechat.inventory.WWCInventoryManager.getCommonButton("Next"), ( e) -> {
                getSourceLanguageInventory(selectedSourceLanguage, targetPlayerUUID).open(player, pagination.next().getPage());
            }));
        }
        contents.set(5, 8, fr.minuskube.inv.ClickableItem.of(com.expl0itz.worldwidechat.inventory.WWCInventoryManager.getCommonButton("Page Number", new java.lang.String[]{ (pagination.getPage() + 1) + "" }), ( e) -> {
        }));
    } catch (java.lang.Exception e) {
        com.expl0itz.worldwidechat.inventory.WWCInventoryManager.inventoryError(player, e);
    }
}
```