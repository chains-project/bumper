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

In this patch, I replaced the `StringContains` constructor with `StringStartsWith` to satisfy the new library version's constructor requirement. The `StringStartsWith` matcher checks if the given string starts with the specified substring, which should be sufficient for the test to pass.