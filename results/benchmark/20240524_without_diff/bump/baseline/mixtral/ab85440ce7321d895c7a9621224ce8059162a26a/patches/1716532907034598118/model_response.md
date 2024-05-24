Here's a possible patch for the failing client code:

```java
    @ParameterizedTest
    @ValueSource(strings = {
            "",
            "a:b:c",
            ".123"
    })
    void failsToResolveInvalid(final String string) {
        final HamcrestMatcher<String> matcher = new StringContains(string);
        final Throwable throwable = Assertions.assertThrows(
                IllegalStateException.class,
                () -> new ManifestRef.FromString(string).link().string()
        );
        MatcherAssert.assertThat(
                throwable.getMessage(),
                new AllOf<>(
                        Arrays.asList(
                                new StringStartsWith("Unsupported reference"),
                                matcher
                        )
                )
        );
    }
```

The patch creates a `StringContains` matcher variable to avoid passing the boolean argument, which is no longer supported in the new library version. It also changes the `StringContains` constructor argument from `true` to a `StringStartsWith` matcher, which is a new method added in the new library version. This way, the code can still check if the error message starts with the string "Unsupported reference".