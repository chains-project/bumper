Here's a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replaced the `StringContains` class with `containsString`, which is a new method added in the latest version of Hamcrest. This should fix the error message you received.