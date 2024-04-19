Here's a possible patch for the failing client code:

```java
@ParameterizedTest
@ValueSource(strings = {
        "",
        "a:b:c",
        ".123"
})
void failsToResolveInvalid(final String string) {
    final Matcher<String> matcher = new AllOf<>(
            Arrays.asList(
                    new StringContains("Unsupported reference"),
                    new StringContains(string)
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

The patch changes the way the `MatcherAssert.assertThat` method is called. Instead of passing a `Matcher` constructor with a list of `Matcher`s, it creates a single `Matcher` instance by chaining `Matcher`s using the `allOf` method. This way, the `Matcher` constructor with a boolean argument is no longer used, which fixes the error message.