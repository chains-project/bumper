Here's a fixed version of the `imagePulled` method that should resolve the error:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(String.format("Downloaded newer image for %s", image));
}
```

The error message indicates that the `StringContains` constructor requires only one argument, but the original code passed two arguments with a `false` boolean value. Therefore, we can simply remove the `false` argument to fix the error.