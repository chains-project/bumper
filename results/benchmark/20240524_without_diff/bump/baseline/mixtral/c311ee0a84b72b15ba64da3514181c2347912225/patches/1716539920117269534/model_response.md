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
            new StringContains<>("Unsupported reference"),
            new StringContains<>(string)
        )
    );
    final Throwable throwable = Assertions.assertThrows(
        IllegalStateException.class,
        () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(throwable.getMessage(), matcher);
}
```

The issue is caused by the fact that the `StringContains` constructor expects a single `String` argument, while it was called with two arguments - a `boolean` and a `String`.

In this fixed version, I created a `HamcrestMatcher` variable called `matcher` that combines the two `StringContains` conditions using the `AllOf` matcher. This allows the `MatcherAssert.assertThat` method to take a single `HamcrestMatcher` argument, resolving the error.