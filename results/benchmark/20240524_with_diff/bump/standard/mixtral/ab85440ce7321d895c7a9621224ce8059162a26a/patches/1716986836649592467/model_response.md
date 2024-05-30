Here's the patched version of the failing method that should work with the new library version:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.ref.ManifestRef.FromString(string).link().string());
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.core.AllOf<>(java.util.Arrays.asList(new org.hamcrest.core.StringContains.StringContains(string), new org.hamcrest.core.StringContains.StringContains(false, string))));
}
```

The change I made is to replace the deprecated `org.hamcrest.core.StringContains` constructor with the new `org.hamcrest.core.StringContains.StringContains` constructor, which takes only a single argument. This should resolve the error you were seeing.