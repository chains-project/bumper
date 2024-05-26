private void prepareTextfieldWithBorder(final JRDesignTextElement textField, final ColumnStyle style) {
```java
    final ColumnBorder border = style.getColBorder();
    if (border == null) {
        return;
    }
    float lineWidth = border.getLineWidth();
    textField.getLineBox().getPen().setLineWidth(lineWidth);
    textField.getLineBox().getPen().setLineColor(border.getLineColor());
    textField.getLineLineBox().getPen().setLineStyle(border.getLineStyle().getLineStyleEnum());
}
```