```java
private void prepareTextfieldWithBorder(final JRDesignTextElement textField, final ColumnStyle style) {
	final ColumnBorder border = style.getColBorder();
	if (border == null) {
		return;
	}

	// Get the line width as a float
	float lineWidth = border.getLineWidth();

	// Set the line width of the text field's pen
	textField.getLineBox().getPen().setLineWidth(lineWidth);

	// Set the line color of the text field's pen
	textField.getLineBox().getPen().setLineColor(border.getLineColor());

	// Set the line style of the text field's pen
	textField.getLineBox().getPen().setLineStyle(border.getLineStyle().getLineStyleEnum());
}
```