Here is a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replace the `StringContains` constructor with a call to `CoreMatchers.containsString`, which is a new method added in Hamcrest 2.1. This method has the same behavior as `StringContains`, but accepts a `String` argument instead of a `CharSequence`. This allows us to use the `String.format` method to construct the expected substring.