Here is a potential patch for the failing client code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Downloaded newer image for %s", image)
    );
}
```

This patch removes the `Status:` prefix from the expected string, which may have been added in a dependency update. This allows the `StringContains` constructor to be applied to the given types.