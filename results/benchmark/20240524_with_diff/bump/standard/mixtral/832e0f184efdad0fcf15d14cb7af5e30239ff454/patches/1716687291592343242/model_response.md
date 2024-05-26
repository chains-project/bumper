Here's the patched method:

```java
import org.bukkit.enchantments.Enchantment;
import org.bukkit.inventory.ItemFlag;
import org.bukkit.inventory.ItemStack;
import org.bukkit.inventory.meta.ItemMeta;
import org.bukkit.material.MaterialData;
import com.cryptomorin.xseries.XMaterial;
import com.expl0itz.worldwidechat.util.CommonDefinitions;

public static ItemStack getCommonButton(String buttonType, String[] args) {
    MaterialData pageButton = XMaterial.WHITE_STAINED_GLASS.parseMaterial();
    ItemMeta pageMeta = pageButton.getItemMeta();
    pageMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
    if (buttonType.equalsIgnoreCase("Previous")) {
        pageButton = XMaterial.RED_STAINED_GLASS.parseMaterial();
        pageMeta.setDisplayName(ChatColor.RED + CommonDefinitions.getMessage("wwcConfigGUIPreviousPageButton"));
    } else if (buttonType.equalsIgnoreCase("Next")) {
        pageButton = XMaterial.GREEN_STAINED_GLASS.parseMaterial();
        pageMeta.setDisplayName(ChatColor.GREEN + CommonDefinitions.getMessage("wwcConfigGUINextPageButton"));
    } else if (buttonType.equalsIgnoreCase("Page Number")) {
        pageButton = XMaterial.LILY_PAD.parseMaterial();
        pageMeta.setDisplayName(ChatColor.AQUA + CommonDefinitions.getMessage("wwcGUIPageNumber", args));
        if (args[0].equals("1")) {
            pageMeta.addEnchant(Enchantment.DAMAGE_ALL, 1, false);
        }
    } else {
        pageMeta.setDisplayName(ChatColor.RED + "Not a valid button! This is a bug, please report it.");
    }
    pageButton.setItemMeta(pageMeta);
    return pageButton;
}
```

The main changes include:

- Replace `com.cryptomorin.xseries.XMaterial.parseItem()` with `XMaterial.parseMaterial()`
- Replace `com.cryptomorin.xseries.XEnchantment.getByName("DAMAGE_ALL").get()` with `Enchantment.DAMAGE_ALL`
- Replace `pageButton` variable type from `org.bukkit.inorganic.ItemStack` to `org.bukkit.material.MaterialData`
- Replace `pageButton` initialization with `XMaterial.WHITE_STAINED_GLASS.parseMaterial()` instead of `com.cryptomorin.xseries.XMaterial.WHITE_STAINED_GLASS.parseItem()`
- Remove the fully qualified imports for `ItemFlag`, `ItemStack`, `ItemMeta`, `MaterialData`, `ChatColor`, `Enchantment`, and `Enchantment.EnchantmentTarget`
- Replace `pageMeta.addEnchant(com.cryptomorin.xseries.XEnchantment.getByName("DAMAGE_ALL").get(), 1, false);` with `pageMeta.addEnchant(Enchantment.DAMAGE_ALL, 1, false);`