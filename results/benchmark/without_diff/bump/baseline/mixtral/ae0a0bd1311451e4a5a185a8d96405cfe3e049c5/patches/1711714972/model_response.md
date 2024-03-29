Here is a fixed version of the method using a different Hamcrest matcher, `StringMatches`, which takes a regular expression as an argument:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringMatches(
        String.format(".*Downloaded newer image for %s", image)
    );
}
```
This code uses the `StringMatches` matcher which takes a regular expression as an argument, allowing us to match the desired log message. The regular expression `".*Downloaded newer image for .*"` will match any string that contains the substring "Downloaded newer image for " followed by any text.

This should fix the error because `StringMatches` takes a regular expression as an argument, whereas `StringContains` takes a plain string as an argument. The `StringContains` matcher is expecting a plain string, but it's getting a formatted string instead, which is causing the error. By using `StringMatches` instead, we can avoid this issue.