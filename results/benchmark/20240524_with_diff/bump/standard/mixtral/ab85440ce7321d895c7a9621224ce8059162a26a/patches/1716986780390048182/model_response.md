Here's the proposed patch:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.ref.ManifestRef.FromString(string).link().string());
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.Matchers.AllOf(java.util.Arrays.asList(new org.hamcrest.Matchers.StringContains.ContainingIgnoringCase(string), new org.hamcrest.Matchers.StringContains.ContainingIgnoringCase("Unsupported reference"))));
}
```

The change is to replace the `StringContains` constructor with `StringContains.ContainingIgnoringCase` constructor, and update the arguments accordingly.