Here's a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.stringContains(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replace the `StringContains` class from `org.hamcrest.core` package with `CoreMatchers.stringContains` method from the same package. This method is added in newer versions of Hamcrest, so it should work with the updated dependency.