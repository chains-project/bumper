Here is a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new ContainsPattern(
        Pattern.compile(
            String.format("Status: Downloaded newer image for %s", image)
        )
    );
}
```

This patch replaces the `StringContains` matcher with the `ContainsPattern` matcher, which accepts a regular expression pattern instead of a plain string. This allows us to use the `Pattern.compile` method to create a pattern that can match the desired string.