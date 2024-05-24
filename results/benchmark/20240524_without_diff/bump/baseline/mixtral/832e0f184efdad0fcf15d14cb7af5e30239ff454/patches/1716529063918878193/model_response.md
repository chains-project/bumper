Here's the fixed `init` method. I had to remove the ternary operator used for setting `outgoingChatButton` and `incomingChatButton` since it was causing the syntax error. I created two separate `if` blocks for setting the buttons.

```java
@Override
public void init(Player player, InventoryContents contents) {
    ActiveTranslator targetTranslator = main.getActiveTranslator(targetPlayerUUID);

    /* White stained glass borders as default, Green stained glass borders for active */
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
        ItemStack outgoingChatButton;
        ItemMeta outgoingChatMeta;
        if (targetTranslator.getTranslatingChatOutgoing()) {
            outgoingChatButton = XMaterial.CHEST_MINECART.parseItem();
            outgoingChatMeta = outgoingChatButton.getItemMeta();
            outgoingChatMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
            Enchantment powerEnchantment = Enchantment.getById(16); // Increase this number if the power enchantment ID changes
            outgoingChatMeta.addEnchant(powerEnchantment, 1, false);
            outgoingChatMeta.setDisplayName(ChatColor.GREEN
                    + CommonDefinitions.getMessage("wwctGUIChatOutgoingButton"));
            outgoingChatButton.setItemMeta(outgoingChatMeta);
            contents.set(1, 3, ClickableItem.of(outgoingChatButton, e -> {
                String[] args = { main.getServer().getPlayer(UUID.fromString(targetPlayerUUID)).getName() };
                WWCTranslateChatOutgoing translateChatOutgoing = new WWCTranslateChatOutgoing((CommandSender) player, null, null, args);
                translateChatOutgoing.processCommand();
                getTranslateChatMenu(targetPlayerUUID).open(player);
            }));
        } else {
            outgoingChatButton = XMaterial.CHEST_MINECART.parseItem();
            outgoingChatMeta = outgoingChatButton.getItemMeta();
            outgoingChatMeta.setDisplayName(ChatColor.YELLOW
                    + CommonDefinitions.getMessage("wwctGUIChatOutgoingButton"));
            outgoingChatButton.setItemMeta(outgoingChatMeta);
            contents.set(1, 3, ClickableItem.of(outgoingChatButton, e -> {
                String[] args = { main.getServer().getPlayer(UUID.fromString(targetPlayerUUID)).getName() };
                WWCTranslateChatOutgoing translateChatOutgoing = new WWCTranslateChatOutgoing((CommandSender) player, null, null, args);
                translateChatOutgoing.processCommand();
                getTranslateChatMenu(targetPlayerUUID).open(player);
            }));
        }
    }

    if ((player.getUniqueId().toString().equals(targetPlayerUUID) && player.hasPermission("worldwidechat.wwctci")) || (!player.getUniqueId().toString().equals(targetPlayerUUID)) && player.hasPermission("worldwidechat.wwctci.otherplayers")) {
        ItemStack incomingChatButton;
        ItemMeta incomingChatMeta;
        if (targetTranslator.getTranslatingChatIncoming()) {
            incomingChatButton = XMaterial.MAP.parseItem();
            incomingChatMeta = incomingChatButton.getItemMeta();
            incomingChatMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
            Enchantment powerEnchantment = Enchantment.getById(16); // Increase this number if the power enchantment ID changes
            incomingChatMeta.addEnchant(powerEnchantment, 1, false);
            incomingChatMeta.setDisplayName(ChatColor.GREEN
                    + CommonDefinitions.getMessage("wwctGUIChatIncomingButton"));
            incomingChatButton.setItemMeta(incomingChatMeta);
            contents.set(1, 5, ClickableItem.of(incomingChatButton, e -> {
                String[] args = { main.getServer().getPlayer(UUID.fromString(targetPlayerUUID)).getName() };
                WWCTranslateChatIncoming translateChatIncoming = new WWCTranslateChatIncoming((CommandSender) player, null, null, args);
                translateChatIncoming.processCommand();
                getTranslateChatMenu(targetPlayerUUID).open(player);
            }));
        } else {
            incomingChatButton = XMaterial.MAP.parseItem();
            incomingChatMeta = incomingChatButton.getItemMeta();
            incomingChatMeta.setDisplayName(ChatColor.YELLOW
                    + CommonDefinitions.getMessage("wwctGUIChatIncomingButton"));
            incomingChatButton.setItemMeta(incomingChatMeta);
            contents.set(1, 5, ClickableItem.of(incomingChatButton, e -> {
                String[] args = { main.getServer().getPlayer(UUID.fromString(targetPlayerUUID)).getName() };
                WWCTranslateChatIncoming translateChatIncoming = new WWCTranslateChatIncoming((CommandSender) player, null, null, args);
                translateChatIncoming.processCommand();
                getTranslateChatMenu(targetPlayerUUID).open(player);
            }));
        }
    }
}
```