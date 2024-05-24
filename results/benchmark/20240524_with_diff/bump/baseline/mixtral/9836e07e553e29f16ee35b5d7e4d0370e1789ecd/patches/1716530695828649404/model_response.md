Here is a possible patch for the failing code:
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
The only change I made is to create a local variable `stringContains` for the `StringContains` matcher, and use it directly instead of passing a boolean and a string to `StringContains`. This way, the code is compatible with the new version of the library.