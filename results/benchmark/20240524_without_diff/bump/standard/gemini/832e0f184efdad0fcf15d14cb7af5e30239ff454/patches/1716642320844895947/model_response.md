```java
@java.lang.Override
public void update(org.bukkit.entity.Player player, fr.minuskube.inv.content.InventoryContents contents) {
    if (targetPlayerUUID != null) {
        com.expl0itz.worldwidechat.inventory.WWCInventoryManager.checkIfPlayerIsMissing(player, targetPlayerUUID);
    } else {
        contents.setProperty("targetPlayerUUID", player.getUniqueId());
        contents.setProperty("targetPlayerName", player.getName());
        contents.setProperty("targetPlayerLanguage", player.locale());
    }
}
```