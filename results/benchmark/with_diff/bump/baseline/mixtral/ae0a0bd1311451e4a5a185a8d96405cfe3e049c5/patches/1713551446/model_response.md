Here's a possible patch for the failing client code:

```java
@ParameterizedTest
@ValueSource(strings = {
        "",
        "a:b:c",
        ".123"
})
void failsToResolveInvalid(final String string) {
    final StringContains stringContains = new StringContains(string);
    final Throwable throwable = Assertions.assertThrows(
            IllegalStateException.class,
            () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(
            throwable.getMessage(),
            new AllOf<>(
                    Arrays.asList(
                            new StringContains(true, "Unsupported reference"),
                            stringContains
                    )
            )
    );
}
```

The only change made is to create a separate variable `stringContains` for the `StringContains` matcher. This allows us to pass the `string` argument without the extra `true` argument that was causing the compilation error. The `true` argument was not necessary in the original code, because the `StringContains` constructor with a single argument already sets the `isEqual` parameter to `true` by default.