Here is a fixed version of the method using a different Hamcrest matcher, `StringMatches`, which takes a regular expression as an argument:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringMatches(
        String.format(".*Status: Downloaded newer image for %s", image)
    );
}
```
This version of the method should work even if the `StringContains` constructor has been removed in the new version of the dependency, because it uses a different matcher that is still available. The regular expression `".*Status: Downloaded newer image for .*"` matches any string that contains the desired pattern.