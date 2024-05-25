Here is a fixed version of the method using a different Hamcrest matcher:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContainsIgnoringCase(
        String.format("downloaded newer image for %s", image)
    );
}
```

This version uses the `StringContainsIgnoringCase` matcher instead of `StringContains`, which should match the desired string regardless of case. This should resolve the error caused by the `StringContains` constructor not accepting the given argument types.