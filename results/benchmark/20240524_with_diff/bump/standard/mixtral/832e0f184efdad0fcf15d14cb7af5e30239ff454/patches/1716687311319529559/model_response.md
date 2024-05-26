Here is the patched method:

```java
import org.bukkit.Bukkit;
import org.bukkit.enchantments.Enchantment;
import org.bukkit.inventory.ItemFlag;
import org.bukkit.inventory.ItemStack;
import org.bukkit.inventory.meta.ItemMeta;
import org.bukkit.material.MaterialData;

public static ItemStack getCommonButton(String buttonType, String[] args) {
    MaterialData pageButtonData = Bukkit.getUnsafe().getMaterialData("STAINED_GLASS_PANE").toMaterialData();
    ItemStack pageButton = new ItemStack(pageButtonData);
    ItemMeta pageMeta = pageButton.getItemMeta();
    pageMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
    if (buttonType.equalsIgnoreCase("Previous")) {
        pageButtonData = Bukkit.getUnsafe().getMaterialData("STAINED_GLASS_PANE").toMaterialData().setColor(org.bukkit.DyeColor.RED);
    } else if (buttonType.equalsIgnoreCase("Next")) {
        pageButtonData = Bukkit.getUnsafe().getMaterialData("STAINED_GLASS_PANE").toMaterialData().setColor(org.bukkit.DyeColor.GREEN);
    } else if (buttonType.equalsIgnoreCase("Page Number")) {
        pageButtonData = Bukkit.getUnsafe().getMaterialData("LILY_PAD");
        if (args[0].equals("1")) {
            pageMeta.addEnchant(Enchantment.DAMAGE_ALL, 1, false);
        }
    } else {
        pageMeta.setDisplayName(org.bukkit.ChatColor.RED + "Not a valid button! This is a bug, please report it.");
    }
    pageMeta.setDisplayName(org.bukkit.ChatColor.AQUA + com.expl0itz.worldwidechat.util.CommonDefinitions.getMessage("wwcGUIPageNumber", args));
    pageButton.setItemMeta(pageMeta);
    return pageButton;
}
```

This patch removes the usage of the `com.cryptomorin.xseries` library, which was removed in the new version. Instead, it uses the `Bukkit` API to create the `ItemStack`s and `ItemMeta`s. The `MaterialData` class is used to set the color of the stained glass panes, and the `Enchantment` class is used to add the enchantment to the page button. The `getMessage` method is assumed to be unchanged and is used as is.