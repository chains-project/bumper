Here is a proposed patch for the failing client code:
```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.ref.ManifestRef.FromString(string).link().string());
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.core.AllOf<>(java.util.Arrays.asList(new org.hamcrest.core.StringContains.ContainingIgnoringCase(string), new org.hamcrest.core.StringContains.StringStart("Unsupported reference"))));
}
```
The failure is caused by the fact that the `StringContains` constructor no longer accepts a `boolean` argument in the new library version. To fix this, I have replaced the `StringContains` constructor with the `StringContains.ContainingIgnoringCase` constructor, which accepts a `String` argument. I have also replaced the `StringContains` constructor with the `StringContains.StringStart` constructor, which also accepts a `String` argument. This should allow the code to compile and run successfully with the new library version.