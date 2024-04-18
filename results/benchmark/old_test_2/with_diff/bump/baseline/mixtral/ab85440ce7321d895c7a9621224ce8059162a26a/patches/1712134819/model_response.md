Here's the fixed `imagePulled` method that should resolve the error:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(String.format("Status: Downloaded newer image for %s", image));
}
```

The issue was caused by passing `false` as the first argument, which was not required by the `StringContains` constructor. I have removed it to resolve the error.