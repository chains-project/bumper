Here's a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replaced the `StringContains` constructor with `CoreMatchers.containsString`. The `StringContains` constructor is no longer available in newer versions of Hamcrest, and has been replaced with the `CoreMatchers.containsString` method. This method has the same functionality as the `StringContains` constructor, and can be used as a drop-in replacement.