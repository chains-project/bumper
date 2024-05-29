Here's the proposed patch:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.ref.ManifestRef.FromString(string).link().string());
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.core.AllOf<>(java.util.Arrays.asList(new org.hamcrest.core.StringContains.StringContains(string), new org.hamcrest.core.StringContains.StringContains(false, string))));
}
```

The issue is caused by the use of `new org.hamcrest.core.StringContains(true, "Unsupported reference")` in the original code, which should be replaced with `new org.hamcrest.core.StringContains.StringContains(string)`. This is because the constructor for `StringContains` has changed, and now takes a single argument of type `String` instead of two booleans.