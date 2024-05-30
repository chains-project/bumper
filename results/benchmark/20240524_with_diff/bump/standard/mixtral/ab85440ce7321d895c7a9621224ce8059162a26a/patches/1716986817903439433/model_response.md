Here's a possible patch for the client code:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.ref.ManifestRef.FromString(string).link().string());
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.core.AllOf<>(java.util.Arrays.asList(new org.hamcrest.core.StringContains.Containing("Unsupported reference"), new org.hamcrest.core.StringContains.ContainingIgnoringCase(string))));
}
```

The changes are as follows:

* Replace `new org.hamcrest.core.StringContains(true, "Unsupported reference")` with `new org.hamcrest.core.StringContains.Containing("Unsupported reference")`. This is because the `StringContains` constructor with a `boolean` argument has been removed in the new library version.
* Replace `new org.hamcrest.core.StringContains(false, string)` with `new org.hamcrest.core.StringContains.ContainingIgnoringCase(string)`. This is because the `StringContains` constructor with a `boolean` argument has been removed in the new library version.

Note that I assumed that the `Containing` and `ContainingIgnoringCase` classes were added in the new library version, since they were not marked as removed. If this is not the case, you may need to adjust the code accordingly.