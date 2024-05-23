```java
private void prepareTextfieldWithBorder(final JRDesignTextElement textField, final ColumnStyle style)
	{
		final ColumnBorder border = style.getColBorder();
		if(border == null)
		{
			return;
		}
		
		// get the pen from the line box
		final JRPen pen = textField.getLineBox().getPen();
		
		// set the line width using the appropriate method
		if (pen instanceof JRBasePen) {
			((JRBasePen) pen).setLineWidth(border.getLineWidth());
		} else {
			pen.setLineWidth(Float.valueOf(border.getLineWidth()));
		}
		
		// set the line color
		pen.setLineColor(border.getLineColor());
		
		// set the line style
		pen.setLineStyle(border.getLineStyle().getLineStyleEnum());
	}
```