Here is a fixed version of the `getCommonButton` method:
```java
  public static ItemStack getCommonButton(String buttonType, String[] args) {
		XMaterial material = null;
		ItemStack pageButton = XMaterial.WHITE_STAINED_GLASS.parseItem();
		ItemMeta pageMeta = pageButton.getItemMeta();
	