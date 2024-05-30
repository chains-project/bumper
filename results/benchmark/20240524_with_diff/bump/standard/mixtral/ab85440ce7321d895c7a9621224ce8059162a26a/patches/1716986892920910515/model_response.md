Here is the proposed patch for the failing client code:
```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.ref.ManifestRef.FromString(string).link().string());
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.MatcherAssert.MatchesPattern(new java.util.regex.Pattern("Unsupported reference.*"+string+".*"), "Unsupported reference"));
}
```
The failure is caused by the change in the `StringContains` constructor, which now requires only a single `String` argument instead of a `boolean` and a `String`. To fix the issue, I replaced the `StringContains` matcher with a `MatchesPattern` matcher, which allows us to use a regular expression to check if the exception message contains the unsupported reference and the given `string`.