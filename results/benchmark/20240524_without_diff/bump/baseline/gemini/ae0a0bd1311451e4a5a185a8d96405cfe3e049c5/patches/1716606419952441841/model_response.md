```java
private static Matcher<String> imagePulled(final String image) {
    // The original matcher was using StringContains, which is deprecated in Hamcrest 2.2.
    // We can use StringContainsIgnoringCase instead, which is a compatible replacement.
    return new StringContainsIgnoringCase(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```