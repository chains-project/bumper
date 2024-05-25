Here's a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new org.hamcrest.CoreMatchers.StringContains(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we're using the fully-qualified name of the `StringContains` class to avoid any conflicts with other classes that might have the same name. We're also removing the `false` argument, which was causing the constructor mismatch error. This argument was deprecated in Hamcrest 2.0 and removed in Hamcrest 2.2, so it's possible that the version of Hamcrest you're using no longer supports it.