Here is the fixed version of the `failsToResolveInvalid` method:
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
The only change made is to create a variable `stringContains` for the `StringContains` matcher, and pass this variable to the `AllOf` constructor instead of the boolean and string arguments. This is because the `StringContains` constructor now only takes a single string argument, instead of a boolean and a string.