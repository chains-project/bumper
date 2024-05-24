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
                new StringStartsWithIgnoringCase(string)
            )
        );
        final Throwable throwable = Assertions.assertThrows(
            IllegalStateException.class,
            () -> new ManifestRef.FromString(string).link().string()
        );
        MatcherAssert.assertThat(throwable.getMessage(), matcher);
    }
```

The changes made are:

* Replace `new StringContains(true, "Unsupported reference")` with `new StringContains("Unsupported reference")`.
* Replace `new StringContains(false, string)` with `new StringStartsWithIgnoringCase(string)`.

Note: I assumed that the `StringStartsWithIgnoringCase` matcher is available in the new version of the library, as it was not explicitly marked as removed. If it's not available, you might need to implement your own matcher for this purpose.