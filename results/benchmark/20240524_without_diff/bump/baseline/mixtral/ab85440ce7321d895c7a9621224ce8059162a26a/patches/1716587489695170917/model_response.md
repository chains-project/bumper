Here is the proposed patch:

```java
private static Matcher<String> imagePulled(final String image) {
    return new org.hamcrest.core.StringContains.StringStartsWith(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This patch replaces the `StringContains` constructor with the `StringStartsWith` constructor from the same `org.hamcrest.core` package. This constructor takes a single `String` argument, which is used to match the beginning of the target string. This should resolve the error message, which indicates that the `StringContains` constructor cannot be applied to the given argument.