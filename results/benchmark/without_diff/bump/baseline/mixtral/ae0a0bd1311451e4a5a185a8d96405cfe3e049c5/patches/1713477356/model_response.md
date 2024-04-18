Here is a possible patch for the failing code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new IsString(
        String.format("Status: Downloaded newer image for %s", image),
        IsString::contains
    );
}
```

This patch uses the `IsString` matcher from Hamcrest, which has a `contains` method that can be used to check if a string contains a substring. The `IsString` matcher is a better fit for this use case than `StringContains`, as it is specifically designed to work with strings.

Note that this patch assumes that the Hamcrest library has been updated to a version that includes the `IsString` matcher. If the library has not been updated, then this patch will not work. In that case, you may need to find a different way to check if a string contains a substring, or you may need to update the library to a version that includes the `IsString` matcher.