Here is a fixed version of the method using a different Hamcrest matcher, `StringMatchesPattern`, which should work as a replacement for `StringContains`:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringMatchesPattern(
        String.format(".*Downloaded newer image for %s", image)
    );
}
```
Note that `StringMatchesPattern` uses a regular expression instead of a plain string, so the pattern needs to be wrapped with `.*` to match the entire line.

This solution assumes that the `StringMatchesPattern` matcher is available in the version of Hamcrest being used. If not, you may need to update the Hamcrest dependency to a version that includes this matcher.