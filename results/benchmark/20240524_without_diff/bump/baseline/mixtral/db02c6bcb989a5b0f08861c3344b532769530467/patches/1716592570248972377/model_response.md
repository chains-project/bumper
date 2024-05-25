Here's the proposed patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new org.hamcrest.CoreMatchers.StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, I replaced the `StringContains` constructor with `org.hamcrest.CoreMatchers.StringContains` to use the fully qualified name of the class. This should fix the error message you provided.