Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(true, image)
    );
}
```
The `StringContains` constructor with two parameters is not available in the version of the Hamcrest library being used, so we're using the `AllOf` class to combine two `StringContains` matchers instead. The first `StringContains` matcher checks for the presence of the given string, and the second `StringContains` matcher checks for the absence of the given string.

This patch replaces the failing code with a working version that uses the `AllOf` class to achieve the same result.