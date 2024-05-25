Here's a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replaced the `StringContains` constructor with `CoreMatchers.containsString`. This is because the `StringContains` constructor has been removed in the new version of the library, and replaced with `CoreMatchers.containsString`. This should fix the error message you provided.