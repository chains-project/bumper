Here's a possible patch for the failing method:

```java
@ParameterizedTest
@ValueSource(strings = {
        "",
        "a:b:c",
        ".123"
})
void failsToResolveInvalid(final String string) {
    final HamcrestMatchers.StringContains stringContains = new HamcrestMatchers.StringContains(string);
    final Throwable throwable = Assertions.assertThrows(
            IllegalStateException.class,
            () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(
            throwable.getMessage(),
            AllOf.allOf(
                    new StringContains("Unsupported reference"),
                    stringContains
            )
    );
}
```

In this patch, we create a new `StringContains` matcher instance for the expected string value, and use it in the `allOf` matcher. This way, we avoid passing a boolean argument to the `StringContains` constructor.