Here's a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.stringContains(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replaced the `StringContains` class from `org.hamcrest.core` with `CoreMatchers.stringContains` from the same package. This is because the `StringContains` constructor is no longer available in the updated version of the Hamcrest library.