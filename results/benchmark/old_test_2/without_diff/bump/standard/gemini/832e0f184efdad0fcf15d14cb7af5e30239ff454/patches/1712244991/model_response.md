```java
import org.bukkit.inventory.ItemStack;
import org.bukkit.inventory.meta.ItemMeta;
import org.bukkit.inventory.ItemFlag;
import org.bukkit.ChatColor;
import com.cryptomorin.xseries.XMaterial;
import com.expl0itz.worldwidechat.util.CommonDefinitions;

public static ItemStack getCommonButton(String buttonType, String[] args) {
    ItemStack pageButton = XMaterial.WHITE_STAINED_GLASS.parseItem();
    ItemMeta pageMeta = pageButton.getItemMeta();
    pageMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
    if (buttonType.equalsIgnoreCase("Previous")) {
        pageButton = XMaterial.RED_STAINED_GLASS.parseItem();
        pageMeta.setDisplayName(ChatColor.RED + CommonDefinitions.getMessage("wwcConfigGUIPreviousPageButton"));
    } else if (buttonType.equalsIgnoreCase("Next")) {
        pageButton = XMaterial.GREEN_STAINED_GLASS.parseItem();
        pageMeta.setDisplayName(ChatColor.GREEN + CommonDefinitions.getMessage("wwcConfigGUINextPageButton"));
    } else if (buttonType.equalsIgnoreCase("Page Number")) {
        pageButton = XMaterial.LILY_PAD.parseItem();
        pageMeta.setDisplayName(ChatColor.AQUA + CommonDefinitions.getMessage("wwcGUIPageNumber", args));
        if (args[0].equals("1")) {
            pageMeta.addEnchant(XMaterial.matchXEnchantment("power").get().getEnchantment(), 1, false);
        }
    } else {
        pageMeta.setDisplayName(ChatColor.RED + "Not a valid button! This is a bug, please report it.");
    }
    pageButton.setItemMeta(pageMeta);
    return pageButton;
}
```