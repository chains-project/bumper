Here's a proposed patch for the given code:

```java
import org.bukkit.enchantments.Enchantment;
import org.bukkit.inventory.ItemFlag;
import org.bukkit.inventory.meta.ItemMeta;
import org.bukkit.material.MaterialData;
import org.bukkit.plugin.Plugin;

import java.util.Arrays;

public static ItemStack getCommonButton(String buttonType, String[] args) {
    Plugin plugin = YourPlugin.getInstance();
    MaterialData pageButton = MaterialData.fromItemStack(XMaterial.WHITE_STAINED_GLASS.parseItem());
    ItemMeta pageMeta = pageButton.getItemMeta();
    pageMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
    if (buttonType.equalsIgnoreCase("Previous")) {
        pageButton = MaterialData.fromItemStack(XMaterial.RED_STAINED_GLASS.parseItem());
        pageMeta.setDisplayName(ChatColor.RED
                + CommonDefinitions.getMessage("wwcConfigGUIPreviousPageButton"));
    } else if (buttonType.equalsIgnoreCase("Next")) {
        pageButton = MaterialData.fromItemStack(XMaterial.GREEN_STAINED_GLASS.parseItem());
        pageMeta.setDisplayName(ChatColor.GREEN
                + CommonDefinitions.getMessage("wwcConfigGUINextPageButton"));
    } else if (buttonType.equalsIgnoreCase("Page Number")) {
        pageButton = MaterialData.fromItemStack(XMaterial.LILY_PAD.parseItem());
        pageMeta.setDisplayName(ChatColor.AQUA
                + CommonDefinitions.getMessage("wwcGUIPageNumber", args));
        if (args[0].equals("1")) {
            Enchantment enchantment = Enchantment.getByKey(plugin.getServer().createItemStack().addEnchantment(Enchantment.ARROW_DAMAGE, 1));
            pageMeta.addEnchant(enchantment, 1, false);
        }
    } else {
        pageMeta.setDisplayName(ChatColor.RED + "Not a valid button! This is a bug, please report it.");
    }
    pageButton.setItemMeta(pageMeta);
    return pageButton.toItemStack();
}
```

The changes made include using `MaterialData` instead of `XMaterial` and manually getting the enchantment by its key. This should resolve the issue with the external dependency update.