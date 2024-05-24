```java
public void init(Player player, InventoryContents contents) {
    try {
        ItemStack customDefaultBorders = XMaterial.WHITE_STAINED_GLASS_PANE.parseItem();
        if (!main.getActiveTranslator(targetPlayerUUID).getUUID().equals("")) {
            customDefaultBorders = XMaterial.GREEN_STAINED_GLASS_PANE.parseItem();
        }
        ItemMeta defaultBorderMeta = customDefaultBorders.getItemMeta();
        defaultBorderMeta.setDisplayName(" ");
        customDefaultBorders.setItemMeta(defaultBorderMeta);
        contents.fillBorders(ClickableItem.empty(customDefaultBorders));

        ItemStack translationButton = XMaterial.COMPASS.parseItem();
        ItemMeta translationMeta = translationButton.getItemMeta();
        translationMeta.setDisplayName(CommonDefinitions.getMessage("wwctGUITranslationButton"));
        translationButton.setItemMeta(translationMeta);
        contents.set(2, 4, ClickableItem.of(translationButton, e -> {
            WWCTranslateGUISourceLanguage.getSourceLanguageInventory("", targetPlayerUUID).open(player);
        }));

        ActiveTranslator targetTranslator = main.getActiveTranslator(targetPlayerUUID);

        if (!main.getActiveTranslator(targetPlayerUUID).getUUID().equals("")) {
            translationMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
            translationMeta.addEnchant(Enchantment.getByName("power"), 1);
            translationMeta.setDisplayName(CommonDefinitions.getMessage("wwctGUIExistingTranslationButton"));
            List<String> outLore = new ArrayList<>();
            outLore.add(ChatColor.LIGHT_PURPLE + CommonDefinitions.getMessage("wwctGUIExistingTranslationInput", new String[]{ChatColor.LIGHT_PURPLE + "" + ChatColor.BOLD + targetTranslator.getInLangCode()}));
            outLore.add(ChatColor.LIGHT_PURPLE + CommonDefinitions.getMessage("wwctGUIExistingTranslationOutput", new String[]{ChatColor.LIGHT_PURPLE + "" + ChatColor.BOLD + targetTranslator.getOutLangCode()}));
            translationMeta.setLore(outLore);
            translationButton.setItemMeta(translationMeta);

            ItemStack stopButton = XMaterial.BARRIER.parseItem();
            ItemMeta stopMeta = stopButton.getItemMeta();
            stopMeta.setDisplayName(ChatColor.RED + CommonDefinitions.getMessage("wwctGUIStopButton"));
            stopButton.setItemMeta(stopMeta);
            contents.set(1, 4, ClickableItem.of(stopButton, e -> {
                String[] args;
                if (!targetPlayerUUID.equals("GLOBAL-TRANSLATE-ENABLED")) {
                    args = new String[]{main.getServer().getPlayer(UUID.fromString(targetPlayerUUID)).getName(), "stop"};
                } else {
                    args = new String[]{"stop"};
                }
                if (targetPlayerUUID.equals("GLOBAL-TRANSLATE-ENABLED")) {
                    WWCTranslate translate = new WWCGlobal((CommandSender) player, null, null, args);
                    translate.processCommand();
                } else {
                    WWCTranslate translate = new WWCTranslate((CommandSender) player, null, null, args);
                    translate.processCommand();
                }
                getTranslateMainMenu(targetPlayerUUID).open(player);
            });

            if (!targetPlayerUUID.equals("GLOBAL-TRANSLATE-ENABLED") && player.hasPermission("worldwidechat.wwctrl") && (player.hasPermission("worldwidechat.wwctrl.otherplayers") || player.getUniqueId().toString().equals(targetPlayerUUID))) {
                ConversationFactory rateConvo = new ConversationFactory(main).withModality(true).withFirstPrompt(new RateLimitConversation(targetTranslator));
                ItemStack rateButton = XMaterial.SLIME_BLOCK.parseItem();
                ItemMeta rateMeta = rateButton.getItemMeta();
                if (targetTranslator.getRateLimit() > 0) {
                    rateMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
                    rateMeta.addEnchant(Enchantment.getByName("power"), 1);
                    rateMeta.setDisplayName(ChatColor.GREEN + CommonDefinitions.getMessage("wwctGUIRateButton"));
                } else {
                    rateMeta.setDisplayName(ChatColor.YELLOW + CommonDefinitions.getMessage("wwctGUIRateButton"));
                }
                rateButton.setItemMeta(rateMeta);
                contents.set(1, 1, ClickableItem.of(rateButton, e -> {
                    rateConvo.buildConversation(player).begin();
                }));

                if (!targetPlayerUUID.equals("GLOBAL-TRANSLATE-ENABLED") && player.hasPermission("worldwidechat.wwctb") && (player.hasPermission("worldwidechat.wwctb.otherplayers") || player.getUniqueId().toString().equals(targetPlayerUUID))) {
                    ItemStack bookButton = XMaterial.WRITABLE_BOOK.parseItem();
                    ItemMeta bookMeta = bookButton.getItemMeta();
                    if (targetTranslator.getTranslatingBook()) {
                        bookMeta.setDisplayName(ChatColor.GREEN + CommonDefinitions.getMessage("wwctGUIBookButton"));
                        bookMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
                        bookMeta.addEnchant(Enchantment.getByName("power"), 1);
                    } else {
                        bookMeta.setDisplayName(ChatColor.YELLOW + CommonDefinitions.getMessage("wwctGUIBookButton"));
                    }
                    bookButton.setItemMeta(bookMeta);
                    contents.set(2, 1, ClickableItem.of(bookButton, e -> {
                        String[] args = {main.getServer().getPlayer(UUID.fromString(targetPlayerUUID)).getName()};
                        WWCTranslateBook translateBook = new WWCTranslateBook((CommandSender) player, null, null, args);
                        translateBook.processCommand();
                        getTranslateMainMenu(targetPlayerUUID).open(player);
                    }));

                    if (!targetPlayerUUID.equals("GLOBAL-TRANSLATE-ENABLED") && player.hasPermission("worldwidechat.wwcts") && (player.hasPermission("worldwidechat.wwcts.otherplayers") || player.getUniqueId().toString().equals(targetPlayerUUID))) {
                        ItemStack signButton = XMaterial.OAK_SIGN.parseItem();
                        ItemMeta signMeta = signButton.getItemMeta();
                        if (targetTranslator.getTranslatingSign()) {
                            signMeta.setDisplayName(ChatColor.GREEN + CommonDefinitions.getMessage("wwctGUISignButton"));
                            signMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
                            signMeta.addEnchant(Enchantment.getByName("power"), 1);
                        } else {
                            signMeta.setDisplayName(ChatColor.YELLOW + CommonDefinitions.getMessage("wwctGUISignButton"));
                        }
                        signButton.setItemMeta(signMeta);
                        contents.set(2, 7, ClickableItem.of(signButton, e -> {
                            String[] args = {main.getServer().getPlayer(UUID.fromString(targetPlayerUUID)).getName()};
                            WWCTranslateSign translateSign = new WWCTranslateSign((CommandSender) player, null, null, args);
                            translateSign.processCommand();
                            getTranslateMainMenu(targetPlayerUUID).open(player);
                        }));

                        if (!targetPlayerUUID.equals("GLOBAL-TRANSLATE-ENABLED") && player.hasPermission("worldwidechat.wwcti") && (player.hasPermission("worldwidechat.wwcti.otherplayers") || player.getUniqueId().toString().equals(targetPlayerUUID))) {
                            ItemStack itemButton = XMaterial.GRASS_BLOCK.parseItem();
                            ItemMeta itemMeta = itemButton.getItemMeta();
                            if (targetTranslator.getTranslatingItem()) {
                                itemMeta.setDisplayName(ChatColor.GREEN + CommonDefinitions.getMessage("wwctGUIItemButton"));
                                itemMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
                                itemMeta.addEnchant(Enchantment.getByName("power"), 1);
                            } else {
                                itemMeta.setDisplayName(ChatColor.YELLOW + CommonDefinitions.getMessage("wwctGUIItemButton"));
                            }
                            itemButton.setItemMeta(itemMeta);
                            contents.set(2, 6, ClickableItem.of(itemButton, e -> {
                                String[] args = {main.getServer().getPlayer(UUID.fromString(targetPlayerUUID)).getName()};
                                WWCTranslateItem translateItem = new WWCTranslateItem((CommandSender) player, null, null, args);
                                translateItem.processCommand();
                                getTranslateMainMenu(targetPlayerUUID).open(player);
                            }));

                            if (!targetPlayerUUID.equals("GLOBAL-TRANSLATE-ENABLED") && player.hasPermission("worldwidechat.wwcte") && (player.hasPermission("worldwidechat.wwcte.otherplayers") || player.getUniqueId().toString().equals(targetPlayerUUID))) {
                                ItemStack entityButton = XMaterial.NAME_TAG.parseItem();
                                ItemMeta entityMeta = entityButton.getItemMeta();
                                if (targetTranslator.getTranslatingEntity()) {
                                    entityMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
                                    entityMeta.addEnchant(Enchantment.getByName("power"), 1);
                                    entityMeta.setDisplayName(ChatColor.GREEN + CommonDefinitions.getMessage("wwctGUIEntityButton"));
                                } else {
                                    entityMeta.setDisplayName(ChatColor.YELLOW + CommonDefinitions.getMessage("wwctGUIEntityButton"));
                                }
                                entityButton.setItemMeta(entityMeta);
                                contents.set(2, 2, ClickableItem.of(entityButton, e -> {
                                    String[] args = {main.getServer().getPlayer(UUID.fromString(targetPlayerUUID)).getName()};
                                    WWCTranslateEntity translateEntity = new WWCTranslateEntity((CommandSender) player, null, null, args);
                                    translateEntity.processCommand();
                                    getTranslateMainMenu(targetPlayerUUID).open(player);
                                }));

                                if (!targetPlayerUUID.equals("GLOBAL-TRANSLATE-ENABLED") && ((targetPlayerUUID.equals(player.getUniqueId().toString()) && (player.hasPermission("worldwidechat.wwctco") || player.hasPermission("worldwidechat.wwctci"))) || (!targetPlayerUUID.equals(player.getUniqueId().toString()) && (player.hasPermission("worldwidechat.wwctco.otherplayers") || player.hasPermission("worldwidechat.wwctci.otherplayers")))) {
                                    ItemStack chatButton = XMaterial.PAINTING.parseItem();
                                    ItemMeta chatMeta = chatButton.getItemMeta();
                                    if (targetTranslator.getTranslatingChatOutgoing() || targetTranslator.getTranslatingChatIncoming()) {
                                        chatMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
                                        chatMeta.addEnchant(Enchantment.getByName("power"), 1);
                                        List<String> outLoreChat = new ArrayList<>();
                                        outLoreChat.add(ChatColor.LIGHT_PURPLE + CommonDefinitions.getMessage("wwctGUIExistingChatIncomingEnabled", new String[]{ChatColor.LIGHT_PURPLE + "" + ChatColor.BOLD + targetTranslator.getTranslatingChatIncoming()}));
                                        outLoreChat.add(ChatColor.LIGHT_PURPLE + CommonDefinitions.getMessage("wwctGUIExistingChatOutgoingEnabled", new String[]{ChatColor.LIGHT_PURPLE + "" + ChatColor.BOLD + targetTranslator.getTranslatingChatOutgoing()}));
                                        chatMeta.setLore(outLoreChat);
                                        chatMeta.setDisplayName(ChatColor.GREEN + CommonDefinitions.getMessage("wwctGUIChatButton"));
                                    } else {
                                        chatMeta.setDisplayName(ChatColor.YELLOW + CommonDefinitions.getMessage("wwctGUIChatButton"));
                                    }
                                    chatButton.setItemMeta(chatMeta);
                                    contents.set(3, 4, ClickableItem.of(chatButton, e -> {
                                        WWCTranslateGUIChatMenu.getTranslateChatMenu(targetPlayerUUID).open(player);
                                    }));
                                }
                            }
                        }
                    }
                }
            }
        }
    } catch (Exception e) {
        WWCInventoryManager.inventoryError(player, e);
    }
}
```