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
    final String message = throwable.getMessage();
    assertThat(message, containsString("Unsupported reference"));
    assertThat(message, not(containsString(string)));
}
```