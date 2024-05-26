Here's the patched method using the new library version:

```java
import org.bukkit.enchantments.Enchantment;
import org.bukkit.inventory.ItemFlag;
import org.bukkit.inventory.ItemStack;
import org.bukkit.inventory.meta.ItemMeta;
import org.bukkit.material.MaterialData;
import com.cryptomorin.xseries.XMaterial;
import com.expl0itz.worldwidechat.util.CommonDefinitions;

public static ItemStack getCommonButton(String buttonType, String[] args) {
    MaterialData pageButton = XMaterial.WHITE_STAINED_GLASS.getData();
    ItemMeta pageMeta = pageButton.toItemStack().getItemMeta();
    pageMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
    if (buttonType.equalsIgnoreCase("Previous")) {
        pageButton = XMaterial.RED_STAINED_GLASS.getData();
        pageMeta.setDisplayName(ChatColor.RED + CommonDefinitions.getMessage("wwcConfigGUIPreviousPageButton"));
    } else if (buttonType.equalsIgnoreCase("Next")) {
        pageButton = XMaterial.GREEN_STAINED_GLASS.getData();
        pageMeta.setDisplayName(ChatColor.GREEN + CommonDefinitions.getMessage("wwcConfigGUINextPageButton"));
    } else if (buttonType.equalsIgnoreCase("Page Number")) {
        pageButton = XMaterial.LILY_PAD.getData();
        pageMeta.setDisplayName(ChatColor.AQUA + CommonDefinitions.getMessage("wwcGUIPageNumber", args));
        if (args[0].equals("1")) {
            pageMeta.addEnchant(Enchantment.DAMAGE_ALL, 1, false);
        }
    } else {
        pageMeta.setDisplayName(ChatColor.RED + "Not a valid button! This is a bug, please report it.");
    }
    pageButton.setItemMeta(pageMeta);
    return pageButton.toItemStack();
}
```

The changes include using `MaterialData` instead of `ItemStack` for the `pageButton` variable and using `Enchantment` instead of `XEnchantment` for adding the enchantment in the "Page Number" case. The method `toItemStack()` is used to convert `MaterialData` to `ItemStack`.