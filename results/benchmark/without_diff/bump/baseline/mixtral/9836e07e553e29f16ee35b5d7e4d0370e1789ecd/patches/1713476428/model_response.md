Here's the proposed patch to fix the error:

```java
private static Matcher<String> imagePulled(final String image) {
    return new PatternMatcher(
        "Status: Downloaded newer image for " + image,
        Pattern.LITERAL
    );
}
```

In this patch, we replace the `StringContains` matcher with a `PatternMatcher` that checks if the given string matches the expected format. This should fix the error caused by the `StringContains` constructor not being applicable to the given types.