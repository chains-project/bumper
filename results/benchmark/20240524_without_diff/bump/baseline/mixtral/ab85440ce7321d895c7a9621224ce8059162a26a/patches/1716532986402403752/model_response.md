Here's a possible patch for the failing code:

```java
@ParameterizedTest
@ValueSource(strings = {
        "",
        "a:b:c",
        ".123"
})
void failsToResolveInvalid(final String string) {
    final HamcrestMatcher stringContains = new StringContains(string);
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

In this patch, we create a new `StringContains` matcher instance with the `string` parameter, and use it directly in the `AllOf` matcher instead of using a boolean value. This way, we avoid the error caused by the change in the `StringContains` constructor.