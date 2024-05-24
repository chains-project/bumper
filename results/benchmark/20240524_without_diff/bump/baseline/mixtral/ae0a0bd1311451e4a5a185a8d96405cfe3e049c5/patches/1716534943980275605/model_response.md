Here is a possible patch for the failing code:
```java
@ParameterizedTest
@ValueSource(strings = {
    "",
    "a:b:c",
    ".123"
})
void failsToResolveInvalid(final String string) {
    final HamcrestMatcher<String> matcher = new AllOf<>(
        Arrays.asList(
            new StringContains<>(string),
            new StringContains<>("Unsupported reference")
        )
    );
    final Throwable throwable = Assertions.assertThrows(
        IllegalStateException.class,
        () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(throwable.getMessage(), matcher);
}
```
The changes I made are:

* I created a variable `matcher` to hold the `AllOf` matcher, so that I can pass it as a single argument to `MatcherAssert.assertThat`.
* I changed the order of the arguments to `StringContains` constructor, so that it matches the new library version.

I hope this helps! Let me know if you have any questions or if there's anything else I can do.