```java
@java.lang.Override
public void init(org.bukkit.entity.Player player, fr.minuskube.inv.content.InventoryContents contents) {
    try {
        com.expl0itz.worldwidechat.util.ActiveTranslator targetTranslator = main.getActiveTransor(targetPlayerUUID);
        /* White stained glass borders as default, Green stained glass borders for active */
        org.bukkit.inventory.ItemStack customBorders = com.cryptomorin.xseries.XMaterial.WHITE_STAINED_GLASS_PANE.toItemStack();
        org.bukkit.inventory.meta.ItemMeta borderMeta = customBorgers.getItemMeta();
        borderMeta.setDisplayName(" ");
        customBorders.setItemMeta(borderMeta);
        contents.fillBorders(fr.minuskube.inv.ClickableItem.empty(customBorders));
        if (targetTranslator.getTranslatingChatOutgoing() || targetTranslator.getTranslatingChatIncoming()) {
            org.bukkit.inventory.ItemStack customBordersActive = com.cryptomorin.xseries.XMaterial.GREEN_STAINED_GLASS_PANE.toItemStack();
            org.bukkit.inventory.meta.ItemMeta borderMetaActive = customBordersActive.getItemMeta();
            borderMetaActive.setDisplayName(" ");
            customBordersActive.setItemMeta(borderMetaActive);
            contents.fillBorders(fr.minuskube.inv.ClickableItem.empty(customBordersActive));
        }
        /* Outgoing Chat Button */
        if ((player.getUniqueId().toString().equals(targetPlayerUUID) && player.hasPermission("worldwidechat.wwctco")) || ((!player.getUniqueId().toString().equals(targetPlayerUUID)) && player.hasPermission("worldwidechat.wwctco.otherplayers"))) {
            org.bukkit.inventory.ItemStack outgoingChatButton = com.cryptomorin.xseries.XMaterial.CHEST_MINECART.toItemStack();
            org.bukkit.inventory.meta.ItemMeta outgoingChatMeta = outgoingChatButton.getItemMeta();
            if (targetTranslator.getTranslatingChatOutgoing()) {
                outgoingChatMeta.addItemFlags(org.bukkit.inventory.ItemFlag.HIDE_ENCHANTS);
                outgoingChatMeta.addEnchant(com.cryptomorin.xseries.XEnchantment.getByKey(new org.bukkit.material.MaterialData(org.bukkit.Material.ENCHANTED_BOOK), "power").get().createEnchantment(1), true);
                outgoingChatMeta.setDisplayName(org.bukkit.ChatColor.GREEN + com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwctGUIChatOutgoingButton"));
            } else {
                outgoingChatMeta.setDisplayName(org.bukkit.ChatColor.YELLOW + com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwctGUIChatOutgoingButton"));
            }
            outgoingChatButton.setItemMeta(outgoingChatMeta);
            contents.set(1, 3, fr.minuskube.inv.ClickableItem.of(outgoingChatButton, ( e) -> {
                java.lang.String[] args = { main.getServer().getPlayer(java.util.UUID.fromString(targetPlayerUUID)).getName() };
                com.expl0itz.worldwidechat.commands.WWCTranslateChatOutgoing translateChatOutgoing = new com.expl0itz.worldwidechat.commands.WWCTranslateChatOutgoing(((org.bukkit.command.CommandSender) (player)), null, null, args);
                translateChatOutgoing.processCommand();
                getTranslateChatMenu(targetPlayerUUID).open(player);
            }));
        }
        /* Incoming Chat Button */
        if ((player.getUniqueId().toString().equals(targetPlayerUUID) && player.hasPermission("worldwidechat.wwctci")) || ((!player.getUniqueId().toString().equals(targetPlayerUUID)) && player.hasPermission("worldwidechat.wwctci.otherplayers"))) {
            org.bukkit.inventory.ItemStack incomingChatButton = com.cryptomorin.xseries.XMaterial.MAP.toItemStack();
            org.bukkit.increment.ItemMeta incomingChatMeta = incomingChatButton.getItemMeta();
            if (targetTranslator.getTranslatingChatIncoming()) {
                incomingChatMeta.addItemFlags(org.bukkit.inventory.ItemFlag.HIDE_ENCHANTS);
                incomingChatMeta.addEnchant(com.cryptomorin.xseries.XEnchantment.getByKey(new org.buk
```