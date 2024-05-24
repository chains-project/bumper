Here's a possible patch for the failing client code:

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

The change is in the `StringContains` matcher, which now uses `StringStartsWith` instead of the removed `StringContains(boolean, String)` constructor. This ensures that the `StringContains` matcher only receives one argument, which is the expected substring. The `StringStartsWith` matcher checks if the actual string starts with the given substring, which should be sufficient for the test case.