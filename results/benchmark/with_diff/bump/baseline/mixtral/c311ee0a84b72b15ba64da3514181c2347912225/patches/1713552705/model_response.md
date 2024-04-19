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

In this patch, I replaced the `StringContains` constructor with `StringStartsWith` constructor, which takes only one argument, to match the updated library version. This should resolve the compilation error.