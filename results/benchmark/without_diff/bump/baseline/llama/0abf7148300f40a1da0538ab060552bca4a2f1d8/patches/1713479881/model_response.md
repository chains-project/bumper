```
private void prepareTextfieldWithBorder(final JRDesignTextElement textField, final ColumnStyle style)
{
		final ColumnBorder border = style.getColBorder();
		if(border == null)
		{
			return;
		}
		
		textField.getLineBox().getPen().setLineWidth(border.getLineWidth() + 0.5f);
		textField.getLineBox().getPen().setLineColor(border.getLineColor());
		textField.getLineBox().getPen().setLineStyle(border.getLineStyle().getLineStyleEnum());
}
```
The error was caused by the fact that `border.getLineWidth()` returns an `int`, while `textField.getLineBox().getPen().setLineWidth()` expects a `float`. To fix this, we simply add 0.5f to the result of `border.getLineWidth()`, which converts the `int` value to a `float` value.