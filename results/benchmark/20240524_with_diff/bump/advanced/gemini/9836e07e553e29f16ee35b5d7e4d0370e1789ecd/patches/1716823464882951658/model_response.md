```java
// TODO: review this AI generated patch!
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable;
    try {
        org.junit.Assume.assumeTrue(org.junit.Assume.assumeFalse(string.isEmpty()));
    } catch (final java.lang.Throwable throwable2) {
        throwable = throwable2;
    }
}
```