Here's the updated `failsToResolveInvalid` method with the required changes:

```java
@ParameterizedTest
@ValueSource(strings = {
        "",
        "a:b:c",
        ".123"
})
void failsToResolveInvalid(final String string) {
    final HamcrestMatcher contains = new StringContains(string);
    final Throwable throwable = Assertions.assertThrows(
            IllegalStateException.class,
            () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(
            throwable.getMessage(),
            new AllOf<>(
                    Arrays.asList(
                            new StringContains(true, "Unsupported reference"),
                            contains
                    )
            )
    );
}
```

The change includes creating a `StringContains` Hamcrest matcher variable and using it directly in the `AllOf` matcher. This way, the error related to the incorrect number of arguments for `StringContains` is resolved.