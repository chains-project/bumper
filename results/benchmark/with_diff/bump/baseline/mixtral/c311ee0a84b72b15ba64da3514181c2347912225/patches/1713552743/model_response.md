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
                                new StringContains(true, "Unsupported reference"),
                                matcher
                        )
                )
        );
    }
```

In this patch, I created a new variable `matcher` of type `HamcrestMatcher<String>` that wraps the `StringContains` matcher for the `string` parameter. This way, the `StringContains` constructor is called with the correct number of arguments.

Note that the `HamcrestMatcher` interface is a part of the Hamcrest library, and it is not specific to the `StringContains` matcher. Therefore, it should be available in the new library version.