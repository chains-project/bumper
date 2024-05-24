Here's a fixed version of the `failsToResolveInvalid` method that should resolve the error:

```java
@ParameterizedTest
@ValueSource(strings = {
        "",
        "a:b:c",
        ".123"
})
void failsToResolveInvalid(final String string) {
    final HamcrestMatcher<String> matcher = new AllOf<>(
            Arrays.asList(
                    new StringContains("Unsupported reference"),
                    new StringStartsWithIgnoringCase(string)
            )
    );
    final Throwable throwable = Assertions.assertThrows(
            IllegalStateException.class,
            () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(
            throwable.getMessage(),
            matcher
    );
}
```

In this version, I've created a `matcher` variable that combines the `AllOf` matcher with two `StringContains` matchers using the `and` method. The first `StringContains` matcher checks for the string "Unsupported reference", and the second `StringStartsWithIgnoringCase` matcher checks if the exception message starts with the given string (`string` parameter).

This should resolve the error caused by the change in the `StringContains` constructor.