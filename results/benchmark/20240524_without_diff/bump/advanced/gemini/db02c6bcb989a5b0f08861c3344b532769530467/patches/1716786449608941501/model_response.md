```java
// TODO: review this AI generated patch!
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable;
    try {
        // TODO: review this AI generated patch!
        org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalArgumentException.class, () -> {
            new org.eclipse.aether.impl.ArtifactResolver(null, null).resolveArtifact(null);
        });
    } catch (java.lang.Exception e) {
        throwable = e;
    }
}
```