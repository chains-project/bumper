```java
// TODO: review this AI generated patch!
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable;
    try {
        org.junit.jupiter.api.Assertions.assertThrows(
                java.lang.IllegalArgumentException.class,
                () -> {
                    com.artipie.docker.ref.ManifestRef.parse(string);
                });
    } catch (final java.lang.IllegalArgumentException e) {
        throwable = e;
    }
}
```