Here's a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.stringContains(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, I replaced the usage of the `StringContains` constructor from `org.hamcrest.core` with the `stringContains` method from `org.hamcrest.CoreMatchers`. It seems that the `StringContains` constructor has been removed, and the `stringContains` method was added in its place. This change should fix the error message you encountered.