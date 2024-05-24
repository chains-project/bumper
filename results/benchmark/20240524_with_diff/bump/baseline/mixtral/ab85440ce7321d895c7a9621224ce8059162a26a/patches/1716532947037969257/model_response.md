Here's a possible patch for the failing client code:

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

The changes I made are:

* Create a local variable `stringContains` of type `StringContains` to replace the argument `true` of the `StringContains` constructor.
* Move the argument `false` of the `StringContains` constructor to the `AllOf` constructor.

This way, the code uses the new constructor signature of `StringContains` and the test still works as expected.