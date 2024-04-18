Here is a fixed version of the method using a different Hamcrest matcher, `StringMatches`, which takes a regular expression:

```java
private static Matcher<String> imagePulled(final String image) {
    String regex = String.format("Downloaded newer image for %s$", image);
    return new StringMatches(Pattern.compile(regex));
}
```
This version uses a regular expression that matches the end of the line (`$`) after the image name, to ensure that the match is only found if the image name is at the end of the line.

Note that `StringMatches` is a matcher provided by Hamcrest, so there should be no need to import any additional libraries.

The `StringContains` matcher is not flexible enough for this use case, since it only checks if a substring is present anywhere in the target string. By using `StringMatches` with a regular expression, we can be more precise about what we're checking for.