Here is the proposed patch:
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
                    new StringStartsWith(true, "Unsupported reference"),
                    stringContains
                )
            )
        );
    }
```
I created a new variable `stringContains` to hold the `StringContains` matcher, and changed the `StringContains` constructor to only take a single argument. I also changed the `StringStartsWith` constructor to take a boolean argument for `isLenient`, since the `StringContains` constructor no longer takes a boolean argument.