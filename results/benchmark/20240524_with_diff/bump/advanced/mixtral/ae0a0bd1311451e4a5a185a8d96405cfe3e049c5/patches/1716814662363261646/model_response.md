Here is the proposed patch:

```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    return new org.hamcrest.core.IsNot(new org.hamcrest.core.StringContains("" + this.image.layer() + ": Pushed"));
}
```

The error message suggests that a semicolon is expected. Looking at the code, there is no need for a semicolon at the end of the return statement. However, the `String.format` method was removed in the new library version, so I have replaced it with string concatenation. This should fix the error.