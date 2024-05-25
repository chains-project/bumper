Here is a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replaced the `StringContains` constructor from `org.hamcrest.core` with the `containsString` method from `org.hamcrest.CoreMatchers`. This method has the same functionality as the `StringContains` constructor, but it takes a `String` argument instead of a `CharSequence` argument. This change should fix the error message, which indicates that the `StringContains` constructor cannot be applied to a `String` argument.