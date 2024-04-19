Here is a possible patch for the failing client code:

```java
@ParameterizedTest
@ValueSource(strings = {
    "",
    "a:b:c",
    ".123"
})
void failsToResolveInvalid(final String string) {
    final Throwable throwable = Assertions.assertThrows(
        IllegalStateException.class,
        () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(
        throwable.getMessage(),
        new AllOf<>(
            Arrays.asList(
                new StringContains("Unsupported reference"),
                new StringStartsWith(string)
            )
        )
    );
}
```

This patch removes the `true` argument from the `StringContains` constructor and replaces it with a `StringStartsWith` matcher to satisfy the new library version.