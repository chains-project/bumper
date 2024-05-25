Here's a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replace the `StringContains` constructor from `org.hamcrest.core` with the `containsString` method from `org.hamcrest.CoreMatchers`. This should fix the error message you encountered.