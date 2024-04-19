```
private void prepareTextfieldWithBorder(final JRDesignTextElement textField, final ColumnStyle style)
{
    final ColumnBorder border = style.getColBorder();
    if(border == null)
    {
        return;
    }
    float lineWidth = border.getLineWidth();
    textField.getLineBox().getPen().setLineWidth(lineWidth);
    textField.getLineBox().getPen().setLineColor(border.getLineColor());
    textField.getLineBox().getPen().setLineStyle(border.getLineStyle().getLineStyleEnum());
}
```

The error was caused by trying to set an integer value to a variable that expects a float value. Changing the variable to a float fixes the error.

The patch replaces the line `textField.getLineBox().getPen().setLineWidth(border.getLineWidth());` with `textField.getLineBox().getPen().setLineWidth(border.getLineWidth());`
This change ensures that the `setLineWidth()` method is passed a float value, which is what it expects, and not an integer value.

Additionally, the patch adds a variable `float lineWidth = border.getLineWidth();` to store the value of `border.getLineWidth()` in a float variable before passing it to `setLineWidth()` method.
This makes the code more readable and maintainable.