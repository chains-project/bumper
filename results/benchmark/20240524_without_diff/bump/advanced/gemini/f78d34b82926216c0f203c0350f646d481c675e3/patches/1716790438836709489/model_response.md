```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import ml.peya.config.Config;
import ml.peya.plugins.Objects.Decorations;
import ml.peya.plugins.Objects.Player;
import ml.peya.plugins.Objects.PlayerData;
import ml.peya.plugins.Utils.Utils;
import net.milkbowl.vault.economy.Economy;
import net.milkbowl.vault.economy.EconomyResponse;
import org.bukkit.Bukkit;
import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.World;
import org.bukkit.block.Block;
import org.bukkit.configuration.file.FileConfiguration;
import org.bukkit.configuration.file.YamlConfiguration;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.block.Action;
import org.bukkit.event.player.PlayerInteractEvent;
import org.bukkit.inventory.ItemStack;
import org.bukkit.inventory.meta.ItemMeta;

public class Decorations implements Listener {
    private static FileConfiguration config = YamlConfiguration.loadConfiguration(Paths.get("plugins/PeyangSuperbAntiCheat/config.yml").toFile());
    private static Economy economy = (Economy) Bukkit.getServer().getServicesManager().getRegistration(Economy.class).getProvider();

    public static void init() {
        Bukkit.getPluginManager().registerEvents(new Decorations(), Bukkit.getPluginManager().getPlugin("PeyangSuperbAntiCheat"));
        if (!Files.exists(Paths.get("plugins/PeyangSuperbAntiCheat/decorations.yml"))) {
            try {
                Files.createFile(Paths.get("plugins/PeyangSuperbAntiCheat/decorations.yml"));
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    @EventHandler
    public void onPlayerInteract(PlayerInteractEvent event) {
        Player player = event.getPlayer();
        PlayerData playerData = PlayerData.getPlayerData(player);
        ItemStack itemStack = event.getItem();
        if (itemStack != null && itemStack.hasItemMeta() && itemStack.getItemMeta().hasDisplayName()) {
            String displayName = itemStack.getItemMeta().getDisplayName();
            if (displayName.startsWith("§a§l[§6§lPeyangSuperbAntiCheat§a§l]")) {
                event.setCancelled(true);
                if (displayName.equals("§a§l[§6§lPeyangSuperbAntiCheat§a§l] §b§lDecorations")) {
                    if (playerData.hasPermission("psac.decorations")) {
                        player.openInventory(Decorations.getDecorationsInventory());
                    } else {
                        player.sendMessage(Utils.getPrefix() + "§cYou do not have permission to use this command.");
                    }
                } else if (displayName.startsWith("§a§l[§6§lPeyangSuperbAntiCheat§a§l] §b§lDecoration - ")) {
                    String decorationName = displayName.substring(27);
                    if (playerData.hasPermission("psac.decorations." + decorationName.toLowerCase())) {
                        if (event.getAction() == Action.LEFT_CLICK_AIR || event.getAction() == Action.LEFT_CLICK_BLOCK) {
                            if (economy.has(player, config.getDouble("decorations." + decorationName + ".price"))) {
                                EconomyResponse economyResponse = economy.withdrawPlayer(player, config.getDouble("decorations." + decorationName + ".price"));
                                if (economyResponse.transactionSuccess()) {
                                    player.sendMessage(Utils.getPrefix() + "§aYou have purchased the decoration §b" + decorationName + "§a for §b" + economyResponse.amount + economyResponse.currencyName + "§a.");
                                    playerData.addDecoration(decorationName);
                                    player.getInventory().setItem(event.getHand(), new ItemStack(Material.AIR));
                                } else {
                                    player.sendMessage(Utils.getPrefix() + "§cAn error occurred while purchasing the decoration. Please try again later.");
                                }
                            } else {
                                player.sendMessage(Utils.getPrefix() + "§cYou do not have enough money to purchase this decoration.");
                            }
                        } else if (event.getAction() == Action.RIGHT_CLICK_AIR || event.getAction() == Action.RIGHT_CLICK_BLOCK) {
                            if (playerData.hasDecoration(decorationName)) {
                                player.openInventory(Decorations.getDecorationInventory(decorationName));
                            } else {
                                player.sendMessage(Utils.getPrefix() + "§cYou do not have this decoration.");
                            }
                        }
                    } else {
                        player.sendMessage(Utils.getPrefix() + "§cYou do not have permission to use this decoration.");
                    }
                }
            }
        }
    }

    public static org.bukkit.inventory.Inventory getDecorationsInventory() {
        org.bukkit.inventory.Inventory inventory = Bukkit.createInventory(null, 54, "§a§lPeyangSuperbAntiCheat §b§lDecorations");
        List<String> decorations = config.getStringList("decorations");
        for (int i = 0; i < decorations.size(); i++) {
            String decorationName = decorations.get(i);
            ItemStack itemStack = new ItemStack(Material.valueOf(config.getString("decorations." + decorationName + ".item")));
            ItemMeta itemMeta = itemStack.getItemMeta();
            itemMeta.setDisplayName("§a§l[§6§lPeyangSuperbAntiCheat§a§l] §b§lDecoration - " + decorationName);
            List<String> lore = new ArrayList<>();
            lore.add("§7Price: §b" + config.getDouble("decorations." + decorationName + ".price") + economy.currencyName());
            lore.add("§7Description: §b" + config.getString("decorations." + decorationName + ".description"));
            itemMeta.setLore(lore);
            itemStack.setItemMeta(itemMeta);
            inventory.setItem(i, itemStack);
        }
        return inventory;
    }

    public static org.bukkit.inventory.Inventory getDecorationInventory(String decorationName) {
        org.bukkit.inventory.Inventory inventory = Bukkit.createInventory(null, 54, "§a§lPeyangSuperbAntiCheat §b§lDecoration - " + decorationName);
        ItemStack itemStack = new ItemStack(Material.valueOf(config.getString("decorations." + decorationName + ".item")));
        ItemMeta itemMeta = itemStack.getItemMeta();
        itemMeta.setDisplayName("§a§l[§6§lPeyangSuperbAntiCheat§a§l] §b§lDecoration - " + decorationName);
        List<String> lore = new ArrayList<>();
        lore.add("§7Price: §b" + config.getDouble("decorations." + decorationName + ".price") + economy.currencyName());
        lore.add("§7Description: §b" + config.getString("decorations." + decorationName + ".description"));
        itemMeta.setLore(lore);
        itemStack.setItemMeta(itemMeta);
        inventory.setItem(4, itemStack);
        ItemStack itemStack2 = new ItemStack(Material.BARRIER);
        ItemMeta itemMeta2 = itemStack2.getItemMeta();
        itemMeta2.setDisplayName("§c§lDelete Decoration");
        itemStack2.setItemMeta(itemMeta2);
        inventory.setItem(49, itemStack2);
        return inventory;
    }

    @EventHandler
    public void onInventoryClick(org.bukkit.event.inventory.InventoryClickEvent event) {
        Player player = (Player) event.getWhoClicked();
        PlayerData playerData = PlayerData.getPlayerData(player);
        org.bukkit.inventory.Inventory inventory = event.getInventory();
        if (inventory.getTitle().startsWith("§a§lPeyangSuperbAntiCheat §b§lDecorations")) {
            event.setCancelled(true);
            if (event.getCurrentItem() != null && event.getCurrentItem().hasItemMeta() && event.getCurrentItem().getItemMeta().hasDisplayName()) {
                String displayName = event.getCurrentItem().getItemMeta().getDisplayName();
                if (displayName.startsWith("§a§l[§6§lPeyangSuperbAntiCheat§a§l] §b§lDecoration - ")) {
                    String decorationName = displayName.substring(27);
                    if (playerData.hasPermission("psac.decorations." + decorationName.toLowerCase())) {
                        player.openInventory(Decorations.getDecorationInventory(decorationName));
                    } else {
                        player.sendMessage(Utils.getPrefix() + "§cYou do not have permission to use this decoration.");
                    }
                }
            }
        } else if (inventory.getTitle().startsWith("§a§lPeyangSuperbAntiCheat §b§lDecoration - ")) {
            event.setCancelled(true);
            if (event.getCurrentItem() != null && event.getCurrentItem().hasItemMeta() && event.getCurrentItem().getItemMeta().hasDisplayName()) {
                String displayName = event.getCurrentItem().getItemMeta().getDisplayName();
                if (displayName.equals("§c§lDelete Decoration")) {
                    if (playerData.hasPermission("psac.decorations.delete")) {
                        String decorationName = inventory.getTitle().substring(27);
                        playerData.removeDecoration(decorationName);
                        player.sendMessage(Utils.getPrefix() + "§aYou have deleted the decoration §b" + decorationName + "§a.");
                        player.closeInventory();
                    } else {
                        player.sendMessage(Utils.getPrefix() + "§cYou do not have permission to delete decorations.");
                    }
                }
            }
        }
    }

    @EventHandler
    public void onPlayerQuit(org.bukkit.event.player.PlayerQuitEvent event) {
        Player player = event.getPlayer();
        PlayerData playerData = PlayerData.getPlayerData(player);
        for (String decorationName : playerData.getDecorations()) {
            if (config.getBoolean("decorations." + decorationName + ".save")) {
                Path path = Paths.get("plugins/PeyangSuperbAntiCheat/decorations.yml");
                FileConfiguration fileConfiguration = YamlConfiguration.loadConfiguration(path.toFile());
                List<String> decorations = fileConfiguration.getStringList("decorations");
                if (!decorations.contains(decorationName)) {
                    decorations.add(decorationName);
                    fileConfiguration.set("decorations", decorations);
                    try {
                        fileConfiguration.save(path.toFile());
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
                World world = Bukkit.getWorld(config.getString("decorations." + decorationName + ".world"));
                Location location = new Location(world, config.getDouble("decorations." + decorationName + ".x"), config.getDouble("decorations." + decorationName + ".y"), config.getDouble("decorations." + decorationName + ".z"));
                Block block = location.getBlock();
                block.setType(Material.valueOf(config.getString("decorations." + decorationName + ".item")));
            }
        }
    }

    @EventHandler
    public void onPlayerJoin(org.bukkit.event.player.PlayerJoinEvent event) {
        Player player = event.getPlayer();
        PlayerData playerData = PlayerData.getPlayerData(player);
        for (String decorationName : playerData.getDecorations()) {
            if (config.getBoolean("decorations." + decorationName + ".save")) {
                World world = Bukkit.getWorld(config.getString("decorations." + decorationName + ".world"));
                Location location = new Location(world, config.getDouble("decorations." + decorationName + ".x"), config.getDouble("decorations." + decorationName + ".y"), config.getDouble("decorations." + decorationName + ".z"));
                Block block = location.getBlock();
                if (block.getType() != Material.valueOf(config.getString("decorations." + decorationName + ".item"))) {
                    playerData.removeDecoration(decorationName);
                    player.sendMessage(Utils.getPrefix() + "§cThe decoration §b" + decorationName + "§c has been removed because it was not found at its saved location.");
                }
            }
        }
    }
}
```