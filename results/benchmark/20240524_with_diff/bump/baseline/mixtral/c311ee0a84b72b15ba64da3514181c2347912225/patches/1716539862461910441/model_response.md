Here is the proposed patch for the failing method:
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
                                new StringContains("Unsupported reference"),
                                stringContains
                        )
                )
        );
    }
```
The only change made is to create a separate variable for the `StringContains` matcher, and pass it directly to the `AllOf` constructor instead of wrapping it in a `new StringContains` call. This should resolve the error message regarding the incorrect number of arguments.