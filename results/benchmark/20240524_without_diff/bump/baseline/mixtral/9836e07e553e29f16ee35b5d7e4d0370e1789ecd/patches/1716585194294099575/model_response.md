Here's a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replace the `StringContains` constructor with `CoreMatchers.containsString`. This is because the `StringContains` constructor has been removed in the new version of the library. Instead, we can use `CoreMatchers.containsString` to achieve the same functionality.