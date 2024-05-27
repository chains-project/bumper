```java
// TODO: review this AI generated patch!
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable;
    try {
        new org.eclipse.jgit.lib.Ref(string);
    } catch (final java.lang.IllegalArgumentException e) {
        throwable = e;
    }
}
```