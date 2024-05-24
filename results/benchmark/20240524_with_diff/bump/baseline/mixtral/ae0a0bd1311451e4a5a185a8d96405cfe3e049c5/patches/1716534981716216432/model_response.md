Here is a possible patch for the failing method:
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
The only change is the creation of a separate `StringContains` matcher for the `string` parameter, so that it can be reused in the `AllOf` matcher. This way, the `StringContains` constructor is called with the correct number of arguments.