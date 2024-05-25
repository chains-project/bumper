Here's a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image),
        "Status: Downloaded newer image for"
    );
}
```

In this patch, I added a third argument to the `StringContains` constructor, which is a regular expression to match. This allows us to match the desired substring while still satisfying the constructor's signature. The regular expression `"Status: Downloaded newer image for"` matches the beginning of the desired substring.