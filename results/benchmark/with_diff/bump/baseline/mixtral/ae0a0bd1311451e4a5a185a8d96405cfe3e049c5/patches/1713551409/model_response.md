Here's the proposed patch for the failing client code:

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
    final HamcrestMatcher allOfMatcher = new AllOf<>(Arrays.asList(unsupportedReferenceMatcher, notContainingMatcher));
    final Throwable throwable = Assertions.assertThrows(
            IllegalStateException.class,
            () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(throwable.getMessage(), allOfMatcher);
}
```

In this patch, I created separate variables for the `StringContains` matchers and the `AllOf` matcher to make the code easier to understand. This way, the `StringContains` constructor is called with only one argument, which is required by the new library version.