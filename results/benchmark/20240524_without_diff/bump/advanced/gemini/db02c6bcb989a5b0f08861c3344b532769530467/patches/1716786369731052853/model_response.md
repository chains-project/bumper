```java
// TODO: review this AI generated patch!
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable;
    try {
        new org.eclipse.microprofile.rest.client.RestClientBuilder().build(org.eclipse.microprofile.rest.client.RestClient.class);
    } catch (final java.lang.Throwable t) {
        throwable = t;
    }
}
```