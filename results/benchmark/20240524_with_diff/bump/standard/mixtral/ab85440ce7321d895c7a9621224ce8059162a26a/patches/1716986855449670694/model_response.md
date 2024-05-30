Here's the patched code that should fix the error:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.ref.ManifestRef.FromString(string).link().string());
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.MatcherAssert.MatchesPattern(new org.hamcrest.core.AllOf<>(java.util.Arrays.asList(new org.hamcrest.core.StringStartsWith(string), new org.hamcrest.core.StringEndsWith("Unsupported reference")))));
}
```

The change consists of replacing the `StringContains` matcher with a `MatchesPattern` matcher that takes a regular expression. This way, we can still check that the message starts and ends with the expected strings.