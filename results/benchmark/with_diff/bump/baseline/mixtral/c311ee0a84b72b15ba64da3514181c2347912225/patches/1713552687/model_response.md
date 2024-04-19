Here's the updated `failsToResolveInvalid` method that should fix the error:

```java
@ParameterizedTest
@ValueSource(strings = {
        "",
        "a:b:c",
        ".123"
})
void failsToResolveInvalid(final String string) {
    final HamcrestMatcher unsupportedReference = new StringContains("Unsupported reference");
    final HamcrestMatcher notContainingString = new StringContains(string);
    final HamcrestMatcher allOfMatcher = new AllOf<>(Arrays.asList(unsupportedReference, notContainingString));
    final Throwable throwable = Assertions.assertThrows(
            IllegalStateException.class,
            () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(throwable.getMessage(), allOfMatcher);
}
```

In the original code, the `StringContains` constructor was being called with two arguments, which caused the error. To fix the issue, I created separate `HamcrestMatcher` variables for each of the conditions and then used them to create an `AllOf` matcher that checks for both conditions. This should fix the error and allow the test to pass.