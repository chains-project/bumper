Here's a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.stringContains(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replaced the `StringContains` constructor from the `org.hamcrest.core` package with the `stringContains` method from the `org.hamcrest.CoreMatchers` package. This should fix the error message you provided.