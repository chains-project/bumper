Here is a possible patch for the client code that takes into account the changes in the library version:
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
                                new StringContains("Unsupported reference"),
                                stringContains
                        )
                )
        );
    }
```
The patch creates a separate `StringContains` matcher for the `string` parameter, and uses it in the `AllOf` matcher. This way, the `StringContains` constructor is called with a single argument, which is consistent with the constructor signature in the new library version.