Here's a fixed version of the `failsToResolveInvalid` method that should resolve the error:

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

The only change I made was to replace the `StringContains` matcher with the `StringStartsWith` matcher, which should have the same effect but without the length mismatch error. This matcher checks if the given string starts with the specified substring.