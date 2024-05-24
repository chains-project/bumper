Here's the updated method with the required changes:

```java
    @ParameterizedTest
    @ValueSource(strings = {
            "",
            "a:b:c",
            ".123"
    })
    void failsToResolveInvalid(final String string) {
        final HamcrestMatcher stringContains = StringContains.stringContains(string);
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

The only change made is creating a variable for the `StringContains` matcher, using the constructor that accepts a single `String` argument. This should resolve the error related to the mismatch in the number of arguments passed to the `StringContains` constructor.