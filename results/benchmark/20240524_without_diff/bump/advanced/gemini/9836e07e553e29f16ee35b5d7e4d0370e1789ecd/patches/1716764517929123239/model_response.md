```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    try {
        new org.apache.http.client.methods.HttpEntityEnclosingRequestBase("invalid");
        org.junit.jupiter.api.Assertions.fail("Should throw exception");
    } catch (final java.lang.IllegalArgumentException ex) {
        // expected
    }
}
```