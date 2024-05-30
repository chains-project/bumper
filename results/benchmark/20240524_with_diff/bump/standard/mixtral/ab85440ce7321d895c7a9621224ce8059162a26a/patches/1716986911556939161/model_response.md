Here's the proposed patch for the client code:
```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.ref.ManifestRef.FromString(string).link().string());
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.MatcherAssert.MatchesPattern(new org.hamcrest.core.AllOf<>(java.util.Arrays.asList(new org.hamcrest.core.StringStartsWith.StringStartsWith(string + ":unsupported"), new org.hamcrest.core.StringContains.StringContains(string)))));
}
```
The patch replaces the `org.hamcrest.core.StringContains` matcher with a new `org.hamcrest.MatcherAssert.MatchesPattern` matcher that uses a regular expression pattern to match the expected message. This is necessary because the new version of the library has removed the overload of `StringContains` that takes a `boolean` parameter. The regular expression pattern is constructed dynamically using the `StringStartsWith` matcher and the `StringContains` matcher to achieve the same behavior as the original code.