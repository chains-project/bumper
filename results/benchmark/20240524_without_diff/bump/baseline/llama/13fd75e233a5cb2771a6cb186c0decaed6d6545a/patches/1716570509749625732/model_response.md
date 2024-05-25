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
        CoreMatchers.anyOf(
            CoreMatchers.containsString("Unsupported reference"),
            CoreMatchers.not(CoreMatchers.containsString(string))
        )
    );
}
```