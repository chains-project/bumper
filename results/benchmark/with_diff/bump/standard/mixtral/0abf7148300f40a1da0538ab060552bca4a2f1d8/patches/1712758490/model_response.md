private void prepareTextfieldWithBorder(final JRDesignTextElement textField, final ColumnStyle style) {
`float` lineWidth = style.getColBorder().getLineWidth();
textField.getLineBox().getPen().setLineWidth(lineWidth);
textField.getLineBox().getPen().setLineColor(style.getColBorder().getLineColor());
textField.getLineBox().getPen().setLineStyle(style.getColBorder().getLineStyle().getLineStyleEnum());
}