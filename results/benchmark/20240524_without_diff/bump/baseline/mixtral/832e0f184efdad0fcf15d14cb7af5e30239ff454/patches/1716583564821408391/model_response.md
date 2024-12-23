Here's a proposed patch to fix the error:

```java
import org.bukkit.enchantments.Enchantment;
import org.bukkit.inventory.ItemFlag;
import org.bukkit.inventory.meta.ItemMeta;
import org.bukkit.material.MaterialData;

import java.util.Arrays;

public static ItemStack getCommonButton(String buttonType, String[] args) {
	ItemStack pageButton = MaterialData.fromData(0).createItemStack();
	ItemMeta pageMeta = pageButton.getItemMeta();
	pageMeta.addItemFlags(ItemFlag.HIDE_ENCHANTS);
	if (buttonType.equalsIgnoreCase("Previous")) {
		pageButton = new ItemStack(Material.RED_STAINED_GLASS);
		pageMeta.setDisplayName(ChatColor.RED
				+ CommonDefinitions.getMessage("wwcConfigGUIPreviousPageButton"));
	} else if (buttonType.equalsIgnoreCase("Next")) {
		pageButton = new ItemStack(Material.GREEN_STAINED_GLASS);
		pageMeta.setDisplayName(ChatColor.GREEN
				+ CommonDefinitions.getMessage("wwcConfigGUINextPageButton"));
	} else if (buttonType.equalsIgnoreCase("Page Number")) {
		pageButton = new ItemStack(Material.LILY_PAD);
		pageMeta.setDisplayName(ChatColor.AQUA
				+ CommonDefinitions.getMessage("wwcGUIPageNumber", args));
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

In this patch, I replaced the usage of `XMaterial` with `Material`, `XEnchantment` with `Enchantment`, and `XMaterial.parseItem()` with `MaterialData.fromData(0).createItemStack()`. Additionally, I replaced `XEnchantment.matchXEnchantment("power").get().parseEnchantment()` with `Enchantment.DAMAGE_ALL`. These changes should resolve the "cannot find symbol" error.