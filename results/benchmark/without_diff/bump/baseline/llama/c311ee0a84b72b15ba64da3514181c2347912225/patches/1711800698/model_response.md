Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringEndsWith(image)
    );
}
```
The patch creates a new `AllOf` matcher that combines two other matchers: `StringContains` and `StringEndsWith`. The `StringContains` matcher checks for the presence of the given string, and the `StringEndsWith` matcher checks that the string ends with the given image name.

The `AllOf` matcher is used to combine the two matchers, which will only pass if both matchers pass. This should fix the error and make the code compile-time safe.