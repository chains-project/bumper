Here's a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new IsString(
        String.format("Status: Downloaded newer image for %s", image),
        IsString::containsSubstring
    );
}
```

This patch uses a different Hamcrest matcher, `IsString`, which checks if a string contains a given substring. It also uses a method reference `IsString::containsSubstring` to specify the matching strategy.

Note that this patch assumes that the `IsString` matcher is available in your version of Hamcrest. If it's not, you may need to use a different matcher or upgrade your Hamcrest library.