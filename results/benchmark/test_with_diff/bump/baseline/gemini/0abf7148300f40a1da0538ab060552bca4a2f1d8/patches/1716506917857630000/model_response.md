```java
  private void prepareTextfieldWithBorder(final JRDesignTextElement textField, final ColumnStyle style)
	{
		final ColumnBorder border = style.getColBorder();
		if(border == null)
		{
			return;
		}
		
		// create a new JRPen object with the desired line width
		JRPen pen = new JRPen();
		pen.setLineWidth(border.getLineWidth());
		pen.setLineColor(border.getLineColor());
		pen.setLineStyle(border.getLineStyle().getLineStyleEnum());
		
		// set the pen of the text field's line box
		textField.getLineBox().setPen(pen);
	}
```