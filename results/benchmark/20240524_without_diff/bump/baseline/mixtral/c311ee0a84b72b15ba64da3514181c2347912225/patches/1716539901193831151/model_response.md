Here's the patched method that should fix the error:

```java
    @ParameterizedTest
    @ValueSource(strings = {
        "",
        "a:b:c",
        ".123"
    })
    void failsToResolveInvalid(final String string) {
        final HamcrestMatcher stringContainsMatcher = new StringContains(string);
        final Throwable throwable = Assertions.assertThrows(
            IllegalStateException.class,
            () -> new ManifestRef.FromString(string).link().string()
        );
        MatcherAssert.assertThat(
            throwable.getMessage(),
            new AllOf<>(
                Arrays.asList(
                    new StringContains(true, "Unsupported reference"),
                    stringContainsMatcher
                )
            )
        );
    }
```

The only change made is to create a separate variable for the `StringContains` matcher, which is then passed to the `AllOf` constructor. This avoids the error message caused by passing a boolean value as the second argument to `StringContains`.