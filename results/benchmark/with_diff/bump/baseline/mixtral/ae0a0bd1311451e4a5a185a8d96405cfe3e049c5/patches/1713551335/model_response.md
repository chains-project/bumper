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
In this patch, I replaced the `StringContains` constructor that takes a boolean argument with the `StringStartsWith` matcher, which only takes a single string argument. This should resolve the compilation error caused by the changes in the library version.