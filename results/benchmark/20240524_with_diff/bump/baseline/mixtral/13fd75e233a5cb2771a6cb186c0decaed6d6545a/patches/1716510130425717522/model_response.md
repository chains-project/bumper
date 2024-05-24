Here's a possible patch for the failing client code:

```java
@ParameterizedTest
@ValueSource(strings = {
        "",
        "a:b:c",
        ".123"
})
void failsToResolveInvalid(final String string) {
    final HamcrestMatcher unsupportedReferenceMatcher = new StringContains("Unsupported reference");
    final HamcrestMatcher notContainingMatcher = new StringContains(string);
    final HamcrestMatcher allOfMatcher = AllOf.allOf(unsupportedReferenceMatcher, notContainingMatcher);
    final Throwable throwable = Assertions.assertThrows(
            IllegalStateException.class,
            () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(
            throwable.getMessage(),
            allOfMatcher
    );
}
```

In this patch, I created new variables for the `StringContains` matchers, and used the `allOf` method from the `MatcherAssert` class to combine them. This allows us to use the `StringContains` constructor that takes only a single `String` argument, which is compatible with the new library version.