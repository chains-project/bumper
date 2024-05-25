Here's the proposed patch for the `imagePulled` method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image),
        StringContains.Containing.SUBSTRING
    );
}
```

The patch adds a `Containing` parameter to the `StringContains` constructor, which was added in a newer version of Hamcrest. This change should resolve the compilation error.