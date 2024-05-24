Here is the fixed method:

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
                    ImmutableList.of(
                            new StringContains("Unsupported reference"),
                            new StringContains(string)
                    )
            )
    );
}
```

The only change I made was to replace the varargs version of `StringContains` with the version that takes a list. This is because the `StringContains` constructor that takes a boolean and a string has been removed in the new library version.