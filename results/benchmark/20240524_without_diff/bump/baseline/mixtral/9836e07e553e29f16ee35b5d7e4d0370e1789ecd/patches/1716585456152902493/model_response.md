Here's a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.stringContains(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we're using the `stringContains` method from the `CoreMatchers` class, which is part of the Hamcrest library and should be available in the new version. This should fix the error message you're seeing.