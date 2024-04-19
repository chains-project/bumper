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
The change I made is to replace the `StringContains` matcher with a `StringStartsWith` matcher. This is because the `StringContains` constructor that takes a boolean flag as its first argument has been removed in the new version of the library. Instead, you can use the `StringStartsWith` matcher to check if the message starts with a given string.