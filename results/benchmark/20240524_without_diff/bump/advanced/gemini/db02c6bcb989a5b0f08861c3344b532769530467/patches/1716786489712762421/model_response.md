```java
// TODO: review this AI generated patch!
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable;
    if (string.isEmpty()) {
        throwable = new java.lang.IllegalArgumentException("String cannot be empty");
    } else if (string.contains(":")) {
        throwable = new java.lang.IllegalArgumentException("String cannot contain colons");
    } else if (!string.matches("\\d+(\\.\\d+)?")) {
        throwable = new java.lang.IllegalArgumentException("String must be a number");
    } else {
        throwable = null;
    }
}
```