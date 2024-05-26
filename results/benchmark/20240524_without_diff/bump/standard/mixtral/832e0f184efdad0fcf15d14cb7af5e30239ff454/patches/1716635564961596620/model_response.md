```java
@java.lang.Override
public void init(org.bukkit.entity.Player player, fr.minuskube.inv.content.InventoryContents contents) {
    com.expl0itz.worldwidechat.util.ActiveTranslator targetTranslator = main.getActiveTranscom.cryptomorin.xseries.XMaterial.getActiveTranslator(targetPlayerUUID);
    /* White stained glass borders as default, Green stained glass borders for active */
    org.bukkit.inventory.ItemStack customBorders = com.cryptomorin.xseries.XMaterial.WHITE_STAINED_GLASS_PANE.parseItem();
    org.bukkit.inventory.meta.ItemMeta borderMeta = customBorders.getItemMeta();
    borderMeta.setDisplayName(" ");
    customBorders.setItemMeta(borderMeta);
    contents.fillBorders(fr.minuskube.inv.ClickableItem.empty(customBorders));
    if (targetTranslator.getTranslatingChatOutgoing() || targetTranslator.getTranslatingChatIncoming()) {
        org.bukkit.inventory.ItemStack customBordersActive = com.cryptomorin.xseries.XMaterial.GREEN_STAINED_GLASS_PANE.parseItem();
        borderMeta = customBordersActive.getItemMeta();
        borderMeta.setDisplayName(" ");
        customBordersActive.setItemMeta(borderMeta);
        for (int i = 
```