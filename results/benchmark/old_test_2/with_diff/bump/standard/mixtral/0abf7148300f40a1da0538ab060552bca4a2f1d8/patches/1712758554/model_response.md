private void prepareTextfieldWithBorder(final JRDesignTextElement textField, final ColumnStyle style) {
`final float lineWidth = style.getColBorder().getLineWidth();`
if(border == null || lineWidth <= 0)
{
return;
}
textField.getLineBox().getPen().setLineWidth(lineWidth);
textField.getLineBox().getPen().setLineColor(border.getLineColor());
textField.getLineBox().getPen().setLineStyle(border.getLineStyle().getLineStyleEnum());
}