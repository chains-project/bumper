Here's a proposed patch for the code:

```java
import net.md_5.bungee.api.ChatColor;
import org.bukkit.enchantments.Enchantment;
import org.bukkit.inventory.ItemFlag;
import org.bukkit.inventory.ItemStack;
import org.bukkit.inventory.meta.ItemMeta;
import org.bukkit.material.MaterialData;
import xyz.xenondevs.invui.XMaterial;

import java.util.Arrays;
import java.util.List;

public static ItemStack getCommonButton(String buttonType, String[] args) {
    XMaterial material;
    if (buttonType.equalsIgnoreCase("Previous")) {
        material = XMaterial.RED_STAINED_GLASS;
    } else if (buttonType.equalsIgnoreCase("Next")) {
        material = XMaterial.GREEN_STAINED_GLASS;
    } else if (buttonType.equalsIgnoreCase("Page Number")) {
        material = XMaterial.LILY_PAD;
    } else {
        material = XMaterial.WHITE_STAINED_GLASS;
    }
    ItemStack pageButton = material.parseItem();
    ItemMeta pageMeta = pageButton.getItemMeta();
    pageMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);

    if (buttonType.equalsIgnoreCase("Page Number")) {
        pageMeta.setDisplayName(ChatColor.AQUA
                + CommonDefinitions.getMessage("wwcGUIPageNumber", args));
        if (args[0].equals("1")) {
            List<Enchantment> enchantments = pageMeta.getEnchants().keySet().stream().toList();
            if (!enchantments.contains(Enchantment.getByKey(new NamespacedKey(null, "power")))) {
                pageMeta.addEnchant(Enchantment.getByKey(new NamespacedKey(null, "power")), 1, false);
            }
        }
    } else {
        pageMeta.setDisplayName(ChatColor.valueOf(buttonType.toUpperCase()).toString()
                + CommonDefinitions.getMessage("wwcConfigGUIPageButton"));
    }
    pageButton.setItemMeta(pageMeta);
    return pageButton;
}
```

This code uses the `NamespacedKey` class to create a key for the enchantment, which has been added in a newer version of the library. It also uses `List<Enchantment>` to get the list of enchantments on the item, which has also been added in a newer version of the library.