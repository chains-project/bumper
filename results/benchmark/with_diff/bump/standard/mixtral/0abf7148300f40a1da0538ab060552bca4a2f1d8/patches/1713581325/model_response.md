private void prepareTextfieldWithBorder(final JRDesignTextElement textField, final ColumnStyle style)
	{
		final ColumnBorder border = style.getColBorder();
		if(border == null)
		{
			return;
		}
		
		Number lineWidth = border.getLineWidth();
		textField.getLineBox().getPen().setLineWidth(lineWidth.floatValue());
		textField.getLineBox().getPen().setLineColor(border.getLineColor());
		textField.getLineBox().getPen().setLineStyle(border.getLineStyle().getLineStyleEnum());
	}