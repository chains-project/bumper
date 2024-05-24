Here's a possible patch for the failing client code:

```java
    @ParameterizedTest
    @ValueSource(strings = {
        "",
        "a:b:c",
        ".123"
    })
    void failsToResolveInvalid(final String string) {
        final HamcrestMatcher matcher = new AllOf<>(
            Arrays.asList(
                new StringContains("Unsupported reference"),
                new StringContains(string)
            )
        );
        final Throwable throwable = Assertions.assertThrows(
            IllegalStateException.class,
            () -> new ManifestRef.FromString(string).link().string()
        );
        MatcherAssert.assertThat(throwable.getMessage(), matcher);
    }
```

The patch changes the way the `StringContains` matcher is created, so that it matches the new library version. Instead of passing a boolean value to the constructor, it now passes a string value. This allows the code to compile and run successfully.