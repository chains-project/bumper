Here's the fixed version of the `imagePulled` method that should resolve the error:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(String.format("Status: Downloaded newer image for %s", image));
}
```

The issue was caused by passing an extra boolean argument `false` to the `StringContains` constructor. I removed this argument, and now the method should compile and work correctly with the new version of the library.