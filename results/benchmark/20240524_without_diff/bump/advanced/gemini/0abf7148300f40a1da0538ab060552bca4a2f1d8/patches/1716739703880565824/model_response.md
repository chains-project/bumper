```java
private void prepareTextfieldWithBorder(final JRDesignTextElement textField, final ColumnStyle style)
	{
		final ColumnBorder border = style.getColBorder();
		if(border == null)
		{
			return;
		}
		
		final float lineWidth = border.getLineWidth();
		final int lineColor = border.getLineColor();
		final int lineStyle = border.getLineStyle().getLineStyleEnum();
		
		textField.getLineBox().getPen().setLineWidth(lineWidth);
		textField.getLineBox().getPen().setLineColor(lineColor);
		textField.getLineBox().getPen().setLineStyle(lineStyle);
	}
```