Here's a fixed version of the method:

```java
@java.lang.Override
public void init(org.bukkit.entity.Player player, fr.minuskube.inv.content.InventoryContents contents) {
    try {
        com.expl0itz.worldwidechat.util.ActiveTranslator targetTranslator = main.getActiveTranslator(targetPlayerUUID);
        /* White stained glass borders as default, Green stained glass borders for active */
        org.bukkit.inventory.ItemStack customBorders = java.util.Objects.requireNonNull(com.cryptomorin.xseries.XMaterial.WHITE_STAINED_GLASS_PANE.parseItem()).clone();
        org.bukkit.inventory.meta.ItemMeta borderMeta = customBorders.getItemMeta();
        borderMeta.setDisplayName(" ");
        customBorders.setItemMeta(borderMeta);
        contents.fillBorders(fr.minuskube.inv.ClickableItem.empty(customBorders));
        if (targetTranslator.getTranslatingChatOutgoing() || targetTranslator.getTranslatingChatIncoming()) {
            org.bukkit.inventory.ItemStack customBordersActive = java.util.Objects.requireNonNull(com.cryptomorin.xseries.XMaterial.GREEN_STAINED_GLASS_PANE.parseItem()).clone();
            org.bukkit.inventory.meta.ItemMeta borderMetaActive = customBordersActive.getItemMeta();
            borderMetaActive.setDisplayName(" ");
            customBordersActive.setItemMeta(borderMetaActive);
            contents.fillBorders(fr.minuskube.inv.ClickableItem.empty(customBordersActive));
        }
        /* Outgoing Chat Button */
        if ((player.getUniqueId().toString().equals(targetPlayerUUID) && player.hasPermission("worldwidechat.wwctco")) || ((!player.getUniqueId().toString().equals(targetPlayerUUID)) && player.hasPermission("worldwidechat.wwctco.otherplayers"))) {
            org.bukkit.inventory.ItemStack outgoingChatButton = java.util.Objects.requireNonNull(com.cryptomorin.xseries.XMaterial.CHEST_MINECART.parseItem()).clone();
            org.bukkit.inventory.meta.ItemMeta outgoingChatMeta = outgoingChatButton.getItemMeta();
            if (targetTranslator.getTranslatingChatOutgoing()) {
                outgoingChatMeta.addItemFlags(org.bukkit.inventory.ItemFlag.HIDE_ENCHANTS);
                com.cryptomorin.xseries.XEnchantment powerEnchantment = com.cryptomorin.xseries.XEnchantment.matchXEnchantment("power").get();
                outgoingChatMeta.addEnchant(powerEnchantment.parseEnchantment(), 1, false);
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
            org.bukkit.inventory.ItemStack incomingChatButton = java.util.Objects.requireNonNull(com.cryptomorin.xseries.XMaterial.MAP.parseItem()).clone();
            org.bukkit.inventory.meta.ItemMeta incomingChatMeta = incomingChatButton.getItemMeta();
            if (targetTranslator.getTranslatingChatIncoming()) {
                incomingChatMeta.addItemFlags(org.bukkit.inventory.ItemFlag.HIDE_ENCHANTS);
                com.cryptomorin.xseries.XEnchantment powerEnchantment = com.cryptomorin.xseries.XEnchantment.matchXEnchantment("power").get();
                incomingChatMeta.addEnchant(powerEnchantment.parseEnchantment(), 1, false);
                incomingChatMeta.setDisplayName(org.bukkit.ChatColor.GREEN + com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwctGUIChatIncomingButton"));
            } else {
                incomingChatMeta.setDisplayName(org.bukkit.ChatColor.YELLOW + com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwctGUIChatIncomingButton"));
            }
            incomingChatButton.setItemMeta(incomingChatMeta);
            contents.set(1, 5, fr.minuskube.inv.ClickableItem.of(incomingChatButton, ( e) -> {
                java.lang.String[] args = { main.getServer().getPlayer(java.util.UUID.fromString(targetPlayerUUID)).getName() };
                com.expl0itz.worldwidechat.commands.WWCTranslateChatIncoming translateChatIncoming = new com.expl0itz.worldwidechat.commands.WWCTranslateChatIncoming(((org.bukkit.command.CommandSender) (player)), null, null, args);
                translateChatIncoming.processCommand();
                getTranslateChatMenu(targetPlayerUUID).open(player);
            }));
        }
        /* Bottom Left Option: Previous Page */
        contents.set(2, 4, fr.minuskube.inv.ClickableItem.of(com.expl0itz.worldwidechat.inventory.WWCInventoryManager.getCommonButton("Previous"), ( e) -> {
            com.expl0itz.worldwidechat.inventory.wwctranslategui.WWCTranslateGUIMainMenu.getTranslateMainMenu(targetPlayerUUID).open(player);
        }));
    } catch (java.lang.Exception e) {
        com.expl0itz.worldwidechat.inventory.WWCInventoryManager.inventoryError(player, e);
    }
}
```

The issue was caused by calling `parseEnchantment()` on `XEnchantment` objects, which is not allowed. Instead, you can use the `matchXEnchantment()` method to get the desired `XEnchantment` object and then call `parseEnchantment()` on the result. Also, I added `clone()` calls when creating `ItemStack` instances to avoid modifying the original `ItemStack` instances.