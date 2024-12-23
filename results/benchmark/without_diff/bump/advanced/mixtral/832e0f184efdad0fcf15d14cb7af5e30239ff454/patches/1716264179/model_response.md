Here's the proposed patch:

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
            org.bukkit.inventory.ItemStack currentLang = com.cryptomorin.xseries.XMaterial.BOOK.parseItem();
            org.bukkit.inventory.meta.ItemMeta currentLangMeta = currentLang.getItemMeta();
            /* Add Glow Effect */
            java.util.ArrayList<java.lang.String> lore = new java.util.ArrayList<>();
            currentLangMeta.addItemFlags(org.bukkit.inventory.ItemFlag.HIDE_ENCHANTS);
            if (selectedSourceLanguage.equals(main.getSupportedTranslatorLanguages().get(i).getLangCode())) {
                currentLangMeta.addEnchant(getEnchantmentByName("power"), 1, false);
                lore.add(((org.bukkit.ChatColor.GREEN + "") + org.bukkit.ChatColor.ITALIC) + com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwctGUISourceTranslationSelected"));
            } else if (currTranslator.getInLangCode().equals(main.getSupportedTranslatorLanguages().get(i).getLangCode())) {
                currentLangMeta.addEnchant(getEnchantmentByName("power"), 1, false);
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
        /* 28 langs per page, start at 1, 1 */
        pagination.setItems(listOfAvailableLangs);
        pagination.setItemsPerPage(28);
        pagination.addToIterator(contents.newIterator(SlotIterator.Type.HORIZONTAL, 1, 1).allowOverride(false));
        /* Bottom Left Option:
```