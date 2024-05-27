```java
private void prepareTextfieldWithBorder(final JRDesignTextElement textField, final ColumnStyle style) {
	final ColumnBorder border = style.getColBorder();
	if(border == null) {
		return;
	}
	
	final Float lineWidth = border.getLineWidth();
	if(lineWidth != null) {
		textField.getLineBox().getPen().setLineWidth(lineWidth.floatValue());
	}
	textField.getLineBox().getPen().setLineColor(border.getLineColor());
	textField.getLineBox().getPen().setLineStyle(border.getLineStyle().getLineStyleEnum());
}
```