Here is the fixed code:

```java
@ParameterizedTest
@ValueSource(strings = {
    "",
    "a:b:c",
    ".123"
})
void failsToResolveInvalid(final String string) {
    final Throwable throwable = Assertions.assertThrows(
        IllegalStateException.class,
        () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(
        throwable.getMessage(),
        CoreMatchers.containsString("Unsupported reference")
    );
    MatcherAssert.assertThat(
        throwable.getMessage(),
        CoreMatchers.not(CoreMatchers.containsString(string))
    );
}
```