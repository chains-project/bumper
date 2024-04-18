Here is a fixed version of the method using a different Hamcrest matcher, `StringMatchesPattern`, which should work as a replacement for `StringContains`:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringMatchesPattern(
        java.util.regex.Pattern.compile(
            String.format("Status: Downloaded newer image for %s", image)
        )
    );
}
```
This solution uses the `StringMatchesPattern` matcher in combination with a regular expression pattern to match the desired string. The `StringMatchesPattern` matcher was added in Hamcrest version 1.3, so it should be available in the new version.