Here is a possible patch for the `imagePulled` method:

```java
private static Matcher<String> imagePulled(String image) {
    String format = String.format("Downloaded newer image for %s", image);
    return new CoreMatchers.<String>containsString(format);
}
```

This patch creates a separate variable `format` for the formatted string, which should resolve the compilation error.