```java
private void prepareTextfieldWithBorder(final JRDesignTextElement textField, final ColumnStyle style)
{
	final ColumnBorder border = style.getColBorder();
	if(border == null)
	{
		return;
	}
	
	textField.getLineBox().getPen().setLineWidth(new Float(border.getLineWidth()));
	textField.getLineBox().getPen().setLineColor(border.getLineColor());
	textField.getLineBox().getPen().setLineStyle(border.getLineStyle().getLineStyleEnum());
}
```